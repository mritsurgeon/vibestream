# -*- coding: utf-8 -*-
from modules import kodi_utils
from modules.scraping_adapters.interface import ScraperInterface

class CocoScrapersAdapter(ScraperInterface):
    def __init__(self):
        self.module_name = 'script.module.cocoscrapers'
        self._provider_class = None

    def _get_provider(self):
        if self._provider_class: return self._provider_class
        try:
            from cocoscrapers import sources
            self._provider_class = sources.sources()
        except ImportError:
            kodi_utils.logger('CocoScrapers', 'Failed to import cocoscrapers module')
        except Exception as e:
            kodi_utils.logger('CocoScrapers', 'Error importing sources: %s' % str(e))
        return self._provider_class

    _REQUIRED_KEYS = {'url', 'quality'}

    def _validate_source(self, item):
        if not isinstance(item, dict): return False
        if not self._REQUIRED_KEYS.issubset(item.keys()): return False
        if not isinstance(item.get('url'), str) or not item['url']: return False
        return True

    def search(self, query_info):
        provider = self._get_provider()
        if not provider: return []
        try:
            if hasattr(provider, 'getAll'):
                raw = provider.getAll(query_info) or []
            elif hasattr(provider, 'getSources'):
                raw = provider.getSources(query_info) or []
            else:
                return []
            valid = [s for s in raw if self._validate_source(s)]
            dropped = len(raw) - len(valid)
            if dropped:
                kodi_utils.logger('CocoScrapers', 'Dropped %d malformed results' % dropped)
            return valid
        except Exception as e:
            kodi_utils.logger('CocoScrapers', 'Search failed: %s' % str(e))
            return []

    def supports(self, feature):
        return True # Supports everything generally
    
    def health_check(self):
        if self._get_provider(): return (True, "OK")
        return (False, "Module not found")
