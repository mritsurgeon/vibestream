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
    try:
        trakt_revoke_authentication()  # Clear old token
    except Exception as e:
        logger('VibeStream trakt_wizard revoke', str(e))

    # During wizard skip sync to avoid DB ops (and possible malformed DB) before setup completes
    try:
        ok = trakt_authenticate(skip_sync=skip_confirm)
    except Exception as e:
        logger('VibeStream trakt_wizard authenticate', str(e))
        notification('Trakt authorization error.', 4000)
        return
    if ok:
        set_setting('trakt.user_keys_setup', 'true')
        if skip_confirm:
            # Wizard flow: don't show blocking ok_dialog so we can continue to next step (Real-Debrid)
            notification('Trakt authorized. Continuing setup…', 2500)
        else:
            try:
                kodi_dialog().ok('Success', 'Trakt is now authorized. Your watch history and lists will sync.')
            except Exception:
                notification('Trakt authorized.', 3000)
    else:
        try:
            kodi_dialog().ok('Error', 'Authorization failed. Make sure you entered the PIN at trakt.tv/activate before it expired.')
        except Exception:
            notification('Authorization failed.', 4000)
