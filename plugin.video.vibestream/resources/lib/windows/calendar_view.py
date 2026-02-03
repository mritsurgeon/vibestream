# -*- coding: utf-8 -*-
"""
Calendar View Window for VibeStream
Displays Trakt calendar data in a visual calendar-style layout
"""
from datetime import datetime, timedelta
from windows.base_window import BaseDialog, open_window
from modules import kodi_utils
from caches.settings_cache import get_setting
from modules.utils import adjust_premiered_date, make_day, get_datetime, jsondate_to_datetime

logger = kodi_utils.logger
set_property, clear_property = kodi_utils.set_property, kodi_utils.clear_property

# Control IDs - must match XML
DAY_LIST_ID = 3000
EPISODE_LIST_ID = 3001

# Day name mappings
DAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
DAY_NAMES_SHORT = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
MONTH_NAMES = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class CalendarView(BaseDialog):
    """
    Visual calendar view showing episodes organized by day.
    Each day shows as a block with episodes listed underneath.
    """
    
    def __init__(self, *args, **kwargs):
        BaseDialog.__init__(self, *args)
        self.calendar_data = kwargs.get('calendar_data', [])
        self.selected_day_index = 0
        self.current_date = datetime.now().date()
        self.handle_key = True
        self.days = []
        self.day_episodes = {}
        self.choice = None
        
    def onInit(self):
        """Initialize the calendar view"""
        set_property('vibestream.window_loaded', 'true')
        self.build_calendar_data()
        self.populate_days()
        if self.days:
            self.populate_episodes(0)
        
    def build_calendar_data(self):
        """Group episodes by date and build day list"""
        # Get calendar settings
        prev_days = int(get_setting('vibestream.trakt.calendar_previous_days', '7'))
        future_days = int(get_setting('vibestream.trakt.calendar_future_days', '7'))
        
        # Build date range
        start_date = self.current_date - timedelta(days=prev_days)
        end_date = self.current_date + timedelta(days=future_days)
        
        # Initialize all days in range
        current = start_date
        while current <= end_date:
            self.days.append(current)
            self.day_episodes[current] = []
            current += timedelta(days=1)
        
        # Group episodes by air date
        for ep in self.calendar_data:
            try:
                air_date_str = ep.get('first_aired', '') or ''
                if not air_date_str:
                    continue
                # Parse the air date (handle ISO 8601 e.g. '2024-01-15T00:00:00.000Z')
                date_part = air_date_str[:10] if len(air_date_str) >= 10 else air_date_str
                air_date = jsondate_to_datetime(date_part, '%Y-%m-%d').date()
                if air_date in self.day_episodes:
                    self.day_episodes[air_date].append(ep)
            except Exception:
                pass
    
    def populate_days(self):
        """Populate the day selector list"""
        items = []
        for i, day in enumerate(self.days):
            item = self.make_listitem()
            
            # Format day display
            day_name = DAY_NAMES_SHORT[day.weekday()]
            month_name = MONTH_NAMES[day.month]
            day_num = day.day
            
            # Check if today
            is_today = day == self.current_date
            is_past = day < self.current_date
            
            # Create display labels (no [B] in property - XML adds it in focusedlayout; use darker teal for contrast)
            if is_today:
                line1 = '[COLOR FF008B72]TODAY[/COLOR]'  # Darker teal for better visibility
                line2 = '%s %d' % (month_name, day_num)
            else:
                line1 = day_name
                line2 = '%s %d' % (month_name, day_num)
            
            # Episode count
            ep_count = len(self.day_episodes[day])
            if ep_count > 0:
                line3 = '[COLOR FFCCCCCC]%d episode%s[/COLOR]' % (ep_count, 's' if ep_count != 1 else '')
            else:
                line3 = '[COLOR FF666666]No episodes[/COLOR]'
            
            item.setLabel(line1)  # Required for list display
            item.setProperty('line1', line1)
            item.setProperty('line2', line2)
            item.setProperty('line3', line3)
            item.setProperty('is_today', 'true' if is_today else 'false')
            item.setProperty('is_past', 'true' if is_past else 'false')
            item.setProperty('day_index', str(i))
            items.append(item)
        
        try:
            self.add_items(DAY_LIST_ID, items)
            # Select today by default
            today_index = next((i for i, d in enumerate(self.days) if d == self.current_date), 0)
            self.select_item(DAY_LIST_ID, today_index)
        except Exception as e:
            logger('CalendarView.populate_days error', str(e))
    
    def populate_episodes(self, day_index):
        """Populate episodes for the selected day"""
        try:
            self.reset_window(EPISODE_LIST_ID)
        except Exception:
            pass
        
        if day_index >= len(self.days):
            return
        
        day = self.days[day_index]
        episodes = self.day_episodes.get(day, [])
        
        if not episodes:
            # Show "No episodes" placeholder
            item = self.make_listitem()
            item.setLabel('No episodes airing')
            item.setProperty('line1', 'No episodes airing')
            item.setProperty('line2', 'Check back later')
            item.setProperty('is_placeholder', 'true')
            try:
                self.add_items(EPISODE_LIST_ID, [item])
            except Exception:
                pass
            return
        
        items = []
        for ep in episodes:
            item = self.make_listitem()
            
            # Extract episode info
            title = ep.get('sort_title', 'Unknown Show')
            season = ep.get('season', 0)
            episode_num = ep.get('episode', 0)
            
            # Format display
            line1 = title.split(' s')[0] if ' s' in title else title  # Get show title only
            line2 = 'S%02dE%02d' % (season, episode_num)
            
            item.setLabel(line1)  # Required for list display
            item.setProperty('line1', line1)
            item.setProperty('line2', line2)
            item.setProperty('season', str(season))
            item.setProperty('episode', str(episode_num))
            
            # Store episode data for selection
            tmdb_id = ep.get('media_ids', {}).get('tmdb', '')
            item.setProperty('tmdb_id', str(tmdb_id) if tmdb_id else '')
            item.setProperty('is_placeholder', 'false')
            
            items.append(item)
        
        try:
            self.add_items(EPISODE_LIST_ID, items)
        except Exception as e:
            logger('CalendarView.populate_episodes error', str(e))
    
    def run(self):
        """Run the dialog"""
        self.doModal()
        self.clear_modals()
        clear_property('vibestream.window_loaded')
        return self.choice
    
    def onAction(self, action):
        """Handle user actions"""
        action_id = action.getId()
        
        if action_id in self.closing_actions:
            self.close()
            return
        
        # Handle navigation between day list and episode list
        focus_id = self.getFocusId()
        
        if action_id in self.selection_actions:
            if focus_id == EPISODE_LIST_ID:
                self.select_episode()
        
        elif action_id == self.up_action or action_id == self.down_action:
            if focus_id == DAY_LIST_ID:
                # Day selection changed, update episodes
                try:
                    pos = self.get_position(DAY_LIST_ID)
                    if pos != self.selected_day_index:
                        self.selected_day_index = pos
                        self.populate_episodes(pos)
                except Exception:
                    pass
    
    def onClick(self, control_id):
        """Handle click events"""
        if control_id == DAY_LIST_ID:
            try:
                pos = self.get_position(DAY_LIST_ID)
                if pos != self.selected_day_index:
                    self.selected_day_index = pos
                    self.populate_episodes(pos)
                    self.setFocusId(EPISODE_LIST_ID)
            except Exception:
                pass
        elif control_id == EPISODE_LIST_ID:
            self.select_episode()
    
    def select_episode(self):
        """Handle episode selection for playback"""
        try:
            item = self.get_listitem(EPISODE_LIST_ID)
            if item is None:
                return
            if item.getProperty('is_placeholder') == 'true':
                return
            
            tmdb_id = item.getProperty('tmdb_id')
            season = item.getProperty('season')
            episode = item.getProperty('episode')
            
            if tmdb_id:
                self.choice = {
                    'mode': 'playback.media',
                    'media_type': 'episode',
                    'tmdb_id': tmdb_id,
                    'season': season,
                    'episode': episode
                }
                self.close()
        except Exception as e:
            logger('CalendarView.select_episode error', str(e))


def open_calendar_view(calendar_data):
    """Open the calendar view window"""
    return open_window(
        ('windows.calendar_view', 'CalendarView'),
        'calendar_view.xml',
        calendar_data=calendar_data
    )
