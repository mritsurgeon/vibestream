# -*- coding: utf-8 -*-
import sys
from modules.router import routing, sys_exit_check
# from modules.kodi_utils import logger

mode = routing(sys)
# Do not exit when we just showed the main list (e.g. after skipping wizard)
if mode != 'navigator.main' and sys_exit_check():
	sys.exit(1)

