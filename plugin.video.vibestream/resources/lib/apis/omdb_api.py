# -*- coding: utf-8 -*-
from xml.dom.minidom import parseString as mdParse
from caches.meta_cache import meta_cache
from modules.metadata import movie_expiry, tvshow_expiry
from modules.utils import get_datetime, get_current_timestamp
from modules.kodi_utils import make_session
# from modules.kodi_utils import logger

url = 'http://www.omdbapi.com/?apikey=%s&i=%s&tomatoes=True&r=xml'
omdb_json_url = 'http://www.omdbapi.com/?apikey=%s&i=%s'
OMDB_API_KEY = 'c7938f09'
timeout = 20.0
session = make_session('http://www.omdbapi.com/')
metascore_icon, imdb_icon, tmdb_icon = 'metacritic.png', 'imdb.png', 'tmdb.png'

class OMDbAPI:
	def fetch_info(self, meta, api_key):
		imdb_id = meta.get('imdb_id')
		if not imdb_id or not api_key: return {}
		self.api_key = api_key
		data = self.process_result(imdb_id, meta)
		return data

	def process_result(self, imdb_id, meta):
		data = {}
		self.result = self.get_result(imdb_id)
		if not self.result: return {}
		self.result_get = self.result.get
		metascore_rating, tomatometer_rating, tomatousermeter_rating = self.process_rating('metascore'), self.process_rating('tomatoMeter'), self.process_rating('tomatoUserMeter')
		imdb_rating, tomato_image = self.process_rating('imdbRating'), self.process_rating('tomatoImage')
		if tomato_image: tomatometer_icon = 'rtcertified.png' if tomato_image == 'certified' else 'rtfresh.png' if tomato_image == 'fresh' else 'rtrotten.png'
		elif tomatometer_rating: tomatometer_icon = 'rtfresh.png' if int(tomatometer_rating) > 59 else 'rtrotten.png'
		else: tomatometer_icon = 'rtrotten.png'
		if tomatousermeter_rating: tomatousermeter_icon = 'popcorn.png' if int(tomatousermeter_rating) > 59 else 'popcorn_spilt.png'
		else: tomatousermeter_icon = 'popcorn_spilt.png'
		data = {
				'metascore': {'rating': '%s%%' %  metascore_rating, 'icon': metascore_icon},
				'tomatometer': {'rating': '%s%%' % tomatometer_rating, 'icon': tomatometer_icon},
				'tomatousermeter': {'rating': '%s%%' % tomatousermeter_rating, 'icon': tomatousermeter_icon},
				'imdb': {'rating': imdb_rating, 'icon': imdb_icon},
				'tmdb': {'rating': '', 'icon': tmdb_icon},
				}
		media_type = meta.get('mediatype')
		expiry_function = movie_expiry if media_type == 'movie' else tvshow_expiry
		meta['extra_ratings'] = data
		meta_cache.set(media_type, 'tmdb_id', meta, expiry_function(get_datetime(), meta), get_current_timestamp())
		return data

	def get_result(self, imdb_id):
		try:
			result = session.get(url % (self.api_key, imdb_id), timeout=timeout).text
			response_test = dict(mdParse(result).getElementsByTagName('root')[0].attributes.items())
			if not response_test.get('response', 'False') == 'True': return None
			return dict(mdParse(result).getElementsByTagName('movie')[0].attributes.items())
		except Exception: return None

	def process_rating(self, rating_name):
		return self.result_get(rating_name, '').replace('N/A', '')

fetch_ratings_info = OMDbAPI().fetch_info


def _omdb_get(imdb_id):
	try:
		resp = session.get(omdb_json_url % (OMDB_API_KEY, imdb_id), timeout=timeout)
		data = resp.json()
		if data.get('Response') != 'True': return None
		return data
	except Exception: return None

def _parse_omdb_date(date_str):
	if not date_str or date_str == 'N/A': return ''
	try:
		from datetime import datetime
		return datetime.strptime(date_str, '%d %b %Y').strftime('%Y-%m-%d')
	except Exception: return ''

def _parse_omdb_runtime(runtime_str):
	try: return int(runtime_str.replace(' min', '').strip()) * 60
	except Exception: return 0

def _parse_omdb_list(val):
	if not val or val == 'N/A': return []
	return [i.strip() for i in val.split(',') if i.strip() and i.strip() != 'N/A']

