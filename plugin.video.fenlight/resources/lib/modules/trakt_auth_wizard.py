# -*- coding: utf-8 -*-
from modules import kodi_utils
from caches.settings_cache import set_setting, get_setting

# Local imports
logger = kodi_utils.logger
kodi_dialog = kodi_utils.kodi_dialog
select_dialog = kodi_utils.select_dialog
notification = kodi_utils.notification
execute_builtin = kodi_utils.execute_builtin

def run_trakt_wizard(skip_confirm=False):
    if not skip_confirm and not kodi_utils.confirm_dialog(heading='VibeStream: Trakt Modernization', 
                                     text='To prevent API issues, VibeStream now requires your own Trakt App credentials.\n\nDo you want to set this up now? (Recommended)'):
        return

    # Step 1: Explanation & Link
    text = "1. Go to: [B]https://trakt.tv/oauth/applications/new[/B]\n" \
           "2. Name: VibeStream (or anything)\n" \
           "3. Redirect URI: [B]urn:ietf:wg:oauth:2.0:oob[/B]\n" \
           "4. Save App.\n\n" \
           "Click OK when you are ready to enter keys."
    
    # We can show a QR code or just text.
    kodi_dialog().ok('Create Trakt App', text)
    
    # Optional: Open browser on specific platforms?
    # execute_builtin('RunScript(script.module.webinterface, url=https://trakt.tv/oauth/applications/new)') # Hypothetical
    
    # Step 2: Client ID
    client_id = kodi_dialog().input('Enter Trakt Client ID (from your new App)')
    if not client_id: return notification('Setup Cancelled')
    
    # Step 3: Client Secret
    client_secret = kodi_dialog().input('Enter Trakt Client Secret')
    if not client_secret: return notification('Setup Cancelled')
    
    # Save Keys
    set_setting('trakt.client', client_id)
    set_setting('trakt.secret', client_secret)
    
    # Step 4: Authenticate
    from apis.trakt_api import trakt_authenticate, trakt_revoke_authentication
    trakt_revoke_authentication() # Clear old token
    
    if trakt_authenticate():
        from caches.settings_cache import set_setting
        set_setting('trakt.user_keys_setup', 'true')
        kodi_dialog().ok('Success', 'Trakt is now configured with your personal keys!\nRate limiting issues should be resolved.')
    else:
        kodi_dialog().ok('Error', 'Authentication failed. Please check your keys and try again.')
