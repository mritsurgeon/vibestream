# -*- coding: utf-8 -*-
from threading import Thread
import time
from modules import kodi_utils

xbmc = kodi_utils.xbmc
logger = kodi_utils.logger
sleep = kodi_utils.sleep

class PlaybackWatchdog(xbmc.Player):
    def __init__(self, observer=None):
        super(PlaybackWatchdog, self).__init__()
        self.observer = observer
        self._playback_active = False
        self._monitoring = False
        self.start_time = 0

    def onPlayBackStarted(self):
        self._playback_active = True
        self.start_time = time.time()
        self.start_monitoring()

    def onPlayBackStopped(self):
        self._playback_active = False
        self._monitoring = False

    def onPlayBackEnded(self):
        self._playback_active = False
        self._monitoring = False

    def start_monitoring(self):
        if self._monitoring: return
        self._monitoring = True
        Thread(target=self._monitor_loop).start()

    def _monitor_loop(self):
        logger('Watchdog', 'Monitoring Started')
        buffer_count = 0
        while self._monitoring and self._playback_active:
            if self.isPlaying():
                try:
                    if kodi_utils.xbmc.getCondVisibility("Player.Caching"):
                        buffer_count += 1
                    else:
                        buffer_count = 0
                    if buffer_count > 15:
                        logger('Watchdog', 'Excessive Buffering Detected')
                        if self.observer and hasattr(self.observer, 'on_playback_failed'):
                            self.observer.on_playback_failed(reason='buffering')
                        break
                except: pass
            sleep(1000)
        logger('Watchdog', 'Monitoring Stopped')
