import sys
import unittest
from unittest.mock import MagicMock, patch

# Mock Kodi and internal modules
sys.modules['xbmc'] = MagicMock()
sys.modules['xbmcgui'] = MagicMock()
sys.modules['xbmcplugin'] = MagicMock()
sys.modules['xbmcvfs'] = MagicMock()
sys.modules['xbmcaddon'] = MagicMock()

sys.modules['modules.kodi_utils'] = MagicMock()
sys.modules['modules.kodi_utils'].get_datetime = MagicMock(return_value='2026-02-01')
sys.modules['modules.settings'] = MagicMock()
sys.modules['modules.settings'].tmdb_api_key = MagicMock(return_value='test_key')
sys.modules['modules.settings'].mpaa_region = MagicMock(return_value='US')

sys.modules['apis.tmdb_api'] = MagicMock()
sys.modules['apis.tmdb_api'].tmdb_api_key = MagicMock(return_value='test_key')

class TestRecommendations(unittest.TestCase):
    @patch('modules.recommendations.get_recently_watched')
    @patch('modules.recommendations.movie_meta')
    def test_get_discovery_params(self, mock_movie_meta, mock_recently_watched):
        from modules.recommendations import recommendations_manager
        
        # Mock 3 watched movies: 2 Action (id 28), 1 Comedy (id 35)
        mock_recently_watched.return_value = [
            {'media_id': 1}, {'media_id': 2}, {'media_id': 3}
        ]
        
        def side_effect(type, id, key, region, date):
            if id == 1: return {'genre_ids': [28, 12]} # Action, Adventure
            if id == 2: return {'genre_ids': [28, 80]} # Action, Crime
            if id == 3: return {'genre_ids': [35]}     # Comedy
            return {}

        mock_movie_meta.side_effect = side_effect
        
        query = recommendations_manager.get_discovery_params('movie')
        
        # Top genre is 28 (Action), followed by 12, 80, or 35.
        # with_genres should contain 28.
        self.assertIn('with_genres=28', query)
        self.assertIn('sort_by=popularity.desc', query)
        print(f"Generated Query: {query}")

if __name__ == '__main__':
    unittest.main()
