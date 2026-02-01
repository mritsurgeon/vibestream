# -*- coding: utf-8 -*-
from modules import kodi_utils
from caches.settings_cache import set_setting, get_setting

# Local imports
kodi_dialog = kodi_utils.kodi_dialog
notification = kodi_utils.notification
confirm_dialog = kodi_utils.confirm_dialog
select_dialog = kodi_utils.select_dialog

def run_setup_wizard():
	# 1. Welcome — user can skip and go straight to the addon
	if not confirm_dialog(heading='Welcome to VibeStream!',
						 text='This wizard will help you set up Trakt, Real-Debrid, and your Quality Presets for the best experience.\n\nStart setup now?',
						 ok_label='Start Setup', cancel_label='Skip for Now'):
		set_setting('vibestream.setup_wizard_run', 'true')
		return

	# 2. Quality Preset
	from modules.quality_manager import PRESETS, PRESET_1080P_BALANCED
	preset_choices = [
		('4K / Ultra (Best for high-speed fiber)', '4k_ultra'),
		('Full HD Balanced (Recommended for most)', '1080p_balanced'),
		('HD Efficient (Good for mobile/slow internet)', '720p_efficient'),
		('Low / Slow (Maximum stability)', 'low')
	]
	labels = [i[0] for i in preset_choices]
	choice = select_dialog(labels, heading='Select Quality Preset')
	if choice:
		preset_id = [i[1] for i in preset_choices if i[0] == choice][0]
		set_setting('vibestream.quality.preset', preset_id)

	# 3. Trakt Setup
	from modules.trakt_auth_wizard import run_trakt_wizard
	run_trakt_wizard(skip_confirm=True)

	# 4. Real-Debrid Setup
	if confirm_dialog(heading='Real-Debrid Setup', text='Do you want to authorize Real-Debrid now?'):
		from apis.real_debrid_api import RealDebridAPI
		RealDebridAPI().auth()

	# Final
	set_setting('vibestream.setup_wizard_run', 'true')
	kodi_utils.ok_dialog('Setup Complete', 'VibeStream is now configured! Enjoy your movies and shows.')

def first_run_check():
	if get_setting('vibestream.setup_wizard_run', 'false') == 'false':
		run_setup_wizard()
