# -*- coding: utf-8 -*-
from caches.settings_cache import get_setting

# Presets
PRESET_4K = '4k_ultra'
PRESET_1080P_BALANCED = '1080p_balanced'
PRESET_720P_EFFICIENT = '720p_efficient'
PRESET_LOW = 'low'

PRESETS = {
    PRESET_4K: {'max_resolution': '4K', 'max_size_gb': 25.0, 'rank': 4},
    PRESET_1080P_BALANCED: {'max_resolution': '1080p', 'max_size_gb': 8.0, 'rank': 3},
    PRESET_720P_EFFICIENT: {'max_resolution': '720p', 'max_size_gb': 5.0, 'rank': 2},
    PRESET_LOW: {'max_resolution': '720p', 'max_size_gb': 2.0, 'rank': 1}
}

RESOLUTION_RANKS = {'4K': 4, '2160p': 4, '1080p': 3, '720p': 2, '480p': 1, 'SD': 1, 'SCR': 0, 'CAM': 0}

class QualityManager:
    def __init__(self):
        self.active_preset_id = get_setting('vibestream.quality.preset', PRESET_1080P_BALANCED)
        self.preset = PRESETS.get(self.active_preset_id, PRESETS[PRESET_1080P_BALANCED])

    def get_max_resolution(self):
        return self.preset['max_resolution']

    def get_max_size_gb(self):
        return self.preset['max_size_gb']
    
    def filter_sources(self, sources):
        """
        Filter sources based on the active preset.
        """
        filtered = []
        max_rank = RESOLUTION_RANKS.get(self.get_max_resolution(), 3)
        max_size_mb = self.get_max_size_gb() * 1024
        
        for source in sources:
            # Check Resolution
            quality = source.get('quality', 'SD')
            rank = RESOLUTION_RANKS.get(quality, 1)
            
            if rank > max_rank:
                continue
                
            # Check Size (if available)
            size_mb = source.get('size', 0)
            if size_mb > max_size_mb:
                continue
                
            filtered.append(source)
            
        return filtered

    def step_down(self):
        """
        Step down to the next lower preset for fallback.
        Returns True if stepped down, False if already at lowest.
        """
        current_rank = self.preset['rank']
        if current_rank <= 1: return False
        
        # Find next lower rank
        next_preset_id = None
        for pid, data in PRESETS.items():
            if data['rank'] == current_rank - 1:
                next_preset_id = pid
                break
        
        if next_preset_id:
            self.active_preset_id = next_preset_id
            self.preset = PRESETS[next_preset_id]
            return True
        return False
