# -*- coding: utf-8 -*-
"""
Composite recommendation caption and rating onto poster/thumbnail images.
Returns cached composite path or original URL on failure.
"""
import hashlib
import os
import sys

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
    hash_str = str(poster_url) + str(caption) + str(rating) + 'v2'
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
    rating_font_size = max(20, min(int(h * 0.08), 60))
    
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        '/system/fonts/DroidSans-Bold.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
        '/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf', # Linux common
    ]
    if sys.platform == 'win32':
        font_paths = [
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'arialbd.ttf'),
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'calibrib.ttf'),
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'segmdl2.ttf'), # Segoe UI
        ] + font_paths
    elif sys.platform == 'darwin':
        font_paths = [
            '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
            '/Library/Fonts/Arial Bold.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
            '/System/Library/Fonts/Supplemental/DIN Alternate Bold.ttf', # Nice modern font on macOS
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

    # --- Text Helper ---
    def draw_text_with_outline(draw_obj, xy, text, font, text_color=(255, 255, 255), outline_color=(0, 0, 0), outline_width=2):
        x, y = xy
        # Draw outline
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if dx != 0 or dy != 0:
                    draw_obj.text((x + dx, y + dy), text, font=font, fill=outline_color)
        # Draw main text
        draw_obj.text((x, y), text, font=font, fill=text_color)

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
            
        # Draw without outline in the bar since bar is dark
        draw.text((tx, current_y), line, fill=text_color, font=font)
        current_y += caption_font_size * 1.2

    # --- Rating Rendering (Top Right) ---
    if rating and rating not in (0, '0', 0.0, '0.0', None, ''):
        try:
            rating_val = float(rating)
            rating_text = "%.1f" % rating_val
        except:
            rating_text = str(rating)

        # Star character if font supports it, otherwise just number
        # Many basic fonts don't support unicode star cleanly, so let's stick to text or simple shape
        # Let's draw a yellow star shape manually or just a box
        
        # Calculate size
        try:
            bbox = draw.textbbox((0, 0), rating_text, font=rating_font) if rating_font else (0, 0, len(rating_text) * 12, 24)
            rw = bbox[2] - bbox[0]
            rh = bbox[3] - bbox[1]
        except:
            rw, rh = len(rating_text) * 12, 24

        padding = 10
        rx = w - rw - padding - 10 # 10px from right
        ry = padding # 10px from top
        
        # Background box for rating (Semi-transparent Black or Dark Yellow/Gold)
        # Let's do a rounded box look (simulated with rectangle)
        box_coords = [rx - 5, ry - 5, rx + rw + 5, ry + rh + 10]
        draw.rectangle(box_coords, fill=(0, 0, 0, 180)) # Dark background
        
        # Accent line (Gold/Yellow)
        draw.rectangle([rx - 5, ry - 5, rx - 2, ry + rh + 10], fill=(255, 215, 0, 255))

        # Draw Rating Text with outline
        draw_text_with_outline(draw, (rx, ry), rating_text, rating_font, text_color=(255, 255, 255), outline_width=2)

    # --- Final Composite ---
    img_rgba = img.convert('RGBA')
    img = Image.alpha_composite(img_rgba, overlay).convert('RGB')

    try:
        img.save(cache_path, 'JPEG', quality=85)
    except Exception:
        return poster_url

    return cache_path
