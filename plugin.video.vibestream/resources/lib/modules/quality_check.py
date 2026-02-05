# -*- coding: utf-8 -*-
from modules.utils import get_datetime, jsondate_to_datetime, subtract_dates, make_thread_list_multi_arg
from modules.settings import tmdb_api_key, mpaa_region
from modules.metadata import movie_meta

# Rule: >= 8 days since release is considered "No CAM" (likely WEB/HD available or will be soon)
MIN_DAYS_MATURITY = 8

def filter_movies_no_cams(tmdb_ids):
    """
    Filters a list of TMDB IDs, returning only those that pass the quality/maturity check.
    Uses threading to fetch metadata efficiently.
    """
    eligible_ids = []
    
    def _check(tmdb_id):
        try:
            # We need metadata to check the date.
            # We use the existing cache if available, or fetch it.
            # Passing current_time=None forces a fresh timestamp check but uses cache if valid.
            meta = movie_meta('tmdb_id', tmdb_id, tmdb_api_key(), mpaa_region(), get_datetime())
            if not meta: return

            premiered = meta.get('premiered')
            if not premiered: return # No date, assume unsafe or not out

            # Calculate days since release
            release_date = jsondate_to_datetime(premiered, '%Y-%m-%d', remove_time=True)
            if not release_date: return
            
            current_date = get_datetime()
            
            # subtract_dates returns days (float/int)
            days_diff = subtract_dates(current_date, release_date)
            
            if days_diff >= MIN_DAYS_MATURITY:
                eligible_ids.append(tmdb_id)
        except Exception:
            pass

    # Thread the checks
    threads = list(make_thread_list(_check, tmdb_ids))
    [i.join() for i in threads]
    
    return eligible_ids
