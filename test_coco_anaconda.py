#!/usr/bin/env python3
"""
Test CocoScrapers for movie "Anaconda" (1997).
Run from vibestream/ with: python3 test_coco_anaconda.py
Requires script.module.cocoscrapers on PYTHONPATH (e.g. KODI_ADDONS_PATH) to get real results.
Mocks Kodi modules so the addon code can load outside Kodi.
"""
import sys
import os

# Mock Kodi modules so we can import addon code outside Kodi
class MockKodi:
    def __getattr__(self, name):
        return lambda *a, **k: None
sys.modules['xbmc'] = MockKodi()
sys.modules['xbmcgui'] = MockKodi()
sys.modules['xbmcplugin'] = MockKodi()
sys.modules['xbmcvfs'] = MockKodi()
class MockAddon:
    def getAddonInfo(self, i):
        return '1.0.0' if i == 'version' else ''
sys.modules['xbmcaddon'] = type(sys)('xbmcaddon')
sys.modules['xbmcaddon'].Addon = lambda addon_id: MockAddon()

# Add addon lib so we can import modules
addon_lib = os.path.join(os.path.dirname(__file__), 'plugin.video.fenlight', 'resources', 'lib')
if addon_lib not in sys.path:
    sys.path.insert(0, addon_lib)

# Optional: add Kodi addons path so script.module.cocoscrapers can be found
kodi_addons = os.environ.get('KODI_ADDONS_PATH', '')
if kodi_addons:
    sys.path.insert(0, kodi_addons)


def main():
    # Query for Anaconda (1997) - same shape as _coco_query_info()
    query = {
        'title': 'Anaconda',
        'year': '1997',
        'imdb_id': 'tt0118615',
        'tmdb_id': '8835',
        'media_type': 'movie',
        'season': None,
        'episode': None,
        'ep_name': None,
        'aliases': [],
    }
    print('Query:', query)
    print()

    # 1) Health check and search
    try:
        from modules.scraping_adapters.cocoscrapers import CocoScrapersAdapter
        adapter = CocoScrapersAdapter()
        ok, msg = adapter.health_check()
        print('CocoScrapers health_check:', ok, msg)
        if not ok:
            print('CocoScrapers not available (script.module.cocoscrapers not found).')
            print('To test with real results, set KODI_ADDONS_PATH to your Kodi addons folder.')
            print()
            # Dry run: fake raw result to test normalizer
            raw = [{'name': 'Anaconda.1997.1080p.WEBRip.x264', 'url': 'magnet:?xt=...', 'quality': '1080p', 'size': 2.5, 'source': 'TorrentProvider'}]
            print('Dry run: using 1 fake raw result to test normalizer.')
        else:
            raw = adapter.search(query)
        print('Raw results count:', len(raw) if raw else 0)
        if raw and isinstance(raw[0], dict):
            print('First raw result keys:', list(raw[0].keys())[:15])
            print('First raw sample:', {k: (str(v)[:60] + '...' if isinstance(v, str) and len(str(v)) > 60 else v) for k, v in list(raw[0].items())[:8]})
        print()
    except Exception as e:
        print('Adapter error:', e)
        import traceback
        traceback.print_exc()
        return

    # 2) Normalize (same logic as Sources._normalize_coco_sources, no Kodi deps)
    def _simple_quality(name_or_url):
        if not name_or_url:
            return 'SD', ''
        n = (name_or_url or '').lower()
        if '2160' in n or '4k' in n:
            return '4K', ''
        if '1080' in n:
            return '1080p', ''
        if '720' in n:
            return '720p', ''
        return 'SD', ''

    normalized = []
    for item in (raw or []):
        try:
            if not isinstance(item, dict):
                continue
            display_name = item.get('display_name') or item.get('name') or item.get('title') or ''
            name_or_url = display_name or item.get('url') or ''
            if not name_or_url and not item.get('hash'):
                continue
            quality = item.get('quality')
            extra_info = item.get('extraInfo', '')
            if quality is None or extra_info == '':
                q, _ = _simple_quality(name_or_url or item.get('url'))
                if quality is None:
                    quality = q
                if extra_info == '':
                    extra_info = 'N/A'
            try:
                size_val = float(item.get('size', 0) or 0)
            except (TypeError, ValueError):
                size_val = 0
            size_label = '%.2f GB' % size_val if size_val else 'N/A'
            out = dict(item)
            out.update({
                'name': display_name or name_or_url,
                'display_name': display_name or name_or_url,
                'quality': quality or 'SD',
                'size': size_val,
                'size_label': size_label,
                'extraInfo': extra_info,
                'scrape_provider': 'cocoscrapers',
                'source': item.get('source') or item.get('provider') or 'CocoScrapers',
                'debrid': item.get('debrid', 'Real-Debrid'),
                'cache_provider': item.get('cache_provider', ''),
            })
            normalized.append(out)
        except Exception:
            continue
    print('Normalized count:', len(normalized))
    if normalized:
        s = normalized[0]
        print('First normalized:', {k: s[k] for k in ('display_name', 'quality', 'size', 'scrape_provider', 'source') if k in s})

    print()
    print('Done. CocoScrapers test for Anaconda completed.')


if __name__ == '__main__':
    main()
