# -*- coding: utf-8 -*-
import time
import sqlite3 as database
from modules import kodi_utils
from caches.base_cache import current_dbs, database_locations
# from modules.kodi_utils import logger

from caches.settings_cache import get_setting, set_setting

notification = kodi_utils.notification
logger = kodi_utils.logger

class CacheManager:
    def __init__(self):
        self.max_db_size_mb = 50 # MB
        self.max_cache_age_days = 7
        self.maintenance_enabled = get_setting('vibestream.maintenance.enabled', 'true') == 'true'
        self.notify = get_setting('vibestream.maintenance.notify', 'false') == 'true'

    def check_health(self):
        """
        Entry point to check health of automation. 
        Should be called periodically.
        """
        if not self.maintenance_enabled:
            return

        should_clean = False
        total_size_mb = self._get_db_size()
        
        if total_size_mb > self.max_db_size_mb:
            logger('CacheMan', f'DB Size ({total_size_mb}MB) exceeds limit ({self.max_db_size_mb}MB)')
            should_clean = True
            
        # We could also check for "old cache" here specifically, 
        # but usually we just run maintenance if size is big OR periodically.
        # For "Smart" hygiene, let's also enforce a strict periodic cleanup
        # regardless of size, e.g. every check (if it's cheap) or rely on size.
        # The prompt says: "Auto-clean when DB > X MB OR Cache entries older than N days"
        
        # To check "Cache entries older than N days" efficiently involves querying the DBs.
        # We can just run the cleanup logic which does the check in SQL.
        # Running it every time might be too heavy?
        # Let's run it if DB size is high OR if we haven't run it in > 24 hours.
        
        last_run = float(get_setting('vibestream.maintenance.last_run', '0.0'))
        days_since_run = (time.time() - last_run) / 86400.0
        
        if days_since_run > 1.0: # Run at least daily
            should_clean = True
            
        if should_clean:
            self.run_maintenance()

    def run_maintenance(self):
        logger('CacheMan', 'Starting Maintenance')
        start_time = time.time()
        
        # 1. Clean Expired & Old Entries
        deleted_count = self._clean_old_cache(self.max_cache_age_days)
        
        # 2. Optimize DB (Vacuum)
        self._optimize_db()
        
        set_setting('vibestream.maintenance.last_run', str(time.time()))
        
        duration = time.time() - start_time
        logger('CacheMan', f'Maintenance complete in {duration:.2f}s. Removed {deleted_count} items.')
        
        if self.notify and deleted_count > 0:
            notification(f'VibeStream Cache Optimized. Freed {deleted_count} items.')

    def _get_db_size(self):
        total_size = 0
        try:
            for db_name in current_dbs:
                 if db_name in database_locations and kodi_utils.path_exists(database_locations[db_name]):
                     total_size += kodi_utils.get_size(database_locations[db_name])
        except Exception as e:
            logger('CacheMan', f'Error calculating DB size: {e}')
        
        return total_size / (1024 * 1024.0) # MB

    def _clean_old_cache(self, days):
        """
        Removes entries that are expired OR older than 'days' (if we tracked creation time, which we don't for all).
        Standard BaseCache only tracks 'expires'.
        For now, let's aggressively prune 'expires' < now (standard cleanup)
        AND maybe prune things that are valid but very old? 
        BaseCache table: id, data, expires.
        We don't have 'created_at'.
        So strictly: Delete where expires < current_time (Clean expired).
        
        If we want to enforce "Cache entries older than N days", we implicitly assume
        that if it expires in the far future but we haven't touched it... well BaseCache doesn't track access time either.
        
        So the best "Hygiene" we can do on existing DBs is:
        1. Delete expired items (expires < now).
        """
        count = 0
        current_time = int(time.time())
        # Iterate all cache DBs
        for db_name, location in database_locations.items():
            if not kodi_utils.path_exists(location):
                continue
            
            # Find which table belongs to this DB?
            # caches.base_cache.table_creators has the schema.
            # We can try to guess the table names.
            # actually base_cache.integrity_check maps db_name -> tables.
            
            from caches.base_cache import integrity_check
            tables = integrity_check.get(db_name, [])
            
            try:
                conn = database.connect(location, isolation_level=None)
                for table in tables:
                     # Check if table has 'expires' column
                     # This is a bit hacky, but robust enough for hygiene
                     try:
                         # 1. Delete expired
                         cursor = conn.execute(f"DELETE FROM {table} WHERE expires < ?", (current_time,))
                         count += cursor.rowcount
                         
                         # 2. (Optional) Enforce max age if we had created_at. We don't.
                     except sqlite3.OperationalError:
                         # Table might not have expires column (e.g. settings table)
                         pass
                conn.close()
            except Exception as e:
                logger('CacheMan', f'Error cleaning {db_name}: {e}')
                
        return count

    def _optimize_db(self):
        for db_name, location in database_locations.items():
            if not kodi_utils.path_exists(location):
                continue
            try:
                conn = database.connect(location, isolation_level=None)
                conn.execute("VACUUM")
                conn.execute("ANALYZE")
                conn.close()
            except Exception as e:
                logger('CacheMan', f'Error optimizing {db_name}: {e}')
