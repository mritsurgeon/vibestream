# -*- coding: utf-8 -*-
from modules.kodi_utils import make_session

FANART_API_KEY = 'c07adc549d38d520cd10bef7e32ac405'
movie_url = 'https://webservice.fanart.tv/v3/movies/%s?api_key=%s'
tv_url = 'https://webservice.fanart.tv/v3/tv/%s?api_key=%s'
timeout = 20.0
session = make_session('https://webservice.fanart.tv/')

def _best_url(items, lang='en'):
	if not items: return ''
	for item in items:
		if item.get('lang', '') == lang: return item.get('url', '')
	return items[0].get('url', '')

def fanart_movie_artwork(tmdb_id):
	try:
		if not tmdb_id or str(tmdb_id) in ('0000000', ''): return {}
		resp = session.get(movie_url % (tmdb_id, FANART_API_KEY), timeout=timeout)
		if resp.status_code != 200: return {}
		data = resp.json()
		return {
			'fanart': _best_url(data.get('moviebackground', [])),
			'clearlogo': _best_url(data.get('hdmovieclearart', [])),
			'landscape': _best_url(data.get('moviethumb', [])),
			'poster': _best_url(data.get('movieposter', [])),
		}
	except Exception: return {}

def fanart_tvshow_artwork(tvdb_id):
	try:
		if not tvdb_id or str(tvdb_id) in ('None', '0000000', '0', ''): return {}
		resp = session.get(tv_url % (tvdb_id, FANART_API_KEY), timeout=timeout)
		if resp.status_code != 200: return {}
		data = resp.json()
		return {
			'fanart': _best_url(data.get('showbackground', [])),
			'clearlogo': _best_url(data.get('hdtvlogo', [])),
			'landscape': _best_url(data.get('tvthumb', [])),
			'poster': _best_url(data.get('tvposter', [])),
		}
	except Exception: return {}
