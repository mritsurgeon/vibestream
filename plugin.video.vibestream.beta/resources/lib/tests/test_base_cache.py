import sys
import unittest
from unittest.mock import MagicMock, patch
import os
import json
import sqlite3

# Mock Kodi modules BEFORE importing anything from the addon
sys.modules['xbmc'] = MagicMock()
sys.modules['xbmcgui'] = MagicMock()
sys.modules['xbmcplugin'] = MagicMock()
sys.modules['xbmcvfs'] = MagicMock()
sys.modules['xbmcaddon'] = MagicMock()

# Setup paths to allow importing modules
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Now we can import the module under test
# We need to mock kodi_utils because it is imported by base_cache
# and doing so will try to access the mocked xbmc modules, which is fine, 
# but we want to control what kodi_utils returns.

class TestBaseCache(unittest.TestCase):

    def setUp(self):
        # Create a temporary database file
        self.db_file = os.path.join(current_dir, 'test_cache.db')
        self.table_name = 'test_table'
        
        # Setup the database table
        conn = sqlite3.connect(self.db_file)
        conn.execute(f'CREATE TABLE IF NOT EXISTS {self.table_name} (id text unique, data text, expires integer)')
        conn.close()

        # Patch kodi_utils in base_cache
        self.kodi_patcher = patch('caches.base_cache.kodi_utils')
        self.mock_kodi_utils = self.kodi_patcher.start()
        
        # Mock specific kodi_utils functions used by BaseCache
        self.mock_kodi_utils.get_property.return_value = None
        self.mock_kodi_utils.connect_database = sqlite3.connect # Use real sqlite3 for tests
        
        # Patch connect_database to accept our path directly
        self.connect_patcher = patch('caches.base_cache.connect_database')
        self.mock_connect = self.connect_patcher.start()
        self.mock_connect.side_effect = lambda x: sqlite3.connect(x, isolation_level=None)
        
        # Import BaseCache here to ensure mocks are in place
        from caches.base_cache import BaseCache
        
        self.cache = BaseCache(self.db_file, self.table_name)
              
    def tearDown(self):
        self.connect_patcher.stop()
        self.kodi_patcher.stop()
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    def test_set_and_get_json(self):
        from caches.base_cache import BaseCache
        
        # Test Data
        key = "test_key"
        data = {"foo": "bar", "baz": 123}
        
        # Set
        self.cache.set(key, data)
        
        # Get
        result = self.cache.get(key)
        self.assertEqual(result, data)
        
        # Verify it is stored as JSON in DB
        conn = sqlite3.connect(self.db_file)
        cursor = conn.execute(f"SELECT data FROM {self.table_name} WHERE id=?", (key,))
        stored_data = cursor.fetchone()[0]
        conn.close()
        
        # Should be a JSON string, not a repr string
        self.assertEqual(stored_data, json.dumps(data))
        
    def test_legacy_data_clearing(self):
        # Simulate legacy data (repr format)
        key = "legacy_key"
        legacy_data = "{'foo': 'bar'}" # python dict string representation
        expires = 9999999999
        
        conn = sqlite3.connect(self.db_file)
        conn.execute(f"INSERT INTO {self.table_name} (id, data, expires) VALUES (?, ?, ?)", 
                     (key, legacy_data, expires))
        conn.commit()
        conn.close()
        
        # Try to Get
        # It should fail json.loads, catch exception, and delete the entry
        result = self.cache.get(key)
        
        self.assertIsNone(result)
        
        # Verify it's gone from DB
        conn = sqlite3.connect(self.db_file)
        cursor = conn.execute(f"SELECT count(*) FROM {self.table_name} WHERE id=?", (key,))
        count = cursor.fetchone()[0]
        conn.close()
        self.assertEqual(count, 0)

if __name__ == '__main__':
    unittest.main()
