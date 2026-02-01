# -*- coding: utf-8 -*-

class ScraperInterface:
    """
    Abstract Base Class for Scraping Adapters.
    Defines the standard interface for searching and resolving media.
    """
    
    def search(self, query_info):
        """
        Search for sources.
        
        :param query_info: Dict containing query parameters:
            - media_type: 'movie' or 'episode'
            - tmdb_id: str
            - title: str
            - year: str
            - season: int (optional)
            - episode: int (optional)
            - aliases: list (optional)
        :return: List of source dictionaries.
        """
        raise NotImplementedError("Search method must be implemented")

    def resolve(self, source):
        """
        Resolve a source to a playable URL.
        
        :param source: Source dictionary returned by search()
        :return: Resolved URL (str) or None
        """
        raise NotImplementedError("Resolve method must be implemented")

    def supports(self, feature):
        """
        Check if the scraper supports a feature.
        
        :param feature: Feature name (e.g., 'cached_torrents', 'hosters')
        :return: bool
        """
        return False

    def health_check(self):
        """
        Check if the scraper provider is healthy/available.
        :return: (bool, message)
        """
        return (True, "OK")
