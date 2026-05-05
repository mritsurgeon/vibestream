# -*- coding: utf-8 -*-
from modules.watched_status import get_recently_watched
from modules.metadata import movie_meta, tvshow_meta
from modules.settings import tmdb_api_key, mpaa_region
from modules.utils import get_datetime
from modules import kodi_utils
from apis.tmdb_api import tmdb_api_key as get_tmdb_key, tmdb_movies_recommendations, tmdb_tv_recommendations, tmdb_movies_popular, tmdb_tv_popular
from modules.watched_status import get_watched_items
from caches.main_cache import main_cache

logger = kodi_utils.logger

# Cache discovery params so "New For You" doesn't refetch metadata every time (5 min TTL)
DISCOVERY_CACHE_PREFIX = 'vibestream_discovery_'
DISCOVERY_CACHE_HOURS = 5 / 60.0  # ~5 minutes (base_cache expiration is in hours)

# Because You Watched: cache merged results (5 min TTL)
BECAUSE_YOU_WATCHED_PREFIX = 'vibestream_because_you_watched_'
BECAUSE_YOU_WATCHED_HOURS = 5 / 60.0
BECAUSE_YOU_WATCHED_SEEDS = 5  # Use last N watched items as seeds
BECAUSE_YOU_WATCHED_PER_SEED = 10  # Recommendations per seed

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

    def get_because_you_watched(self, media_type, page_no=1, page_limit=20):
        """
        Build personalized recommendations with "Because you watched X" for each item.
        Uses: recently watched (Trakt/local) → TMDB recommendations per seed.
        Returns: (list of {'tmdb_id': int, 'because_you_watched': str}, total_pages)
        """
        cache_key = '%s%s_full' % (BECAUSE_YOU_WATCHED_PREFIX, media_type)
        cached = main_cache.get(cache_key)
        if cached is not None:
            start = (page_no - 1) * page_limit
            page_items = cached[start:start + page_limit]
            total_pages = max(1, (len(cached) + page_limit - 1) // page_limit)
            logger('VibeStream I Cant Decide', 'cache hit %s page=%s returning %s items (total %s)' % (media_type, page_no, len(page_items), len(cached)))
            return page_items, total_pages

        recently_watched = get_recently_watched(media_type, short_list=1)
        if not recently_watched:
            logger('VibeStream I Cant Decide', '%s no recently_watched -> fallback' % media_type)
            return self._get_fallback_recommendations(media_type, page_no, page_limit)

        # Get unique seeds (by tmdb_id for movies, by show tmdb_id for tv)
        seen = set()
        seeds = []
        
        # Pre-fetch watched status to exclude items the user has already seen
        # watched_items is a list of dicts or just dicts depending on type.
        # get_watched_items returns a list of items.
        try:
            watched_list = get_watched_items(media_type, 1) # page_no 1, but we want all. 
            # get_watched_items implementation in watched_status.py fetches ALL items if page_no is irrelevant or it returns everything.
            # Looking at watched_status.py: get_watched_items(media_type, page_no) returns results.
            # Movie: [v for k,v in watched_info_movie().items()] -> returns list of dicts {'media_id': ...}
            # TV: active_tvshows_information('watched') -> returns list of dicts.
            watched_ids = set()
            for i in watched_list:
                 mid = i.get('media_id') or (i.get('media_ids') or {}).get('tmdb')
                 if mid: watched_ids.add(str(mid))
        except Exception:
            watched_ids = set()

        for item in recently_watched[:BECAUSE_YOU_WATCHED_SEEDS * 2]:  # Overfetch in case of dupes
            tmdb_id = item.get('media_id') or (item.get('media_ids') or {}).get('tmdb')
            if not tmdb_id or tmdb_id in seen:
                continue
            seen.add(tmdb_id)
            title = item.get('title', '') or 'Unknown'
            if media_type == 'tvshow':
                try:
                    meta = tvshow_meta('tmdb_id', tmdb_id, self.tmdb_key, self.mpaa_region, get_datetime())
                    title = meta.get('title', 'Unknown')
                except Exception:
                    title = 'Unknown'
            if len(seeds) >= BECAUSE_YOU_WATCHED_SEEDS:
                break
            seeds.append((tmdb_id, title))

        if not seeds:
            logger('VibeStream I Cant Decide', '%s recently_watched had %s items but 0 valid seeds -> fallback' % (media_type, len(recently_watched)))
            return self._get_fallback_recommendations(media_type, page_no, page_limit)

        seed_titles = [t for _, t in seeds]
        logger('VibeStream I Cant Decide', '%s seeds from recently_watched: %s' % (media_type, ' | '.join(seed_titles)))

        rec_func = tmdb_movies_recommendations if media_type == 'movie' else tmdb_tv_recommendations
        merged = []
        seen_ids = set()
        for seed_tmdb_id, seed_title in seeds:
            try:
                data = rec_func(seed_tmdb_id, 1)
                results = data.get('results', [])[:BECAUSE_YOU_WATCHED_PER_SEED]
                added = 0
                for r in results:
                    rid = r.get('id')
                    if rid and rid not in seen_ids and str(rid) not in watched_ids:
                        seen_ids.add(rid)
                        merged.append({'tmdb_id': rid, 'because_you_watched': seed_title})
                        added += 1
                logger('VibeStream I Cant Decide', 'seed "%s" (tmdb=%s) -> %s recs added (total merged=%s)' % (seed_title, seed_tmdb_id, added, len(merged)))
            except Exception as e:
                logger('VibeStream I Cant Decide', 'seed "%s" tmdb=%s failed: %s' % (seed_title, seed_tmdb_id, str(e)))

        if not merged:
             logger('VibeStream I Cant Decide', 'Merged list empty after processing seeds -> fallback')
             return self._get_fallback_recommendations(media_type, page_no, page_limit)

        main_cache.set(cache_key, merged, expiration=BECAUSE_YOU_WATCHED_HOURS)
        start = (page_no - 1) * page_limit
        page_items = merged[start:start + page_limit]
        total_pages = max(1, (len(merged) + page_limit - 1) // page_limit)
        logger('VibeStream I Cant Decide', '%s built %s items page=%s showing %s' % (media_type, len(merged), page_no, len(page_items)))
        return page_items, total_pages

    def _get_fallback_recommendations(self, media_type, page_no, page_limit):
        """
        Fallback logic when no watch history is available.
        Uses generic Popular/Trending items.
        """
        logger('VibeStream I Cant Decide', 'Using fallback recommendations for %s' % media_type)
        fallback_func = tmdb_movies_popular if media_type == 'movie' else tmdb_tv_popular
        try:
            data = fallback_func(1)
            if not data or not isinstance(data, dict) or 'results' not in data: return [], 1
            results = data.get('results', [])
            fallback_items = [{'tmdb_id': r['id'], 'because_you_watched': 'Global Popularity'} for r in results]
            
            # We don't cache fallbacks under the main key so that if the user watches something, 
            # the next load will try to generate real recs again.
            start = (page_no - 1) * page_limit
            page_items = fallback_items[start:start + page_limit]
            total_pages = max(1, (len(fallback_items) + page_limit - 1) // page_limit)
            return page_items, total_pages
        except Exception as e:
            logger('VibeStream I Cant Decide', 'Fallback failed: %s' % str(e))
            return [], 1

recommendations_manager = RecommendationsManager()
