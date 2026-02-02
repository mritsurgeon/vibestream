# -*- coding: utf-8 -*-
import sqlite3
import time
from modules.kodi_utils import addon_profile, path_join, mkdirs, exists

# Health Score Decay: Ignore events older than 7 days
DECAY_DAYS = 7
DB_NAME = 'health_db'

class HosterHealthManager:
    def __init__(self):
        self._db_path = path_join(addon_profile(), 'health.db')
        self._initialize_db()

    def _initialize_db(self):
        if not exists(addon_profile()): mkdirs(addon_profile())
        dbcon = sqlite3.connect(self._db_path, timeout=10)
        dbcon.execute("CREATE TABLE IF NOT EXISTS hoster_events "
                      "(hoster_name TEXT, event_type INTEGER, latency REAL, timestamp INTEGER)")
        dbcon.execute("CREATE INDEX IF NOT EXISTS ix_hoster_name ON hoster_events (hoster_name)")
        dbcon.commit()
        dbcon.close()

    def record_event(self, hoster_name, event_type, latency=0.0):
        """
        event_type: 1 for success, 0 for failure
        """
        try:
            dbcon = sqlite3.connect(self._db_path, timeout=10)
            dbcon.execute("INSERT INTO hoster_events VALUES (?, ?, ?, ?)",
                          (hoster_name, event_type, latency, int(time.time())))
            dbcon.commit()
            dbcon.close()
        except Exception: pass

    def get_health_score(self, hoster_name):
        """
        Returns a score between 0.0 and 1.0. 
        Calculates: Success Rate * Latency Factor
        """
        try:
            cutoff = int(time.time()) - (DECAY_DAYS * 24 * 3600)
            dbcon = sqlite3.connect(self._db_path, timeout=10)
            
            # Get success/failure counts
            cursor = dbcon.execute("SELECT event_type, COUNT(*) FROM hoster_events "
                                   "WHERE hoster_name = ? AND timestamp > ? GROUP BY event_type", 
                                   (hoster_name, cutoff))
            results = dict(cursor.fetchall())
            dbcon.close()

            successes = results.get(1, 0)
            failures = results.get(0, 0)
            total = successes + failures

            if total == 0: return 1.0 # New/neutral hoster
            
            success_rate = float(successes) / total
            
            # Basic penalty for frequent failures
            # We skip latency factor for now to keep it simple
            return success_rate
        except Exception:
            return 1.0

    def cleanup_old_events(self):
        try:
            cutoff = int(time.time()) - (DECAY_DAYS * 24 * 3600)
            dbcon = sqlite3.connect(self._db_path, timeout=10)
            dbcon.execute("DELETE FROM hoster_events WHERE timestamp < ?", (cutoff,))
            dbcon.commit()
            dbcon.close()
        except Exception: pass

health_manager = HosterHealthManager()
