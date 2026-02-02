import sys
import unittest
import os
from unittest.mock import MagicMock, patch

# Mock Kodi modules
sys.modules['xbmc'] = MagicMock()
sys.modules['xbmcgui'] = MagicMock()
sys.modules['xbmcplugin'] = MagicMock()
sys.modules['xbmcvfs'] = MagicMock()
sys.modules['xbmcaddon'] = MagicMock()

# Mock internal modules
sys.modules['modules.kodi_utils'] = MagicMock()
sys.modules['modules.kodi_utils'].addon_profile = MagicMock(return_value='/tmp')
sys.modules['modules.kodi_utils'].path_join = lambda *args: '/'.join(args)
sys.modules['modules.kodi_utils'].exists = MagicMock(return_value=True)
sys.modules['modules.kodi_utils'].mkdirs = MagicMock()

import modules.health_manager

class TestHealthManager(unittest.TestCase):
    def test_record_and_score(self):
        db_file = '/tmp/test_health_robust.db'
        if os.path.exists(db_file): os.remove(db_file)
        
        # Patch precisely BEFORE instantiating
        with patch('modules.health_manager.path_join', return_value=db_file):
            hm = modules.health_manager.HosterHealthManager()
            
            # Neutral score
            self.assertEqual(hm.get_health_score('test_hoster'), 1.0)
            
            # Record events
            hm.record_event('test_hoster', 1) # Success
            hm.record_event('test_hoster', 0) # Failure
            
            score = hm.get_health_score('test_hoster')
            # print(f"DEBUG: Score after S/F: {score}")
            self.assertEqual(score, 0.5)
            
            hm.record_event('test_hoster', 1)
            hm.record_event('test_hoster', 1)
            hm.record_event('test_hoster', 1)
            
            score = hm.get_health_score('test_hoster')
            # print(f"DEBUG: Score after S/F,S,S,S: {score}")
            self.assertEqual(score, 0.8)

if __name__ == '__main__':
    unittest.main()
