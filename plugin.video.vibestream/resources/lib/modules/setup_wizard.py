# -*- coding: utf-8 -*-
import json
from modules import kodi_utils
from modules.kodi_utils import debug_log
from caches.settings_cache import set_setting, get_setting

# Local imports
kodi_dialog = kodi_utils.kodi_dialog
notification = kodi_utils.notification
confirm_dialog = kodi_utils.confirm_dialog
select_dialog = kodi_utils.select_dialog

def run_setup_wizard():
	try:
		return _run_setup_wizard()
	except Exception as e:
		kodi_utils.logger('VibeStream setup_wizard', str(e))
		set_setting('vibestream.setup_wizard_run', 'true')
		return False

def _run_setup_wizard():
	debug_log('setup_wizard.py:_run_setup_wizard', 'start', {}, 'H2')
	# 1. Welcome — user can skip and go straight to the addon
	if not confirm_dialog(heading='Welcome to VibeStream!',
						 text='This wizard will help you set up Trakt, Real-Debrid, and your Quality Presets for the best experience.\n\nStart setup now?',
						 ok_label='Start Setup', cancel_label='Skip for Now'):
		debug_log('setup_wizard.py:_run_setup_wizard', 'user skipped wizard', {}, 'H2')
		set_setting('vibestream.setup_wizard_run', 'true')
		return False

	# 2. Trakt Setup (auth first so user expects it before quality)
	try:
		from modules.trakt_auth_wizard import run_trakt_wizard
		run_trakt_wizard(skip_confirm=True)
	except Exception as e:
		kodi_utils.logger('VibeStream setup_wizard Trakt', str(e))
		notification('Trakt setup skipped due to an error.', 4000)

	# 3. Quality Preset
	from modules.quality_manager import PRESETS, PRESET_1080P_BALANCED
	preset_choices = [
		('4K / Ultra (Best for high-speed fiber)', '4k_ultra'),
		('Full HD Balanced (Recommended for most)', '1080p_balanced'),
		('HD Efficient (Good for mobile/slow internet)', '720p_efficient'),
		('Low / Slow (Maximum stability)', 'low')
	]
	labels = [i[0] for i in preset_choices]
	list_items = [{'line1': label} for label in labels]
	kwargs = {'items': json.dumps(list_items), 'heading': 'Select Quality Preset'}
	choice = select_dialog(labels, **kwargs)
	if choice:
		matches = [i[1] for i in preset_choices if i[0] == choice]
		if matches:
			set_setting('vibestream.quality.preset', matches[0])

	# 4. Real-Debrid Setup
	try:
		if confirm_dialog(heading='Real-Debrid Setup', text='Do you want to authorize Real-Debrid now?'):
			from apis.real_debrid_api import RealDebridAPI
			RealDebridAPI().auth()
	except Exception as e:
		kodi_utils.logger('VibeStream setup_wizard Real-Debrid', str(e))

	# Final
	set_setting('vibestream.setup_wizard_run', 'true')
	debug_log('setup_wizard.py:_run_setup_wizard', 'wizard complete, returning True', {}, 'H2')
	try:
		kodi_utils.ok_dialog('Setup Complete', 'VibeStream is now configured! Enjoy your movies and shows.')
	except Exception as e:
		kodi_utils.logger('VibeStream setup_wizard final', str(e))
		notification('Setup complete.', 3000)
	return True

def first_run_check():
	wizard_not_run = get_setting('vibestream.setup_wizard_run', 'false') == 'false'
	debug_log('setup_wizard.py:first_run_check', 'entry', {'wizard_not_run': wizard_not_run}, 'H2')
	if wizard_not_run:
		result = run_setup_wizard()
		debug_log('setup_wizard.py:first_run_check', 'run_setup_wizard returned', {'result': result}, 'H2')
		return result
	debug_log('setup_wizard.py:first_run_check', 'skipping wizard (already run)', {}, 'H2')
	return False
