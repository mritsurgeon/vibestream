# -*- coding: utf-8 -*-
from modules.watched_status import get_recently_watched
from modules.metadata import movie_meta, tvshow_meta
from modules.settings import tmdb_api_key, mpaa_region
from modules.utils import get_datetime
from apis.tmdb_api import tmdb_api_key as get_tmdb_key

class RecommendationsManager:
    def __init__(self):
        self.tmdb_key = get_tmdb_key()
        self.mpaa_region = mpaa_region()

    def get_discovery_params(self, media_type):
        """
        Analyzes recent history and returns a dict of TMDb discovery parameters.
        """
        recently_watched = get_recently_watched(media_type, short_list=1) # Get top 20
        if not recently_watched:
            return None

        genre_counts = {}
        for item in recently_watched[:10]: # Analyze top 10 for speed
            tmdb_id = item.get('media_id') or item.get('media_ids', {}).get('tmdb')
            if not tmdb_id: continue
            
            try:
                if media_type == 'movie':
                    meta = movie_meta('tmdb_id', tmdb_id, self.tmdb_key, self.mpaa_region, get_datetime())
                else:
                    meta = tvshow_meta('tmdb_id', tmdb_id, self.tmdb_key, self.mpaa_region, get_datetime())
                
                genres = meta.get('genre_ids', [])
                for g_id in genres:
                    genre_counts[g_id] = genre_counts.get(g_id, 0) + 1
            except:
                continue

        if not genre_counts:
            return None

        # Sort genres by frequency
        sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
        top_genres = [str(g[0]) for g in sorted_genres[:2]] # Take top 2 genres
        
        # Build discovery query string
        # Example: with_genres=28,12&sort_by=popularity.desc
        query = "with_genres=%s&sort_by=popularity.desc" % ",".join(top_genres)
        
        return query

recommendations_manager = RecommendationsManager()
