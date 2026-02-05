# -*- coding: utf-8 -*-
"""
Composite viewer rating onto poster/thumbnail images.
Returns cached composite path or original URL on failure.
"""
import hashlib
import os
import sys
import math

def draw_star(draw, center, radius, fill_color, outline_color):
    cx, cy = center
    points = []
    # 5 points
    for i in range(10):
        angle = i * 36 * math.pi / 180 - math.pi / 2
        r = radius if i % 2 == 0 else radius * 0.4
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        points.append((x, y))
    draw.polygon(points, fill=fill_color, outline=outline_color)

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
        from io import BytesIO
    except ImportError:
        return poster_url

    cache_dir = translatePath(addon_info('profile')) + 'rating_cache/'
    # Use v3 hash for new style
    cache_key = hashlib.md5((str(poster_url) + str(rating) + 'v3').encode()).hexdigest()
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
        img = Image.open(BytesIO(r.content))
    except Exception:
        return poster_url
    if img.mode != 'RGB':
        img = img.convert('RGB')

    w, h = img.size
    
    # Create transparent overlay layer
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font = None
    # Large, readable rating font size (same scale as recommendation overlay)
    font_size = max(40, min(int(h * 0.12), 110))
    
    # Platform-specific font paths: prefer bold/standout fonts (Impact, Arial Black)
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        '/system/fonts/DroidSans-Bold.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
    ]
    if sys.platform == 'win32':
        font_paths = [
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'impact.ttf'),
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'ariblk.ttf'),
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'arialbd.ttf'),
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'Arial Bold.ttf'),
        ] + font_paths
    elif sys.platform == 'darwin':
        font_paths = [
            '/System/Library/Fonts/Supplemental/Arial Black.ttf',
            '/Library/Fonts/Arial Black.ttf',
            '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
            '/Library/Fonts/Arial Bold.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
        ] + font_paths
        
    for path in font_paths:
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
    
    # --- Calculate Badge Dimensions ---
    
    # Star Dimensions
    star_radius = int(font_size * 0.35) 
    star_diameter = star_radius * 2
    
    # Text Dimensions
    try:
        bbox = draw.textbbox((0, 0), rating_str, font=font) if font else (0, 0, len(rating_str) * 12, 24)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        text_y_offset = bbox[1]
    except (AttributeError, TypeError):
        try:
            tw, th = draw.textsize(rating_str, font=font) if font else (len(rating_str) * 12, 16)
            text_y_offset = 0
        except Exception:
            tw, th = len(rating_str) * 12, 16
            text_y_offset = 0

    padding = int(h * 0.02)
    if padding < 8: padding = 8
    
    gap = int(padding * 0.8)
    
    content_width = star_diameter + gap + tw
    content_height = max(star_diameter, th)
    
    box_width = content_width + (padding * 2)
    box_height = content_height + (padding * 1.5)

    # Position: Top Right
    rx = w - box_width - padding
    ry = padding
    
    # Draw Rounded Box (Dark Background)
    box_color = (0, 0, 0, 200)
    draw.rectangle([rx, ry, rx + box_width, ry + box_height], fill=box_color, outline=None)
    
    # Draw Gold Star
    star_center_x = rx + padding + star_radius
    star_center_y = ry + (box_height // 2)
    draw_star(draw, (star_center_x, star_center_y), star_radius, (255, 215, 0), (218, 165, 32))

    # Draw Rating Text
    text_x = rx + padding + star_diameter + gap
    text_y = ry + (box_height - th) // 2 - text_y_offset
    
    draw.text((text_x, text_y), rating_str, fill=(255, 255, 255), font=font)

    # --- Final Composite ---
    img_rgba = img.convert('RGBA')
    img_rgba.paste(overlay, (0, 0), overlay) # Paste overlay handling alpha
    img_out = img_rgba.convert('RGB')
    
    try:
        img_out.save(cache_path, 'JPEG', quality=90)
    except Exception:
        return poster_url
    return cache_path
