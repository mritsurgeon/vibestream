import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Mock Kodi modules BEFORE importing anything from the addon
sys.modules['xbmc'] = MagicMock()
sys.modules['xbmcgui'] = MagicMock()
sys.modules['xbmcplugin'] = MagicMock()
sys.modules['xbmcvfs'] = MagicMock()
sys.modules['xbmcaddon'] = MagicMock()

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

class TestCacheManager(unittest.TestCase):
    def setUp(self):
        self.kodi_patcher = patch('modules.cache_manager.kodi_utils')
        self.mock_kodi = self.kodi_patcher.start()
        
        # Provide all attributes accessed at import time
        self.mock_kodi.notification = MagicMock()
        self.mock_kodi.addon_name = "VibeStream"
        self.mock_kodi.logger = MagicMock()
        self.mock_kodi.path_exists = MagicMock()
        self.mock_kodi.get_size = MagicMock()

        # Patch settings directly in cache_manager since they are imported "from..."
        self.settings_patcher = patch('modules.cache_manager.get_setting')
        self.mock_get_setting = self.settings_patcher.start()
        
        self.settings_set_patcher = patch('modules.cache_manager.set_setting')
        self.mock_set_setting = self.settings_set_patcher.start()
        
        # Default settings mock side_effect
        def get_setting_side_effect(key, default):
            if key == 'vibestream.maintenance.enabled': return 'true'
            if key == 'vibestream.maintenance.last_run': return '0.0'
            return default
        self.mock_get_setting.side_effect = get_setting_side_effect
        
        from modules.cache_manager import CacheManager
        self.CacheManager = CacheManager

    def tearDown(self):
        self.kodi_patcher.stop()
        self.settings_patcher.stop()
        self.settings_set_patcher.stop()

    def test_health_check_triggered_by_size(self):
        cm = self.CacheManager()
        
        # Mock DB size = 100MB (limit is 50)
        with patch.object(cm, '_get_db_size', return_value=100.0):
            with patch.object(cm, 'run_maintenance') as mock_maintain:
                cm.check_health()
                mock_maintain.assert_called_once()

    def test_health_check_triggered_by_time(self):
        cm = self.CacheManager()
        # Mock DB size = 10MB (under limit)
        with patch.object(cm, '_get_db_size', return_value=10.0):
             with patch.object(cm, 'run_maintenance') as mock_maintain:
                 cm.check_health()
                 # Last run was 0.0 (1970), so it should run
                 mock_maintain.assert_called_once()
                 
    def test_health_check_respects_setting(self):
        # Disable maintenance in settings
        self.mock_get_setting.side_effect = lambda k, d: 'false' if 'enabled' in k else d
        
        cm = self.CacheManager()
        with patch.object(cm, 'run_maintenance') as mock_maintain:
            cm.check_health()
            mock_maintain.assert_not_called()

if __name__ == '__main__':
    unittest.main()
