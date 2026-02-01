# -*- coding: utf-8 -*-
from modules import kodi_utils
from caches.settings_cache import set_setting, get_setting

# Local imports
logger = kodi_utils.logger
kodi_dialog = kodi_utils.kodi_dialog
notification = kodi_utils.notification

def run_trakt_wizard(skip_confirm=False):
    """Trakt auth: same approach as Real-Debrid — user goes to trakt.tv/activate and enters the one-time PIN shown in the plugin."""
    if not skip_confirm and not kodi_utils.confirm_dialog(heading='VibeStream: Authorize Trakt',
                                     text='You will be shown a one-time PIN.\n\n'
                                          'Go to [B]trakt.tv/activate[/B] in your browser and enter that PIN to link your Trakt account.\n\n'
                                          'Continue?'):
        return

    from apis.trakt_api import trakt_authenticate, trakt_revoke_authentication
    trakt_revoke_authentication()  # Clear old token

    if trakt_authenticate():
        set_setting('trakt.user_keys_setup', 'true')
        kodi_dialog().ok('Success', 'Trakt is now authorized. Your watch history and lists will sync.')
    else:
        kodi_dialog().ok('Error', 'Authorization failed. Make sure you entered the PIN at trakt.tv/activate before it expired.')
