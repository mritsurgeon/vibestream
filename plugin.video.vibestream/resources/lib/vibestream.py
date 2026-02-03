# -*- coding: utf-8 -*-
import sys
from modules.router import routing, sys_exit_check
from modules.kodi_utils import debug_log
# from modules.kodi_utils import logger

debug_log('vibestream.py', 'entry', {'argv_len': len(sys.argv), 'argv': list(sys.argv)}, 'H1')
mode = routing(sys)
# Do not exit when we just showed the main list (e.g. after skipping wizard), or after auth-only actions
action_only_modes = ('trakt.trakt_authenticate', 'trakt.trakt_revoke_authentication',
	'real_debrid.authenticate', 'real_debrid.revoke_authentication',
	'premiumize.authenticate', 'premiumize.revoke_authentication',
	'alldebrid.authenticate', 'alldebrid.revoke_authentication',
	'offcloud.authenticate', 'offcloud.revoke_authentication',
	'easydebrid.authenticate', 'easydebrid.revoke_authentication',
	'torbox.authenticate', 'torbox.revoke_authentication',
	'tmdb.authenticate', 'tmdb.deauth', 'open_settings')
if mode != 'navigator.main' and mode not in action_only_modes and sys_exit_check():
	sys.exit(1)

