# -*- coding: utf-8 -*-
from caches.base_cache import BaseCache

class SourceCache(BaseCache):
	def __init__(self):
		BaseCache.__init__(self, 'source_cache.db', 'sources')

source_cache = SourceCache()

def get_cached_sources(media_type, tmdb_id, season='', episode=''):
    key = _get_key(media_type, tmdb_id, season, episode)
    return source_cache.get(key)

def set_cached_sources(media_type, tmdb_id, results, season='', episode=''):
    key = _get_key(media_type, tmdb_id, season, episode)
    # Default TTL 1 hour (60 minutes)
    source_cache.set(key, results, expiration=60)

def _get_key(media_type, tmdb_id, season, episode):
    if media_type == 'movie':
        return 'movie_%s' % tmdb_id
    else:
        return 'episode_%s_%s_%s' % (tmdb_id, season, episode)
