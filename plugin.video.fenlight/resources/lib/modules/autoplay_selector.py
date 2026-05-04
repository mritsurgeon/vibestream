# -*- coding: utf-8 -*-
import re
from caches.settings_cache import get_setting
from modules.health_manager import health_manager

# Language tokens found in release filenames, mapped to ISO-639-1 codes
_LANG_TOKENS = {
    'french': 'fr', 'francais': 'fr', 'truefrench': 'fr',
    'vff': 'fr', 'vfq': 'fr', 'vf': 'fr', 'vostfr': 'fr',
    'english': 'en', 'eng': 'en',
    'spanish': 'es', 'espanol': 'es', 'esp': 'es', 'spa': 'es',
    'german': 'de', 'deutsch': 'de', 'ger': 'de', 'deu': 'de',
    'italian': 'it', 'italiano': 'it', 'ita': 'it',
    'portuguese': 'pt', 'portugues': 'pt', 'por': 'pt',
    'dutch': 'nl', 'nederlands': 'nl', 'nld': 'nl',
    'multi': 'multi', 'multilang': 'multi', 'dual': 'multi',
}

_SPLIT_RE = re.compile(r'[\s.\-_\[\]()+]')


def detect_language(name):
    """Return ISO lang code detected from release name, or None if unknown."""
    for token in _SPLIT_RE.split((name or '').lower()):
        if token in _LANG_TOKENS:
            return _LANG_TOKENS[token]
    return None


def _language_score(source_name, preferred_lang):
    """3=exact, 2=multi, 1=unknown/neutral, 0=wrong language."""
    if preferred_lang == 'any':
        return 3
    detected = detect_language(source_name)
    if detected is None:
        return 1
    if detected == 'multi':
        return 2
    return 3 if detected == preferred_lang else 0


def rank_sources(results, media_type):
    """
    Re-order results using: language preference > quality tier > provider health.
    Sources with the wrong language are not dropped — they stay as last-resort
    fallbacks at the end of the list.
    """
    preferred_lang = get_setting('fenlight.autoplay_language', 'en')
    quality_order_str = get_setting('fenlight.autoplay_quality_%s' % media_type, 'SD, 720p, 1080p, 4K')
    quality_tiers = [q.strip() for q in quality_order_str.split(',')]

    def _score(source):
        name = source.get('name', '') or source.get('display_name', '')
        lang = _language_score(name, preferred_lang)
        quality = source.get('quality', 'SD')
        q_tier = quality_tiers.index(quality) if quality in quality_tiers else -1
        health = health_manager.get_health_score(source.get('scrape_provider', ''))
        return (lang, q_tier, health)

    return sorted(results, key=_score, reverse=True)
