# -*- coding: utf-8 -*-
from caches.settings_cache import get_setting

# Presets
PRESET_4K = '4k_ultra'
PRESET_1080P_BALANCED = '1080p_balanced'
PRESET_720P_EFFICIENT = '720p_efficient'
PRESET_LOW = 'low'

PRESETS = {
    PRESET_4K: {'max_resolution': '4K', 'max_size_gb': 25.0, 'rank': 4, 'prefer_smallest': False},
    PRESET_1080P_BALANCED: {'max_resolution': '1080p', 'max_size_gb': 15.0, 'rank': 3, 'prefer_smallest': True},
    PRESET_720P_EFFICIENT: {'max_resolution': '720p', 'max_size_gb': 5.0, 'rank': 2, 'prefer_smallest': True},
    PRESET_LOW: {'max_resolution': '720p', 'max_size_gb': 2.0, 'rank': 1, 'prefer_smallest': True}
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
        Filter sources (used e.g. for retry/fallback). Handles size in GB or MB.
        Strictly enforces max_resolution and max_size_gb.
        """
        filtered = []
        max_rank = RESOLUTION_RANKS.get(self.get_max_resolution(), 3)
        max_size_mb = self.get_max_size_gb() * 1024
        
        for source in sources:
            quality = source.get('quality', 'SD')
            rank = RESOLUTION_RANKS.get(quality, 1)
            
            # 1. Resolution Filtering
            if rank > max_rank:
                continue

            # 2. Size Filtering
            size_raw = source.get('size', 0) or 0
            try:
                size_val = float(size_raw)
                # Improved Logic: 
                # If size_val is < 0.01, it's likely 0 or invalid.
                # If size_val is < 100, it's almost certainly GB (even a 100GB 4K file is rare).
                # If size_val is >= 100, it's likely MB (a 100GB file is huge, but a 100MB file is possible).
                # This handles the 500MB case (no scaling) and 1.2GB case (scaling to 1228MB).
                if 0 < size_val < 100:
                    size_mb = size_val * 1024
                else:
                    size_mb = size_val
                
                if size_mb > max_size_mb:
                    continue
            except (TypeError, ValueError):
                pass
            
            filtered.append(source)
        return filtered

    def stamp_sources(self, sources):
        """
        Full scrape, then stamp only: mark sources that exceed the selected quality preset
        with a note (e.g. "High usage" / "Outside selected quality") so user can still
        see and select them. Does not remove any sources.
        """
        max_rank = RESOLUTION_RANKS.get(self.get_max_resolution(), 3)
        max_size_mb = self.get_max_size_gb() * 1024
        stamp = 'Outside selected quality'
        for source in sources:
            source.pop('quality_preset_note', None)
            quality = source.get('quality', 'SD')
            rank = RESOLUTION_RANKS.get(quality, 1)
            over_res = rank > max_rank
            size_mb = 0
            try:
                size_raw = source.get('size', 0) or 0
                size_val = float(size_raw)
                size_mb = (size_val * 1024) if size_val and size_val < 1000 else size_val
            except (TypeError, ValueError):
                pass
            over_size = size_mb > max_size_mb
            if over_res or over_size:
                source['quality_preset_note'] = stamp

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
