import sys
import unittest
from unittest.mock import MagicMock, patch
import os

# Create a concrete base class instead of a MagicMock to avoid inheritance issues
class MockXbmcPlayer:
    def __init__(self): pass
    def isPlayingVideo(self): return False
    def getTime(self): return 0
    def getTotalTime(self): return 0
    def stop(self): pass

# Mock Kodi modules
xbmc = MagicMock()
xbmc.Player = MockXbmcPlayer
sys.modules['xbmc'] = xbmc
sys.modules['xbmcgui'] = MagicMock()
sys.modules['xbmcplugin'] = MagicMock()
sys.modules['xbmcvfs'] = MagicMock()
sys.modules['xbmcaddon'] = MagicMock()

# Mock kodi_utils to return our MockXbmcPlayer for 'xbmc_player'
mock_ku = MagicMock()
mock_ku.xbmc_player = MockXbmcPlayer
sys.modules['modules.kodi_utils'] = mock_ku

# Setup paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import modules.player as player_module
from modules.player import VibeStreamPlayer

class TestWatchdog(unittest.TestCase):

    def setUp(self):
        # Directly patch variables in player_module
        self.patch_list = [
            patch.object(player_module, 'get_visibility'),
            patch.object(player_module, 'sleep'),
            patch.object(player_module, 'notification'),
            patch.object(player_module, 'hide_busy_dialog')
        ]
        
        self.mocks = {}
        for p in self.patch_list:
            m = p.start()
            setattr(self, f'mock_{p.attribute}', m)
            
        self.player = VibeStreamPlayer()
        self.player.sources_object = MagicMock()
        self.player.media_type = 'movie'
        self.player.num_episodes = 0
        
        # Now we can safely mock the methods on the instance
        self.player.isPlayingVideo = MagicMock()
        self.player.getTime = MagicMock()
        self.player.getTotalTime = MagicMock()
        self.player.retry_next_source = MagicMock()
        self.player.playback_close_dialogs = MagicMock()
        self.player.media_watched_marker = MagicMock()
        self.player.clear_playback_properties = MagicMock()
        self.player.clear_playing_item = MagicMock()
        self.player.kill_dialog = MagicMock()

    def tearDown(self):
        for p in self.patch_list:
            p.stop()

    def test_watchdog_timeout_triggers_fallback(self):
        # Setup mocks
        self.player.isPlayingVideo.side_effect = [True] * 20 + [False]
        # start_time will be 120, then curr_time will be 121, 122...
        self.player.getTime.side_effect = range(120, 150)
        self.player.getTotalTime.return_value = 6000
        
        def mock_vis_side_effect(prop):
            if prop == player_module.video_fullscreen_check: return True # Break first loop
            if prop == 'Player.Caching': return True
            if prop == 'Player.Paused': return False
            return True
            
        self.mock_get_visibility.side_effect = mock_vis_side_effect
        
        # Run monitor
        self.player.monitor()
        
        # Verify fallback was triggered
        self.player.retry_next_source.assert_called_once()
        self.mock_notification.assert_any_call('Buffering Detected. Switching Source...', 3000)

    def test_watchdog_no_fallback_on_normal_playback(self):
        # Setup mocks
        self.player.isPlayingVideo.side_effect = [True] * 5 + [False]
        self.player.getTime.return_value = 120
        self.player.getTotalTime.return_value = 6000
        
        def mock_vis_side_effect(prop):
            if prop == player_module.video_fullscreen_check: return True
            if prop == 'Player.Caching': return False
            return True
            
        self.mock_get_visibility.side_effect = mock_vis_side_effect
        
        # Run monitor
        self.player.monitor()
        
        # Verify fallback was NOT triggered
        self.player.retry_next_source.assert_not_called()

if __name__ == '__main__':
    unittest.main()
