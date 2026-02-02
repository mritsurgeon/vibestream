# -*- coding: utf-8 -*-
menu_settings = '\
\n                    <item id="10">\
\n                        <property name="setting_label">General</property>\
\n                    </item>\
\n                    <item id="20">\
\n                        <property name="setting_label">Features</property>\
\n                    </item>\
\n                    <item id="30">\
\n                        <property name="setting_label">Content</property>\
\n                    </item>\
\n                    <item id="40">\
\n                        <property name="setting_label">Single Episode Lists</property>\
\n                    </item>\
\n                    <item id="50">\
\n                        <property name="setting_label">Accounts</property>\
\n                    </item>\
\n                    <item id="60">\
\n                        <property name="setting_label">Results</property>\
\n                    </item>\
\n                    <item id="70">\
\n                        <property name="setting_label">Playback</property>\
\n                    </item>'

content_settings = '\
\n        <!-- GENERAL 10-->\
\n            <!-- General -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">General</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                   </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">Autostart VibeStream When Kodi Starts</property>\
                        <property name="setting_type">boolean</property>\
                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.auto_start_vibestream)]</property>\
                        <property name="setting_description">Enable this and VibeStream will autostart after running its services upon Kodi start</property>\
                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=auto_start_vibestream)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">Assign Addon Background Image</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.default_addon_fanart)]</property>\
\n                        <property name="setting_description">Choose any custom background you would like to use within VibeStream</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_path&amp;setting_id=default_addon_fanart)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <visible>!String.EndsWith(Window(10000).Property(vibestream.default_addon_fanart),vibestream_fanart.png)</visible>\
\n                        <property name="setting_label">    - Restore Default Background Image</property>\
                        <property name="setting_type">action</property>\
                        <property name="setting_value">...</property>\
                        <property name="setting_description">Restore default VibeStream background</property>\
                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.restore_setting_default&amp;setting_id=default_addon_fanart)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">Limit Concurrent Threads</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.limit_concurrent_threads)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will limit the threads enacted simultaneously. Best to leave this disabled unless you are having issues with your device not supporting high numbers of concurrent threads in python</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=limit_concurrent_threads)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.limit_concurrent_threads),true)</visible>\
\n                        <property name="setting_label">    - Maximum Active Threads</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.max_threads)]</property>\
\n                        <property name="setting_description">Choose the maximum active concurrent threads VibeStream will be limited to</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=max_threads)</onclick>\
\n                    </item>\
\n            <!-- Watched Indicators -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">Watched Indicators</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.trakt.user),empty_setting)</visible>\
\n                        <property name="setting_label">Watched Status Provider</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.watched_indicators_name)]</property>\
\n                        <property name="setting_description">Choose the provider that keeps track of the Movies and Episodes you have watched within VibeStream. Options are the built in method of VibeStream or your Trakt account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=watched_indicators)</onclick>\
\n                    </item>\
\n            <!-- Trakt Cache -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">Trakt Cache</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.trakt.user),empty_setting)</visible>\
\n                        <property name="setting_label">Resync Interval (mins)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.trakt.sync_interval)]</property>\
\n                        <property name="setting_description">Choose how often VibeStream polls your Trakt service for any changes</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=trakt.sync_interval)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.trakt.user),empty_setting)</visible>\
\n                        <property name="setting_label">Refresh Widgets After Trakt Sync</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.trakt.refresh_widgets)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will refresh widgets after performing a Trakt Sync if there were any changes</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=trakt.refresh_widgets)</onclick>\
\n                    </item>\
\n            <!-- UTC Time Offset -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">UTC Time Offset</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">UTC (+/-)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.datetime.offset)]</property>\
\n                        <property name="setting_description">Choose the correct UTC offset based on your location</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=datetime.offset)</onclick>\
\n                    </item>\
\n            <!-- Downloads -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">Downloads</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">Movies Directory</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.movie_download_directory)]</property>\
\n                        <property name="setting_description">Choose your download location for Movies</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_path&amp;setting_id=movie_download_directory)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">TV Shows Directory</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.tvshow_download_directory)]</property>\
\n                        <property name="setting_description">Choose your download location for TV Shows</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_path&amp;setting_id=tvshow_download_directory)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">Premium Files Directory</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.premium_download_directory)]</property>\
\n                        <property name="setting_description">Choose your download location for Premium files. Includes downloads from debrid service caches or Easynews</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_path&amp;setting_id=premium_download_directory)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(10)</visible>\
\n                        <property name="setting_label">Image Files Directory</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.image_download_directory)]</property>\
\n                        <property name="setting_description">Choose your download location for Images</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_path&amp;setting_id=image_download_directory)</onclick>\
\n                    </item>\
\n        <!-- FEATURES 20-->\
\n            <!-- Extras -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(20)</visible>\
\n                        <property name="setting_label">Extras</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(20)</visible>\
\n                        <property name="setting_label">Enable Content for Extras Lists</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Choose what content is included within the Extras window</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=extras_lists_choice)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(20)</visible>\
\n                        <property name="setting_label">Set Actions for Extras Buttons</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Choose the function and order of the buttons in the Extras window. You can set separate button functions for Movies and TV Shows</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=extras_buttons_choice)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(20)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.omdb_api),empty_setting)</visible>\
\n                        <property name="setting_label">Enable Extra Ratings</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.extras.enable_extra_ratings)]</property>\
\n                        <property name="setting_description">Enable this and the Extras menu will show ratings from more services than just TMDb. Must have a valid OMDb API assigned in the Accounts settings for this to show</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=extras.enable_extra_ratings)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(20)</visible>\
\n                        <property name="setting_label">Enable Scrollbars for Extras Lists</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.extras.enable_scrollbars)]</property>\
\n                        <property name="setting_description">Choose this and the individual lists within the Extras window will each utilize a scrollbar when needed</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=extras.enable_scrollbars)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(20)</visible>\
\n                        <property name="setting_label">Extras View Mode</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.extras.view_mode_name)]</property>\
\n                        <property name="setting_description">Choose the mode for the Extras window. "Simple" shows only the most important info, while "Advanced" shows all available metadata</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=extras.view_mode)</onclick>\
\n                    </item>\
\n            <!-- Special Open Actions -->\
\n                  <item>\
\n                        <visible>Container(2000).HasFocus(20)</visible>\
\n                        <property name="setting_label">Special Open Actions</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(20)</visible>\
\n                        <property name="setting_label">Movies</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.media_open_action_movie_name)]</property>\
\n                        <property name="setting_description">Choose the Open Action when a Movie is selected in VibeStream. Choices Are None, Open Extras, Open Movie Set, Both. "Both" will open the Movie Set if available or open Extras</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=media_open_action_movie)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(20)</visible>\
\n                        <property name="setting_label">TV Shows</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.media_open_action_tvshow_name)]</property>\
\n                        <property name="setting_description">Choose the Open Action when a TV Show is selected in VibeStream. Choices Are None or Open Extras</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=media_open_action_tvshow)</onclick>\
\n                    </item>\
\n        <!-- CONTENT 30 -->\
\n            <!-- Sorting - Personal Lists -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Sorting - Personal Lists</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">In Progress</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.sort.progress_name)]</property>\
\n                        <property name="setting_description">Choose the sort order for your In Progress media</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=sort.progress)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Watched</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.sort.watched_name)]</property>\
\n                        <property name="setting_description">Choose the sort order for your Watched media</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=sort.watched)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.trakt.user),empty_setting)</visible>\
\n                        <property name="setting_label">Collection</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.sort.collection_name)]</property>\
\n                        <property name="setting_description">Choose the sort order for your Trakt Collection media</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=sort.collection)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.trakt.user),empty_setting)</visible>\
\n                        <property name="setting_label">Watchlist</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.sort.watchlist_name)]</property>\
\n                        <property name="setting_description">Choose the sort order for your Trakt Watchlist media</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=sort.watchlist)</onclick>\
\n                    </item>\
\n            <!-- Widgets -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Widgets</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Refresh Widgets on Timer</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.widget_refresh_timer_name)]</property>\
\n                        <property name="setting_description">Choose whether VibeStream refreshes widgets based on a set timer. You should set a value here if you are using random widgets from VibeStream, and wish for their contents to update between Kodi starts</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=widget_refresh_timer_choice)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.widget_refresh_timer),0)</visible>\
\n                        <property name="setting_label">    - Show Notification after Refresh</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.widget_refresh_notification)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will show a notification whenever widgets are refreshed by the timer</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=widget_refresh_notification)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Hide Watched Items in Widgets</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.widget_hide_watched)]</property>\
\n                        <property name="setting_description">Enable this and watched items will be hidden in VibeStream widgets</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=widget_hide_watched)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Hide Next Page Item in Widgets</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.widget_hide_next_page)]</property>\
\n                        <property name="setting_description">Enable this and the "Next Page" item will be hidden in VibeStream widgets</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=widget_hide_next_page)</onclick>\
\n                    </item>\
\n            <!-- General -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">General</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Paginate Lists When Available</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.paginate.lists_name)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will attempt to paginate lists when possible. This is mainly applicable to personal lists</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=paginate.lists)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.paginate.lists),1) | String.IsEqual(Window(10000).Property(vibestream.paginate.lists),3)</visible>\
\n                        <property name="setting_label">    - Addon Item Limit</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.paginate.limit_addon)]</property>\
\n                        <property name="setting_description">Choose the limit of pagination when within VibeStream</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=paginate.limit_addon)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.paginate.lists),2) | String.IsEqual(Window(10000).Property(vibestream.paginate.lists),3)</visible>\
\n                        <property name="setting_label">    - Widgets Item Limit</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.paginate.limit_widgets)]</property>\
\n                        <property name="setting_description">Choose the limit of pagination for VibeStream widgets</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=paginate.limit_widgets)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Service used for Because You Watched</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.recommend_service_name)]</property>\
\n                        <property name="setting_description">Choose which service provides recommendations for the Because You Watched menus. Options are Recommended (TMDb) or More Like This (IMDb)</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=recommend_service)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Seeds used for Because You Watched Random</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.recommend_seed_name)]</property>\
\n                        <property name="setting_description">Choose how much previously watched media is used for recommendations for the Because You Watched Random menu.</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=recommend_seed)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Set MPAA Region</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.mpaa_region_display_name)]</property>\
\n                        <property name="setting_description">Choose the region from which the MPAA advisories will be displayed</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=mpaa_region_choice)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Watched (Still Airing) TV Shows Location</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.tv_progress_location_name)]</property>\
\n                        <property name="setting_description">Choose where fully watched, but still airing TV Shows are shown. Options are Watched, In Progress or Both</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=tv_progress_location)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Show Special Episodes When Available</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.show_specials)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will show TV Show Special Episodes</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=show_specials)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Flatten TV Show Seasons</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.default_all_episodes_name)]</property>\
\n                        <property name="setting_description">Choose the times when VibeStream will load all episodes of a TV Show when browsed into</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=default_all_episodes)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Include Unaired Media in Trakt Watchlists</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.show_unaired_watchlist)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will display any unaired media in your Trakt Movie/TV Show Watchlists. Disable this and any unaired Media will be hidden</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=show_unaired_watchlist)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Include Adult Results from Media Searches</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.meta_filter)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will attempt to filter out adult content from Movie, TV Show and People searches. Success is based purely on the accuracy of TMDbs database. Expect that some adult results may come through and plan accordingly</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=meta_filter)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <property name="setting_label">Control Viewtypes within Addon</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.use_viewtypes)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will control view types used within the addon. This can be disabled if the skin you are using has a helper that provides a "lock view" type function. If enabled, views can be set in Tools->Set Views within the addon</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=use_viewtypes)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.use_viewtypes),true)</visible>\
\n                        <property name="setting_label">    - Manually Enter Viewtype Values</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.manual_viewtypes)]</property>\
\n                        <property name="setting_description">Enable this to manually enter values for the viewtypes used. Only do this if you know the viewtype values for the skin you are using. Otherwise, use the "Set Views" menu in Tools</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=manual_viewtypes)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.use_viewtypes),true) + String.IsEqual(Window(10000).Property(vibestream.manual_viewtypes),true)</visible>\
\n                        <property name="setting_label">        - Set Menu View ID</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.view.main)]</property>\
\n                        <property name="setting_description">Enter the Viewtype ID for Menu Content</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=view.main&amp;min_value=1)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.use_viewtypes),true) + String.IsEqual(Window(10000).Property(vibestream.manual_viewtypes),true)</visible>\
\n                        <property name="setting_label">        - Set Movies View ID</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.view.movies)]</property>\
\n                        <property name="setting_description">Enter the Viewtype ID for Movies Content</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=view.movies&amp;min_value=1)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.use_viewtypes),true) + String.IsEqual(Window(10000).Property(vibestream.manual_viewtypes),true)</visible>\
\n                        <property name="setting_label">        - Set TV Shows View ID</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.view.tvshows)]</property>\
\n                        <property name="setting_description">Enter the Viewtype ID for TV Shows Content</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=view.tvshows&amp;min_value=1)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.use_viewtypes),true) + String.IsEqual(Window(10000).Property(vibestream.manual_viewtypes),true)</visible>\
\n                        <property name="setting_label">        - Set Seasons View ID</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.view.seasons)]</property>\
\n                        <property name="setting_description">Enter the Viewtype ID for Seasons Content</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=view.seasons&amp;min_value=1)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.use_viewtypes),true) + String.IsEqual(Window(10000).Property(vibestream.manual_viewtypes),true)</visible>\
\n                        <property name="setting_label">        - Set Episodes View ID</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.view.episodes)]</property>\
\n                        <property name="setting_description">Enter the Viewtype ID for Episodes Content</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=view.episodes&amp;min_value=1)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.use_viewtypes),true) + String.IsEqual(Window(10000).Property(vibestream.manual_viewtypes),true)</visible>\
\n                        <property name="setting_label">        - Set Episode Lists View ID</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.view.episodes_single)]</property>\
\n                        <property name="setting_description">Enter the Viewtype ID for Episode Lists Content</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=view.episodes_single&amp;min_value=1)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(30)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.use_viewtypes),true) + String.IsEqual(Window(10000).Property(vibestream.manual_viewtypes),true)</visible>\
\n                        <property name="setting_label">        - Set Premium Files View ID</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.view.premium)]</property>\
\n                        <property name="setting_description">Enter the Viewtype ID for Premium Files Content</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=view.premium&amp;min_value=1)</onclick>\
\n                    </item>\
\n        <!-- SINGLE EPISODE LISTS 40 -->\
\n            <!-- General -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">General</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Single Episode Display Format - Within Addon</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.single_ep_display_name)]</property>\
\n                        <property name="setting_description">Choose the display format VibeStream uses when naming single episodes within the addon. Applicable for lists like Next Episodes, In Progress Episodes etc</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=single_ep_display)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Single Episode Display Format - Widgets</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.single_ep_display_widget_name)]</property>\
\n                        <property name="setting_description">Choose the display format VibeStream uses when naming single episodes for widgets. Applicable for lists like Next Episodes, In Progress Episodes etc</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=single_ep_display_widget)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Provide Unwatched Episodes Info</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.single_ep_unwatched_episodes)]</property>\
\n                        <property name="setting_description">Enable this to share with Kodi the number of unwatched episodes for the TV Show of each episode in single episode lists</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=single_ep_unwatched_episodes)</onclick>\
\n                    </item>\
\n            <!-- Next Episodes -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Next Episodes</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Calculate Content Based On</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.nextep.method_name)]</property>\
\n                        <property name="setting_description">Choose the method used to determine the content of your Next Episodes list. Last Aired or Last Watched</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=nextep.method)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Sort Type</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.nextep.sort_type_name)]</property>\
\n                        <property name="setting_description">Choose the sort type of Next Episodes list. Recently Watched, Airdate or Title</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=nextep.sort_type)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Sort Order</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.nextep.sort_order_name)]</property>\
\n                        <property name="setting_description">Choose the sort direction of Next Episodes list. Ascending or Descending</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=nextep.sort_order)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Limit Used Watched History</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.nextep.limit_history)]</property>\
\n                        <property name="setting_description">Enable this to limit the amount of watched history used to determine Next Episodes</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=nextep.limit_history)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.nextep.limit_history),true)</visible>\
\n                        <property name="setting_label">    - Limit</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.nextep.limit)]</property>\
\n                        <property name="setting_description">A setting of "20" will limit the history used based on the previous 20 watched episodes. This means a 20 limit will not usually result in 20 items in your Next Episodes list, rather the previous 20 watched episodes will be used as history</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=nextep.limit)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Include Trakt Watchlist/VibeStream Favorites</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.nextep.include_unwatched_name)]</property>\
\n                        <property name="setting_description">Choose which lists are included within Next Episodes. You can include your Trakt Watchlist, your VibeStream Favorites, or both. They will show with a DARKGOLDENROD highlight</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=nextep.include_unwatched)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Include Airdate in Title</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.nextep.include_airdate)]</property>\
\n                        <property name="setting_description">Enable this to include the airdate at the beginning of the list item label</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=nextep.include_airdate)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Sort Airing Today to Top</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.nextep.airing_today)]</property>\
\n                        <property name="setting_description">Enable this to sort episodes airing today to the top of the Next Episodes list</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=nextep.airing_today)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Include Unaired Episodes When Within 7 Days</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.nextep.include_unaired)]</property>\
\n                        <property name="setting_description">Enable this to include unaired episodes within Next Episodes. They will show with a RED highlight and become visible within 7 days of their airdate</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=nextep.include_unaired)</onclick>\
\n                    </item>\
\n            <!-- Trakt Calendar -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Trakt Calendar</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Flatten TV Shows Airing on Same Day</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.trakt.flatten_episodes)]</property>\
\n                        <property name="setting_description">Enable this to limit to the first instance of a TV Show episode when that TV Show has multiple episodes airing on the same day</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=trakt.flatten_episodes)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Sort Order</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.trakt.calendar_sort_order_name)]</property>\
\n                        <property name="setting_description">Choose the sort direction of the Trakt Calendar list. Ascending or Descending</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=trakt.calendar_sort_order)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Show Previous Days</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.trakt.calendar_previous_days)]</property>\
\n                        <property name="setting_description">Choose how many previous days will be shown within the Trakt Calendar</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=trakt.calendar_previous_days)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(40)</visible>\
\n                        <property name="setting_label">Show Future Days</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.trakt.calendar_future_days)]</property>\
\n                        <property name="setting_description">Choose how many future days will be shown within the Trakt Calendar</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=trakt.calendar_future_days)</onclick>\
\n                    </item>\
\n        <!-- ACCOUNTS 50 -->\
\n            <!-- Trakt -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Trakt</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.trakt.user),empty_setting)</visible>\
\n                        <property name="setting_label">Authorize</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Authorize your Trakt account and use it within VibeStream</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=trakt.trakt_authenticate)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Revoke Authorization</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.trakt.user)]</property>\
\n                        <property name="setting_description">Revoke authorization of your Trakt account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=trakt.trakt_revoke_authentication)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Client ID Key</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.trakt.client)]</property>\
\n                        <property name="setting_description">Enter here your Trakt Client ID key</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_string&amp;setting_id=trakt.client)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.trakt.client),1038ef327e86e7f6d39d80d2eb5479bff66dd8394e813c5e0e387af0f84d89fb)</visible>\
\n                        <property name="setting_label">    - Restore Default Client ID Key</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Restore default Trakt Client ID Key</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.restore_setting_default&amp;setting_id=trakt.client)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Client Secret Key</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.trakt.secret)]</property>\
\n                        <property name="setting_description">Enter here your Trakt Client Secret key</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_string&amp;setting_id=trakt.secret)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.trakt.secret),8d27a92e1d17334dae4a0590083a4f26401cb8f721f477a79fd3f218f8534fd1)</visible>\
\n                        <property name="setting_label">    - Restore Default Client Secret Key</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Restore default Trakt Client Secret Key</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.restore_setting_default&amp;setting_id=trakt.secret)</onclick>\
\n                    </item>\
\n            <!-- TMDb -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">TMDB</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Read API Key</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.tmdb_api)]</property>\
\n                        <property name="setting_description">Enter your TMDb Read Access API key</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_string&amp;setting_id=tmdb_api)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.tmdb_api),b370b60447737762ca38457bd77579b3)</visible>\
\n                        <property name="setting_label">    - Restore Default TMDb API Key</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Restore default TMDb API Key</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.restore_setting_default&amp;setting_id=tmdb_api)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Test API Key...</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Test if your TMDb API is activated and working</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=tmdb_api_check_choice)</onclick>\
\n                    </item>\
\n            <!-- TMDb Lists -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">TMDB Lists</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                        <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.tmdb.access_token),empty_setting)</visible>\
\n                        <property name="setting_label">Authorize</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Authorize your TMDB account and use it within VibeStream</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=tmdb.authenticate)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.tmdb.access_token),empty_setting)</visible>\
\n                        <property name="setting_label">Revoke Authorization</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Revoke authorization of your TMDb account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=tmdb.deauth)</onclick>\
\n                    </item>\
\n            <!-- OMDb -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">OMDb</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">API Key</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.omdb_api)]</property>\
\n                        <property name="setting_description">Enter here your OMDb API key. This will allow you to utilize extra ratings information in the Extras window</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_string&amp;setting_id=omdb_api)</onclick>\
\n                    </item>\
\n            <!-- External Scrapers -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">External Scrapers</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Enable</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.provider.external)]</property>\
\n                        <property name="setting_description">Enable this to use external scrapers. No support is provided when you choose to use external scrapers within VibeStream</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=provider.external)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.external),true)</visible>\
\n                        <property name="setting_label">Choose External Scrapers Module</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.external_scraper.name)]</property>\
\n                        <property name="setting_description">Choose the external scraper module to use within VibeStream. No support is provided when you choose to use external scrapers within VibeStream</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=external_scraper_choice)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.external),true)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.external_scraper.name),empty_setting)</visible>\
\n                        <property name="setting_label">Open External Scraper Settings</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Open the External Scraper settings. The settings of the module chosen above will be opened</property>\
\n                        <onclick>back</onclick>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=open_external_scraper_settings)</onclick>\
\n                    </item>\
\n            <!-- Real Debrid -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Real Debrid</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.rd.token),empty_setting)</visible>\
\n                        <property name="setting_label">Authorize</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Authorize your Real Debrid account and use it within VibeStream</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=real_debrid.authenticate)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.rd.token),empty_setting)</visible>\
\n                        <property name="setting_label">Enable</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.rd.enabled)]</property>\
\n                        <property name="setting_description">Enable the use of your Real Debrid account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=rd.enabled)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.rd.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.rd.enabled),true)</visible>\
\n                        <property name="setting_label">Revoke Authorization</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.rd.account_id)]</property>\
\n                        <property name="setting_description">Revoke authorization of your Real Debrid account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=real_debrid.revoke_authentication)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.rd.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.rd.enabled),true)</visible>\
\n                        <property name="setting_label">Add Resolved Debrid Cache to Cloud</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.store_resolved_to_cloud.real-debrid_name)]</property>\
\n                        <property name="setting_description">Choose which resolved media is automatically added to your Real Debrid Cloud. All media or only show packs</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=store_resolved_to_cloud.real-debrid)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.rd.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.rd.enabled),true)</visible>\
\n                        <property name="setting_label">Search Cloud Storage</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.provider.rd_cloud)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will search your Real Debrid Cloud for media</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=provider.rd_cloud)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.rd.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.rd.enabled),true)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.rd_cloud),true)</visible>\
\n                        <property name="setting_label">    - Filter Results by Name</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.rd_cloud.title_filter)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will perform extra name matching functions on your Real Debrid Cloud results. Will help to limit incorrect results, but may also filter some relevant results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=rd_cloud.title_filter)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.rd.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.rd.enabled),true)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.rd_cloud),true)</visible>\
\n                        <property name="setting_label">    - Check Before Full Search</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.check.rd_cloud)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will search for results in your Real Debrid Cloud before checking other enabled scrapers</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=check.rd_cloud)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.rd.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.rd.enabled),true)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.rd_cloud),true)</visible>\
\n                        <property name="setting_label">    - Show Results at Top</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.sort_rdcloud_first)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will sort the results from your Real Debrid Cloud to the top of all results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=results.sort_rdcloud_first)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.rd.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.rd.enabled),true)</visible>\
\n                        <property name="setting_label">Priority (Lower Number Equals Higher Priority)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.rd.priority)]</property>\
\n                        <property name="setting_description">Choose the order in which Real Debrid results appear in relation to any other active accounts. The lower the number, the higher the sort order</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=rd.priority)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Alternative API URL</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.rd.alt_api)]</property>\
\n                        <property name="setting_description">Use alternative URL for the RD API. Useful if api.real-debrid.com is blocked.</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=rd.alt_api)</onclick>\
\n                    </item>\
\n            <!-- Premiumize -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Premiumize</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.pm.token),empty_setting)</visible>\
\n                        <property name="setting_label">Authorize</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Authorize your Premiumize account and use it within VibeStream</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=premiumize.authenticate)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.pm.token),empty_setting)</visible>\
\n                        <property name="setting_label">Enable</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.pm.enabled)]</property>\
\n                        <property name="setting_description">Enable the use of your Premiumize account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=pm.enabled)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.pm.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.pm.enabled),true)</visible>\
\n                        <property name="setting_label">Revoke Authorization</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.pm.account_id)]</property>\
\n                        <property name="setting_description">Revoke authorization of your Premiumize account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=premiumize.revoke_authentication)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.pm.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.pm.enabled),true)</visible>\
\n                        <property name="setting_label">Add Resolved Debrid Cache to Cloud</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.store_resolved_to_cloud.premiumize.me_name)]</property>\
\n                        <property name="setting_description">Choose which resolved media is automatically added to your Premiumize Cloud. All media or only show packs</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=store_resolved_to_cloud.premiumize.me)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.pm.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.pm.enabled),true)</visible>\
\n                        <property name="setting_label">Search Cloud Storage</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.provider.pm_cloud)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will search your Premiumize Cloud for media</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=provider.pm_cloud)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.pm.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.pm.enabled),true)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.pm_cloud),true)</visible>\
\n                        <property name="setting_label">    - Filter Results by Name</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.pm_cloud.title_filter)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will perform extra name matching functions on your Premiumize Cloud results. Will help to limit incorrect results, but may also filter some relevant results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=pm_cloud.title_filter)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.pm.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.pm.enabled),true)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.pm_cloud),true)</visible>\
\n                        <property name="setting_label">    - Check Before Full Search</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.check.pm_cloud)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will search for results in your Premiumize Cloud before checking other enabled scrapers</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=check.pm_cloud)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.pm.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.pm.enabled),true)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.pm_cloud),true)</visible>\
\n                        <property name="setting_label">    - Show Results at Top</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.sort_pmcloud_first)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will sort the results from your Premiumize Cloud to the top of all results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=results.sort_pmcloud_first)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.pm.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.pm.enabled),true)</visible>\
\n                       <property name="setting_label">Priority (Lower Number Equals Higher Priority)</property>\
\n                       <property name="setting_type">numeric</property>\
\n                       <property name="setting_value">$INFO[Window(10000).Property(vibestream.pm.priority)]</property>\
\n                       <property name="setting_description">Choose the order in which Real Debrid results appear in relation to any other active accounts. The lower the number, the higher the sort order</property>\
\n                       <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=pm.priority)</onclick>\
\n                   </item>\
\n           <!-- All Debrid -->\
\n                   <item>\
\n                       <visible>Container(2000).HasFocus(50)</visible>\
\n                       <property name="setting_label">All Debrid</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.ad.token),empty_setting)</visible>\
\n                        <property name="setting_label">Authorize</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">...</property>\
\n                        <property name="setting_description">Authorize your All Debrid account and use it within VibeStream</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=alldebrid.authenticate)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.ad.token),empty_setting)</visible>\
\n                        <property name="setting_label">Enable</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.ad.enabled)]</property>\
\n                        <property name="setting_description">Enable the use of your All Debrid account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=ad.enabled)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.ad.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.ad.enabled),true)</visible>\
\n                        <property name="setting_label">Revoke Authorization</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.ad.account_id)]</property>\
\n                        <property name="setting_description">Revoke authorization of your All Debrid account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=alldebrid.revoke_authentication)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.ad.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.ad.enabled),true)</visible>\
\n                        <property name="setting_label">Add Resolved Debrid Cache to Cloud</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.store_resolved_to_cloud.alldebrid_name)]</property>\
\n                        <property name="setting_description">Choose which resolved media is automatically added to your All Debrid Cloud. All media or only show packs</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=store_resolved_to_cloud.alldebrid)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.ad.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.ad.enabled),true)</visible>\
\n                        <property name="setting_label">Search Cloud Storage</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.provider.ad_cloud)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will search your All Debrid Cloud for media</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=provider.ad_cloud)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.ad.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.ad.enabled),true)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.ad_cloud),true)</visible>\
\n                        <property name="setting_label">    - Filter Results by Name</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.ad_cloud.title_filter)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will perform extra name matching functions on your All Debrid Cloud results. Will help to limit incorrect results, but may also filter some relevant results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=ad_cloud.title_filter)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.ad.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.ad.enabled),true)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.ad_cloud),true)</visible>\
\n                        <property name="setting_label">    - Check Before Full Search</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.check.ad_cloud)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will search for results in your All Debrid Cloud before checking other enabled scrapers</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=check.ad_cloud)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.ad.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.ad.enabled),true)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.ad_cloud),true)</visible>\
\n                        <property name="setting_label">    - Show Results at Top</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.sort_adcloud_first)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will sort the results from your All Debrid Cloud to the top of all results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=results.sort_adcloud_first)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>!String.IsEqual(Window(10000).Property(vibestream.ad.token),empty_setting)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.ad.enabled),true)</visible>\
\n                        <property name="setting_label">Priority (Lower Number Equals Higher Priority)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.ad.priority)]</property>\
\n                        <property name="setting_description">Choose the order in which Real Debrid results appear in relation to any other active accounts. The lower the number, the higher the sort order</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=ad.priority)</onclick>\
\n                    </item>\
\n            <!-- Easynews -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Easynews</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Enable</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.provider.easynews)]</property>\
\n                        <property name="setting_description">Enable the use of your Easynews account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=provider.easynews)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.easynews),true)</visible>\
\n                        <property name="setting_label">Login</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.easynews_user)]</property>\
\n                        <property name="setting_description">Enter the Login of your Easynews account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_string&amp;setting_id=easynews_user)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.easynews),true)</visible>\
\n                        <property name="setting_label">Password</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.easynews_password)]</property>\
\n                        <property name="setting_description">Enter the Password of your Easynews account</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_string&amp;setting_id=easynews_password)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.easynews),true)</visible>\
\n                        <visible>![String.IsEmpty(Window(10000).Property(vibestream.easynews_user)) + String.IsEmpty(Window(10000).Property(vibestream.easynews_password))]</visible>\
\n                        <property name="setting_label">Filter Results by Name</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.easynews.title_filter)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will perform extra name matching functions on your Easynews results. Will help to limit incorrect results, but may also filter some relevant results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=easynews.title_filter)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.easynews),true)</visible>\
\n                        <visible>![String.IsEmpty(Window(10000).Property(vibestream.easynews_user)) + String.IsEmpty(Window(10000).Property(vibestream.easynews_password))]</visible>\
\n                        <property name="setting_label">Filter Languages</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.easynews.filter_lang)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will perform extra language filtering on your Easynews results. Will help to limit incorrect results, but may also filter some relevant results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=easynews.filter_lang)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.easynews),true)</visible>\
\n                        <visible>![String.IsEmpty(Window(10000).Property(vibestream.easynews_user)) + String.IsEmpty(Window(10000).Property(vibestream.easynews_password))]</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.easynews.filter_lang),true)</visible>\
\n                        <property name="setting_label">    - Choose Languages To Include</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.easynews.lang_filters)]</property>\
\n                        <property name="setting_description">Choose which languages you wish to include in Easynews results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=set_language_filter_choice&amp;filter_setting_id=easynews.lang_filters&amp;multi_choice=true)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.easynews),true)</visible>\
\n                        <visible>![String.IsEmpty(Window(10000).Property(vibestream.easynews_user)) + String.IsEmpty(Window(10000).Property(vibestream.easynews_password))]</visible>\
\n                        <property name="setting_label">Check Before Full Search</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.check.easynews)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will search for results from your Easynews service before checking other enabled scrapers</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=check.easynews)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.easynews),true)</visible>\
\n                        <visible>![String.IsEmpty(Window(10000).Property(vibestream.easynews_user)) + String.IsEmpty(Window(10000).Property(vibestream.easynews_password))]</visible>\
\n                        <property name="setting_label">Priority (Lower Number Equals Higher Priority)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.en.priority)]</property>\
\n                        <property name="setting_description">Choose the order in which Real Debrid results appear in relation to any other active accounts. The lower the number, the higher the sort order</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=en.priority)</onclick>\
\n                    </item>\
\n            <!-- Local Media Folders -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Local Media Folders</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <property name="setting_label">Enable</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.provider.folders)]</property>\
\n                        <property name="setting_description">Enable the use of any local media folder locations i.e. NAS drives, HDDs etc</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=provider.folders)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.folders),true)</visible>\
\n                        <property name="setting_label">Set Folder Scrapers</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">empty_setting</property>\
\n                        <property name="setting_description">Choose this to activate a settings window allowing you to set the location of up to 5 devices containing local media</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=sources_folders_choice)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.folders),true)</visible>\
\n                        <property name="setting_label">Filter Results by Name</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.folders.title_filter)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will perform extra name matching functions on your local media folders results. Will help to limit incorrect results, but may also filter some relevant results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=folders.title_filter)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.folders),true)</visible>\
\n                        <property name="setting_label">Check Before Full Search</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.check.folders)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will search for results from your local media folders before checking other enabled scrapers</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=check.folders)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.folders),true)</visible>\
\n                        <property name="setting_label">Show Results at Top</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.sort_folders_first)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will sort the results from your local media folders to the top of all results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=results.sort_folders_first)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(50)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.provider.folders),true)</visible>\
\n                        <property name="setting_label">Ignore Quality and Size Filters</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.folders_ignore_filters)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will ignore any Quality or Size filters when processing local media folders results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=results.folders_ignore_filters)</onclick>\
\n                    </item>\
\n        <!-- RESULTS 60 -->\
\n            <!-- Display -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Display</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Scraper Timeout</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.timeout)]</property>\
\n                        <property name="setting_description">Choose the amount of time VibeStream will allow all scrapers to search for results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=results.timeout)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Results Display Format</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.list_format)]</property>\
\n                        <property name="setting_description">Choose the format in which VibeStream will display the results of a source search. Lists, Rows and WideList are provided</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=results_format_choice)</onclick>\
\n                    </item>\
\n            <!-- General -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">General</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Retry With All Scrapers When No Results</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.auto_rescrape_with_all_name)]</property>\
\n                        <property name="setting_description">Choose whether to rescrape with all external scrapers when there are no results. Choices are Off, Auto or Prompt</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=results.auto_rescrape_with_all)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Retry With Custom Episode Group When No Results</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.auto_episode_group_name)]</property>\
\n                        <property name="setting_description">Choose whether to rescrape with a custom episode grouping (if available) when there are no results. This setting only relates to episode scrapes. If a Custom Episode Group is already assigned to the TV Show, then the regular season/episode will be used. Choices are Off, Auto or Prompt</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=results.auto_episode_group)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Ignore All Filters When No Results</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.ignore_filter_name)]</property>\
\n                        <property name="setting_description">Choose whether to rescrape ignoring filters when there are no results. Choices are Off, Auto or Prompt</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=results.ignore_filter)</onclick>\
\n                    </item>\
\n            <!-- Sorting and Filtering -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Sorting and Filtering</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Results Sorting</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.sort_order_display)]</property>\
\n                        <property name="setting_description">Choose the priority ordering performed by VibeStream before displaying source results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=results_sorting_choice)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Results Size Sort Direction</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.size_sort_direction_name)]</property>\
\n                        <property name="setting_description">Choose the sort direction with regards to results size</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=results.size_sort_direction)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Filter Results by Size</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.filter_size_method_name)]</property>\
\n                        <property name="setting_description">Choose the method used to filter results by their size. Either by internet speed, or actual size of the result</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=results.filter_size_method)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.results.filter_size_method),1)</visible>\
\n                        <property name="setting_label">    - Internet Speed (Mbit/s)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.line_speed)]</property>\
\n                        <property name="setting_description">Enter here your internet line speed. It is a good idea to choose a value slightly below your true internet speed, although VibeStream will still reduce this value by 10% before filtering results by size</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=results.line_speed)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.results.filter_size_method),2)</visible>\
\n                        <property name="setting_label">    - Movies Maximum Size (MB)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.movie_size_max)]</property>\
\n                        <property name="setting_description">Enter here the Maximum size allowed for Movies playback</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=results.movie_size_max)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.results.filter_size_method),2)</visible>\
\n                        <property name="setting_label">    - Episodes Maximum Size (MB)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.episode_size_max)]</property>\
\n                        <property name="setting_description">Enter here the Maximum size allowed for Episodes playback</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=results.episode_size_max)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.results.filter_size_method),1) | String.IsEqual(Window(10000).Property(vibestream.results.filter_size_method),2)</visible>\
\n                        <property name="setting_label">    - Movies Minimum Size (MB)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.movie_size_min)]</property>\
\n                        <property name="setting_description">Enter here the Minimum size allowed for Movies</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=results.movie_size_min)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.results.filter_size_method),1) | String.IsEqual(Window(10000).Property(vibestream.results.filter_size_method),2)</visible>\
\n                        <property name="setting_label">    - Episodes Minimum Size (MB)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.episode_size_min)]</property>\
\n                        <property name="setting_description">Enter here the Minimum size allowed for Episodes</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=results.episode_size_min)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.results.filter_size_method),1) | String.IsEqual(Window(10000).Property(vibestream.results.filter_size_method),2)</visible>\
\n                        <property name="setting_label">    - Include Results with Unknown Size</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results.size_unknown)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will include results where the size of the file is unknown</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=results.size_unknown)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Include Pre-Release Results (CAM/SCR/TELE)</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.include_prerelease_results)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will include CAMS, SCR and TELE results through the filter</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=include_prerelease_results)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">3D Files Filter</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.filter.3d_name)]</property>\
\n                        <property name="setting_description">Choose how to handle 3D source results. They can be INCLUDED or EXCLUDED</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=filter.3d)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">HDR Files Filter</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.filter.hdr_name)]</property>\
\n                        <property name="setting_description">Choose how to handle HDR source results. They can be INCLUDED or EXCLUDED</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=filter.hdr)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Dolby Vision Files Filter</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.filter.dv_name)]</property>\
\n                        <property name="setting_description">Choose how to handle DOLBY VISION source results. They can be INCLUDED or EXCLUDED</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=filter.dv)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">AV1 Files Filter</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.filter.av1_name)]</property>\
\n                        <property name="setting_description">Choose how to handle AV1 source results. They can be INCLUDED or EXCLUDED</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=filter.av1)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">AI Enhanced/Upscaled Files Filter</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.filter_enhanced_upscaled_name)]</property>\
\n                        <property name="setting_description">Choose how to handle AI Enhanced/Upscaled source results. They can be INCLUDED or EXCLUDED</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=filter_enhanced_upscaled)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">HEVC Files Filter</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.filter.hevc_name)]</property>\
\n                        <property name="setting_description">Choose how to handle HEVC source results. They can be INCLUDED or EXCLUDED</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=filter.hevc)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.filter.hevc),0) | String.IsEqual(Window(10000).Property(vibestream.filter.hevc),2)</visible>\
\n                        <property name="setting_label">    - Max. HEVC Quality</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.filter.hevc.max_quality_name)]</property>\
\n                        <property name="setting_description">Choose the maximum quality allowed for HEVC files when allowing source select</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=filter.hevc.max_quality)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.filter.hevc),0) | String.IsEqual(Window(10000).Property(vibestream.filter.hevc),2)</visible>\
\n                        <property name="setting_label">    - Max. Autoplay HEVC Quality</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.filter.hevc.max_autoplay_quality_name)]</property>\
\n                        <property name="setting_description">Choose the maximum quality allowed for HEVC files being autoplayed</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=filter.hevc.max_autoplay_quality)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Custom Autoplay Sort To Top</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.preferred_autoplay)]</property>\
\n                        <property name="setting_description">Choose video and audio properties that will be sorted to the top of the sources list when using Autoplay. Choose up to 5 different parameters to be used, in order of importance. "Sort to Top" settings involving Debrid Cache and Folder Scraper results will take priority over these 5 params</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=preferred_autoplay_choice)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Choose Audio Properties to Exclude</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.filter_audio)]</property>\
\n                        <property name="setting_description">Choose audio properties that will be filtered out of source results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=audio_filters_choice)</onclick>\
\n                    </item>\
\n            <!-- Results Color Highlights -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Results Color Highlights</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <property name="setting_label">Highlight Results Based On</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.highlight.type_name)]</property>\
\n                        <property name="setting_description">Choose the method used to provide highlight colors to source results. The options are PROVIDER, QUALITY, or the use of a SINGLE COLOR</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=highlight.type)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),0)</visible>\
\n                        <property name="setting_label">    - Real Debrid Color</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.provider.rd_highlight)]]$INFO[Window(10000).Property(vibestream.provider.rd_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose Real Debrid color</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=provider.rd_highlight)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),0)</visible>\
\n                        <property name="setting_label">    - Premiumize Color</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.provider.pm_highlight)]]$INFO[Window(10000).Property(vibestream.provider.pm_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose Premiumize color</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=provider.pm_highlight)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),0)</visible>\
\n                        <property name="setting_label">    - All Debrid Color</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.provider.ad_highlight)]]$INFO[Window(10000).Property(vibestream.provider.ad_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose All Debrid color</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=provider.ad_highlight)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),0)</visible>\
\n                        <property name="setting_label">    - Easynews Color</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.provider.easynews_highlight)]]$INFO[Window(10000).Property(vibestream.provider.easynews_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose Easynews color</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=provider.easynews_highlight)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),0)</visible>\
\n                        <property name="setting_label">    - Debrid Cloud Color</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.provider.debrid_cloud_highlight)]]$INFO[Window(10000).Property(vibestream.provider.debrid_cloud_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose Debrid Cloud color</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=provider.debrid_cloud_highlight)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),0)</visible>\
\n                        <property name="setting_label">    - Local Media Folders Color</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.provider.folders_highlight)]]$INFO[Window(10000).Property(vibestream.provider.folders_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose Local Media Folders color</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=provider.folders_highlight)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),1)</visible>\
\n                        <property name="setting_label">    - 4K Results Color</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.scraper_4k_highlight)]]$INFO[Window(10000).Property(vibestream.scraper_4k_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose 4K Quality color</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=scraper_4k_highlight)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),1)</visible>\
\n                        <property name="setting_label">    - 1080P Results Color</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.scraper_1080p_highlight)]]$INFO[Window(10000).Property(vibestream.scraper_1080p_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose 1080P Quality color</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=scraper_1080p_highlight)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),1)</visible>\
\n                        <property name="setting_label">    - 720P Results Color</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.scraper_720p_highlight)]]$INFO[Window(10000).Property(vibestream.scraper_720p_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose 720P Quality color</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=scraper_720p_highlight)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),1)</visible>\
\n                        <property name="setting_label">    - SD Results Color</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.scraper_SD_highlight)]]$INFO[Window(10000).Property(vibestream.scraper_SD_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose SD Quality color</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=scraper_SD_highlight)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(60)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.highlight.type),2)</visible>\
\n                        <property name="setting_label">    - Single Color For All</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">[COLOR $INFO[Window(10000).Property(vibestream.scraper_single_highlight)]]$INFO[Window(10000).Property(vibestream.scraper_single_highlight)][/COLOR]</property>\
\n                        <property name="setting_description">Choose Single color for all results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=scraper_color_choice&amp;setting_id=scraper_single_highlight)</onclick>\
\n                    </item>\
\n      <!-- PLAYBACK 70 -->\
\n            <!-- Playback Movies -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <property name="setting_label">Movies</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <property name="setting_label">Auto Play</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.auto_play_movie)]</property>\
\n                        <property name="setting_description">Enable this for Movies to play automatically when selected</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=auto_play_movie)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_movie),false)</visible>\
\n                        <property name="setting_label">Limit Quality</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results_quality_movie)]</property>\
\n                        <property name="setting_description">Choose the Quality properties allowed for source select results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=set_quality_choice&amp;setting_id=results_quality_movie)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_movie),true)</visible>\
\n                        <property name="setting_label">Limit Auto Play Quality</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.autoplay_quality_movie)]</property>\
\n                        <property name="setting_description">Choose the Quality properties allowed for autoplay results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=set_quality_choice&amp;setting_id=autoplay_quality_movie)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <property name="setting_label">Automatically Resume Playback</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.auto_resume_movie_name)]</property>\
\n                        <property name="setting_description">Choose when VibeStream will automatically resume playback of an in-progress Movie</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=auto_resume_movie)</onclick>\
\n                    </item>\
\n            <!-- Playback Episodes -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <property name="setting_label">Episodes</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <property name="setting_label">Auto Play</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.auto_play_episode)]</property>\
\n                        <property name="setting_description">Enable this for Episodes to play automatically when selected</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=auto_play_episode)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_episode),false)</visible>\
\n                        <property name="setting_label">Limit Quality</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.results_quality_episode)]</property>\
\n                        <property name="setting_description">Choose the Quality properties allowed for source select results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=set_quality_choice&amp;setting_id=results_quality_episode)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_episode),true)</visible>\
\n                        <property name="setting_label">Limit Auto Play Quality</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.autoplay_quality_episode)]</property>\
\n                        <property name="setting_description">Choose the Quality properties allowed for autoplay results</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=set_quality_choice&amp;setting_id=autoplay_quality_episode)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_episode),true)</visible>\
\n                        <property name="setting_label">Autoplay Next Episode</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.autoplay_next_episode)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will automatically search for sources for the next episode of a TV Show towards the end of the episode currently being watched</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=autoplay_next_episode)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_episode),true) + String.IsEqual(Window(10000).Property(vibestream.autoplay_next_episode),true)</visible>\
\n                        <property name="setting_label">    - When No Interaction with Window</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.autoplay_default_action_name)]</property>\
\n                        <property name="setting_description">Choose the action performed when you fail to interact with the Next Episode alert</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=autoplay_default_action)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_episode),true) + String.IsEqual(Window(10000).Property(vibestream.autoplay_next_episode),true)</visible>\
\n                        <property name="setting_label">    - Next Episode Alert Method</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.autoplay_alert_method_name)]</property>\
\n                        <property name="setting_description">Choose the alert method when Next Episode is ready to be played. Choose Window or Notification</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=autoplay_alert_method)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_episode),true) + String.IsEqual(Window(10000).Property(vibestream.autoplay_next_episode),true)</visible>\
\n                        <property name="setting_label">    - Show Alert After (%) Playback</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.autoplay_next_window_percentage)]</property>\
\n                        <property name="setting_description">Choose when VibeStream will show the Next Episode Alert</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=autoplay_next_window_percentage)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_episode),true) + String.IsEqual(Window(10000).Property(vibestream.autoplay_next_episode),true)</visible>\
\n                        <property name="setting_label">    - Use Chapter Info For Alert When Available</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.autoplay_use_chapters)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will attempt to use video file Chapter information to ascertain when to show the Next Episode alert. If unsuccessful, then the percentage of playback value will be used instead</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=autoplay_use_chapters)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_episode),false)</visible>\
\n                        <property name="setting_label">Autoscrape Next Episode</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.autoscrape_next_episode)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will automatically search for sources for the next episode of a TV Show towards the end of the episode currently being watched</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=autoscrape_next_episode)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_episode),false) + String.IsEqual(Window(10000).Property(vibestream.autoscrape_next_episode),true)</visible>\
\n                        <property name="setting_label">    - Show Notification After (%) Playback</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.autoscrape_next_window_percentage)]</property>\
\n                        <property name="setting_description">Choose when VibeStream will show the Next Episode Alert</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=autoscrape_next_window_percentage)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.auto_play_episode),false) + String.IsEqual(Window(10000).Property(vibestream.autoscrape_next_episode),true)</visible>\
\n                        <property name="setting_label">    - Use Chapter Info For Alert When Available</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.autoscrape_use_chapters)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will attempt to use video file Chapter information to ascertain when to show the Next Episode alert. If unsuccessful, then the percentage of playback value will be used instead</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=autoscrape_use_chapters)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <property name="setting_label">Automatically Resume Playback</property>\
\n                        <property name="setting_type">action</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.auto_resume_episode_name)]</property>\
\n                        <property name="setting_description">Choose when VibeStream will automatically resume playback of an in-progress Episode</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_from_list&amp;setting_id=auto_resume_episode)</onclick>\
\n                    </item>\
\n            <!-- Playback Utilities -->\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <property name="setting_label">Playback Utilities</property>\
\n                        <property name="setting_type">separator</property>\
\n                        <onclick>noop</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <property name="setting_label">Limit Resolve Attempts to Selected Result</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.playback.limit_resolve)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will limit the playback attempts to only the source result chosen. If disabled, VibeStream will potentially try 15 results of similar properties to your chosen source result until it is able to successfully resolve and playback</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=playback.limit_resolve)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <property name="setting_label">Check Volume Before Start of Playback</property>\
\n                        <property name="setting_type">boolean</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.playback.volumecheck_enabled)]</property>\
\n                        <property name="setting_description">Enable this and VibeStream will attempt to check the current level of volume within Kodi, and adjust it downwards if it is exceeding a set level</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_boolean&amp;setting_id=playback.volumecheck_enabled)</onclick>\
\n                    </item>\
\n                    <item>\
\n                        <visible>Container(2000).HasFocus(70)</visible>\
\n                        <visible>String.IsEqual(Window(10000).Property(vibestream.playback.volumecheck_enabled),true)</visible>\
\n                        <property name="setting_label">    - Set Max. Percent Starting Volume (0-100)</property>\
\n                        <property name="setting_type">numeric</property>\
\n                        <property name="setting_value">$INFO[Window(10000).Property(vibestream.playback.volumecheck_percent)]</property>\
\n                        <property name="setting_description">Choose the maximum allowed volume level</property>\
\n                        <onclick>RunPlugin(plugin://plugin.video.vibestream/?mode=settings_manager.set_numeric&amp;setting_id=playback.volumecheck_percent)</onclick>\
\n                    </item>'