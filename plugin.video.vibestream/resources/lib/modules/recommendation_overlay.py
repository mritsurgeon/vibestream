# -*- coding: utf-8 -*-
"""
Composite recommendation caption and rating onto poster/thumbnail images.
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

def get_poster_with_caption(poster_url, caption, rating=None):
    """
    Return a composite image path (poster + caption bar + rating) or original URL on failure.
    :param poster_url: Source image URL (e.g. TMDB poster)
    :param caption: Text to display (e.g. "Because you watched The Matrix")
    :param rating: Rating to display (e.g. 7.5), optional
    :return: special:// path to cached composite, or poster_url if compositing fails
    """
    if not poster_url or not poster_url.startswith('http'):
        return poster_url or ''
    
    # Check for PIL availability
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return poster_url

    try:
        from modules.kodi_utils import addon_profile, translatePath, addon_info
        import requests
        from io import BytesIO
    except ImportError:
        return poster_url

    # Cache directory
    cache_dir = translatePath(addon_info('profile')) + 'rec_overlay_cache/'
    # Include caption and rating in hash
    hash_str = str(poster_url) + str(caption) + str(rating) + 'v3' # v3 for new visual style
    cache_key = hashlib.md5(hash_str.encode()).hexdigest()
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
    
    # --- Overlay Configuration ---
    
    # Bottom Bar for Caption
    bar_h = max(int(h * 0.15), 60)
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Draw bottom dark bar
    draw.rectangle([(0, h - bar_h), (w, h)], fill=(0, 0, 0, 220))

    # --- Font Selection ---
    font = None
    rating_font = None
    caption_font_size = max(16, min(int(bar_h * 0.35), 40))
    
    # Large, readable rating font size
    rating_font_size = max(40, min(int(h * 0.12), 110))
    
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        '/system/fonts/DroidSans-Bold.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
        '/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf', # Linux common
    ]
    if sys.platform == 'win32':
        font_paths = [
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'impact.ttf'), # Impact is great for numbers
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'arialbd.ttf'),
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'calibrib.ttf'),
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'segmdl2.ttf'), # Segoe UI
        ] + font_paths
    elif sys.platform == 'darwin':
        font_paths = [
            '/System/Library/Fonts/Supplemental/Arial Black.ttf', # Thickest font
            '/Library/Fonts/Arial Black.ttf',
            '/System/Library/Fonts/Supplemental/DIN Alternate Bold.ttf',
            '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
            '/Library/Fonts/Arial Bold.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
        ] + font_paths
        
    found_font = None
    for path in font_paths:
        try:
            if os.path.exists(path):
                found_font = path
                break
        except Exception:
            pass
            
    if found_font:
        try:
            font = ImageFont.truetype(found_font, caption_font_size)
            rating_font = ImageFont.truetype(found_font, rating_font_size)
        except Exception: pass
        
    if font is None:
        try:
            font = ImageFont.load_default()
            rating_font = ImageFont.load_default()
        except Exception: pass

    # --- Caption Rendering (Bottom Center) ---
    text_color = (255, 255, 255)
    
    lines = []
    if "watched " in caption:
        parts = caption.split("watched ", 1)
        lines.append(parts[0] + "watched")
        lines.append(parts[1])
    else:
        lines.append(caption)

    total_text_height = len(lines) * caption_font_size * 1.2
    start_y = h - bar_h + (bar_h - total_text_height) // 2
    
    current_y = start_y
    for line in lines:
        try:
            bbox = draw.textbbox((0, 0), line, font=font) if font else (0, 0, len(line) * 8, 16)
            tw = bbox[2] - bbox[0]
        except (AttributeError, TypeError):
            try:
                tw, th = draw.textsize(line, font=font) if font else (len(line) * 8, 16)
            except Exception:
                tw = len(line) * 8
        
        tx = (w - tw) // 2
        if tx < 5: tx = 5
            
        draw.text((tx, current_y), line, fill=text_color, font=font)
        current_y += caption_font_size * 1.2

    # --- Rating Rendering (Top Right with Star) ---
    if rating and rating not in (0, '0', 0.0, '0.0', None, ''):
        try:
            rating_val = float(rating)
            rating_text = "%.1f" % rating_val
        except:
            rating_text = str(rating)

        # Star Dimensions
        star_radius = int(rating_font_size * 0.35) # Star slightly smaller than text height
        star_diameter = star_radius * 2
        
        # Text Dimensions
        try:
            bbox = draw.textbbox((0, 0), rating_text, font=rating_font) if rating_font else (0, 0, len(rating_text) * 12, 24)
            rw = bbox[2] - bbox[0]
            rh = bbox[3] - bbox[1]
            # Offset fix for some fonts
            text_y_offset = bbox[1]
        except:
            rw, rh = len(rating_text) * 12, 24
            text_y_offset = 0

        padding = int(h * 0.02) # Dynamic padding based on image height
        if padding < 8: padding = 8
        
        gap = int(padding * 0.8) # Gap between star and text
        
        content_width = star_diameter + gap + rw
        content_height = max(star_diameter, rh)
        
        box_width = content_width + (padding * 2)
        box_height = content_height + (padding * 1.5)

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
        # Vertically center text
        text_y = ry + (box_height - rh) // 2 - text_y_offset
        
        draw.text((text_x, text_y), rating_text, font=rating_font, fill=(255, 255, 255))

    # --- Final Composite ---
    img_rgba = img.convert('RGBA')
    img = Image.alpha_composite(img_rgba, overlay).convert('RGB')

    try:
        img.save(cache_path, 'JPEG', quality=90)
    except Exception:
        return poster_url

    return cache_path
