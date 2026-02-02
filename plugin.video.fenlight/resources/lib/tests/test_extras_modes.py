import sys
import unittest
from unittest.mock import MagicMock, patch

# Mock Kodi modules
sys.modules['xbmc'] = MagicMock()
sys.modules['xbmcgui'] = MagicMock()
sys.modules['xbmcplugin'] = MagicMock()
sys.modules['xbmcvfs'] = MagicMock()
sys.modules['xbmcaddon'] = MagicMock()

# Mock internal modules
sys.modules['modules.kodi_utils'] = MagicMock()
sys.modules['modules.settings'] = MagicMock()
sys.modules['modules.watched_status'] = MagicMock()
sys.modules['modules.utils'] = MagicMock()
sys.modules['modules.meta_lists'] = MagicMock()
sys.modules['modules.metadata'] = MagicMock()
sys.modules['modules.episode_tools'] = MagicMock()
sys.modules['modules.sources'] = MagicMock()
sys.modules['apis.tmdb_api'] = MagicMock()
sys.modules['apis.imdb_api'] = MagicMock()
sys.modules['apis.omdb_api'] = MagicMock()
sys.modules['apis.trakt_api'] = MagicMock()
sys.modules['indexers.dialogs'] = MagicMock()
sys.modules['indexers.people'] = MagicMock()
sys.modules['indexers.images'] = MagicMock()

# Mock BaseDialog before importing Extras
import windows.base_window
windows.base_window.BaseDialog = MagicMock

from windows.extras import Extras

class TestExtrasModes(unittest.TestCase):
    def setUp(self):
        # Setup dummy methods on Extras so getattr works
        methods = [
            'set_artwork', 'set_infoline1', 'set_infoline2', 'make_ratings', 'make_cast', 'make_recommended', 
            'make_more_like_this', 'make_reviews', 'make_comments', 'make_in_lists', 'make_trivia', 
            'make_blunders', 'make_parentsguide', 'make_videos', 'make_year', 'make_genres', 
            'make_network', 'make_collection'
        ]
        for m in methods:
            setattr(Extras, m, MagicMock(__name__=m))
        
        # Mocking methods that __init__ calls
        Extras.set_starting_constants = MagicMock()
        Extras.set_properties = MagicMock()

    @patch('windows.extras.extras_view_mode')
    def test_extras_tasks_simple(self, mock_view_mode):
        mock_view_mode.return_value = 0 # Simple
        extras = Extras()
        
        # Verify tasks
        task_names = [t.__name__ for t in extras.tasks]
        self.assertIn('make_recommended', task_names)
        self.assertIn('make_videos', task_names)
        self.assertNotIn('make_trivia', task_names)

    @patch('windows.extras.extras_view_mode')
    def test_extras_tasks_advanced(self, mock_view_mode):
        mock_view_mode.return_value = 1 # Advanced
        extras = Extras()
        
        # Verify tasks
        task_names = [t.__name__ for t in extras.tasks]
        self.assertIn('make_recommended', task_names)
        self.assertIn('make_trivia', task_names)
        self.assertIn('make_blunders', task_names)

if __name__ == '__main__':
    unittest.main()