def omdb_movie_metadata(imdb_id):
	data = _omdb_get(imdb_id)
	if not data: return None
	title = data.get('Title', '') or ''
	year_raw = data.get('Year', '') or ''
	year = year_raw[:4]
	premiered = _parse_omdb_date(data.get('Released', ''))
	genre = _parse_omdb_list(data.get('Genre', ''))
	director = _parse_omdb_list(data.get('Director', ''))
	writer = _parse_omdb_list(data.get('Writer', ''))
	cast = [{'name': a, 'role': '', 'thumbnail': ''} for a in _parse_omdb_list(data.get('Actors', ''))]
	country = _parse_omdb_list(data.get('Country', ''))
	rating = (data.get('imdbRating', '') or '').replace('N/A', '')
	votes = (data.get('imdbVotes', '') or '').replace('N/A', '').replace(',', '')
	poster = data.get('Poster', '') or ''
	if poster == 'N/A': poster = ''
	mpaa = (data.get('Rated', '') or '').replace('N/A', '')
	plot = (data.get('Plot', '') or '').replace('N/A', '')
	duration = _parse_omdb_runtime(data.get('Runtime', ''))
	lang_list = _parse_omdb_list(data.get('Language', ''))
	spoken_language = lang_list[0] if lang_list else ''
	rootname = '%s (%s)' % (title, year)
	extra_info = {'status': 'N/A', 'budget': '$0', 'revenue': '$0', 'homepage': 'N/A', 'collection_name': None, 'collection_id': None}
	return {
		'tmdb_id': '0000000', 'imdb_id': imdb_id, 'imdbnumber': imdb_id, 'tvdb_id': 'None',
		'title': title, 'original_title': title, 'english_title': title,
		'year': year, 'premiered': premiered, 'plot': plot, 'tagline': '',
		'rating': rating, 'votes': votes, 'mpaa': mpaa,
		'poster': poster, 'fanart': '', 'clearlogo': '', 'landscape': '',
		'genre': genre, 'cast': cast, 'director': director, 'writer': writer,
		'duration': duration, 'country': country, 'country_codes': [],
		'studio': (), 'spoken_language': spoken_language,
		'alternative_titles': [], 'keywords': None, 'trailer': '', 'all_trailers': [],
		'rootname': rootname, 'extra_info': extra_info, 'mediatype': 'movie',
	}

def omdb_tvshow_metadata(imdb_id):
	data = _omdb_get(imdb_id)
	if not data: return None
	title = data.get('Title', '') or ''
	year_raw = data.get('Year', '') or ''
	year = year_raw[:4]
	if year_raw and (year_raw.endswith('-') or year_raw.endswith('\u2013')): status = 'Returning Series'
	elif '-' in year_raw or '\u2013' in year_raw: status = 'Ended'
	else: status = 'Returning Series'
	premiered = _parse_omdb_date(data.get('Released', '')) or (year + '-01-01' if year else '')
	genre = _parse_omdb_list(data.get('Genre', ''))
	director = _parse_omdb_list(data.get('Director', ''))
	writer = _parse_omdb_list(data.get('Writer', ''))
	cast = [{'name': a, 'role': '', 'thumbnail': ''} for a in _parse_omdb_list(data.get('Actors', ''))]
	country = _parse_omdb_list(data.get('Country', ''))
	rating = (data.get('imdbRating', '') or '').replace('N/A', '')
	votes = (data.get('imdbVotes', '') or '').replace('N/A', '').replace(',', '')
	poster = data.get('Poster', '') or ''
	if poster == 'N/A': poster = ''
	mpaa = (data.get('Rated', '') or '').replace('N/A', '')
	plot = (data.get('Plot', '') or '').replace('N/A', '')
	duration = _parse_omdb_runtime(data.get('Runtime', ''))
	lang_list = _parse_omdb_list(data.get('Language', ''))
	spoken_language = lang_list[0] if lang_list else ''
	try: total_seasons = int(data.get('totalSeasons', '0') or '0')
	except Exception: total_seasons = 0
	rootname = '%s (%s)' % (title, year)
	extra_info = {'status': status, 'type': 'Scripted', 'homepage': 'N/A', 'created_by': 'N/A', 'next_episode_to_air': None, 'last_episode_to_air': None}
	return {
		'tmdb_id': '0000000', 'tvdb_id': 'None', 'imdb_id': imdb_id, 'imdbnumber': imdb_id,
		'title': title, 'original_title': title, 'english_title': title, 'tvshowtitle': title,
		'year': year, 'premiered': premiered, 'plot': plot, 'tagline': '',
		'rating': rating, 'votes': votes, 'mpaa': mpaa, 'status': status,
		'poster': poster, 'fanart': '', 'clearlogo': '', 'landscape': '',
		'genre': genre, 'cast': cast, 'director': director, 'writer': writer,
		'duration': duration, 'country': country, 'country_codes': [],
		'studio': (), 'spoken_language': spoken_language,
		'alternative_titles': [], 'keywords': None, 'trailer': '', 'all_trailers': [],
		'rootname': rootname, 'season_data': [], 'extra_info': extra_info,
		'total_seasons': total_seasons, 'total_aired_eps': 0, 'mediatype': 'tvshow',
	}
