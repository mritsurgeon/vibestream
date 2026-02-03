# -*- coding: utf-8 -*-
"""
Composite viewer rating onto poster/thumbnail images.
Returns cached composite path or original URL on failure.
"""
import hashlib
import os

def get_poster_with_rating(poster_url, rating):
	"""
	Return a composite image path (poster + rating badge) or original URL on failure.
	:param poster_url: Source image URL (e.g. TMDB poster)
	:param rating: Numeric rating (float/int) or None; displayed as "7.5" or "N/A"
	:return: special:// path to cached composite, or poster_url if compositing fails
	"""
	if not poster_url or not poster_url.startswith('http'):
		return poster_url or ''
	try:
		from PIL import Image, ImageDraw, ImageFont
	except ImportError:
		return poster_url
	try:
		from modules.kodi_utils import addon_profile, translatePath
		from modules.kodi_utils import addon_info
		import requests
	except ImportError:
		return poster_url
	cache_dir = translatePath(addon_info('profile')) + 'rating_cache/'
	cache_key = hashlib.md5((str(poster_url) + str(rating)).encode()).hexdigest()
	cache_path = os.path.join(cache_dir, '%s.jpg' % cache_key)
	if os.path.exists(cache_path):
		return cache_path
	try:
		os.makedirs(cache_dir, exist_ok=True)
	except OSError:
		return poster_url
	try:
		r = requests.get(poster_url, timeout=10)
		r.raise_for_status()
		img = Image.open(__import__('io').BytesIO(r.content))
	except Exception:
		return poster_url
	if img.mode != 'RGB':
		img = img.convert('RGB')
	w, h = img.size
	bar_h = max(int(h * 0.12), 24)
	overlay = Image.new('RGBA', (w, bar_h), (0, 0, 0, 180))
	draw = ImageDraw.Draw(overlay)
	font = None
	font_size = max(12, min(int(bar_h * 0.6), 28))
	for path in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
	             '/system/fonts/DroidSans-Bold.ttf',
	             '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'):
		try:
			if os.path.exists(path):
				font = ImageFont.truetype(path, font_size)
				break
		except Exception:
			pass
	if font is None:
		try:
			font = ImageFont.load_default()
		except Exception:
			pass
	rating_str = '%.1f' % float(rating) if rating not in (None, 0, 0.0, '', 'N/A') else 'N/A'
	rating_str = '[%s]' % rating_str
	try:
		bbox = draw.textbbox((0, 0), rating_str, font=font) if font else (0, 0, len(rating_str) * 8, 16)
		tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
	except (AttributeError, TypeError):
		try:
			tw, th = draw.textsize(rating_str, font=font) if font else (len(rating_str) * 8, 16)
		except Exception:
			tw, th = len(rating_str) * 8, 16
	tx = (w - tw) // 2
	ty = (bar_h - th) // 2
	draw.text((tx, ty), rating_str, fill=(255, 255, 255), font=font)
	img_rgba = img.convert('RGBA')
	img_rgba.paste(overlay, (0, h - bar_h), overlay)
	img_out = img_rgba.convert('RGB')
	try:
		img_out.save(cache_path, 'JPEG', quality=90)
	except Exception:
		return poster_url
	return cache_path
