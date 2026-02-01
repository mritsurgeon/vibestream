# -*- coding: utf-8 -*-
from modules.watched_status import get_recently_watched
from modules.metadata import movie_meta, tvshow_meta
from modules.settings import tmdb_api_key, mpaa_region
from modules.utils import get_datetime
from apis.tmdb_api import tmdb_api_key as get_tmdb_key
from caches.main_cache import main_cache

# Cache discovery params so "New For You" doesn't refetch metadata every time (5 min TTL)
DISCOVERY_CACHE_PREFIX = 'vibestream_discovery_'
DISCOVERY_CACHE_HOURS = 5 / 60.0  # ~5 minutes (base_cache expiration is in hours)

class RecommendationsManager:
    def __init__(self):
        self.tmdb_key = get_tmdb_key()
        self.mpaa_region = mpaa_region()

    def get_discovery_params(self, media_type):
        """
        Analyzes recent history and returns TMDb discovery query string.
        Cached briefly to avoid slow repopulation; uses fewer metadata lookups.
        """
        cache_key = '%s%s' % (DISCOVERY_CACHE_PREFIX, media_type)
        cached = main_cache.get(cache_key)
        if cached is not None:
            return cached

        recently_watched = get_recently_watched(media_type, short_list=1)
        if not recently_watched:
            return None

        genre_counts = {}
        # Analyze only top 5 items to keep "New For You" fast
        for item in recently_watched[:5]:
            tmdb_id = item.get('media_id') or (item.get('media_ids') or {}).get('tmdb')
            if not tmdb_id:
                continue
            try:
                if media_type == 'movie':
                    meta = movie_meta('tmdb_id', tmdb_id, self.tmdb_key, self.mpaa_region, get_datetime())
                else:
                    meta = tvshow_meta('tmdb_id', tmdb_id, self.tmdb_key, self.mpaa_region, get_datetime())
                for g_id in (meta.get('genre_ids') or []):
                    genre_counts[g_id] = genre_counts.get(g_id, 0) + 1
            except Exception:
                continue

        if not genre_counts:
            return None

        sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
        top_genres = [str(g[0]) for g in sorted_genres[:2]]
        query = "with_genres=%s&sort_by=popularity.desc" % ",".join(top_genres)
        main_cache.set(cache_key, query, expiration=DISCOVERY_CACHE_HOURS)
        return query

recommendations_manager = RecommendationsManager()
