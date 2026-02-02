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

    def search(self, query_info):
        """
        Delegates search to CocoScrapers. Works with script.module.cocoscrapers when installed.
        Tries getAll(query_info) then getSources(query_info) for API compatibility.
        """
        provider = self._get_provider()
        if not provider: return []
        
        try:
            if hasattr(provider, 'getAll'):
                return provider.getAll(query_info) or []
            if hasattr(provider, 'getSources'):
                return provider.getSources(query_info) or []
            return []
        except Exception as e:
            kodi_utils.logger('CocoScrapers', 'Search failed: %s' % str(e))
            return []

    def supports(self, feature):
        return True # Supports everything generally
    
    def health_check(self):
        if self._get_provider(): return (True, "OK")
        return (False, "Module not found")
