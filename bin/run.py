# -*- coding: utf-8 -*-
"""
	run.py
	~~~~~~~~~~~~

	web interface, using flask and restful

	:Author: taotao.li
	:last updated: Nov.11th.2014
"""

import sys
sys.path.insert(0,'../')
sys.path.insert(0,'../lib/')
sys.path.insert(0,'../lib/web/')

from web.server import app, api

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 7000, debug = True)


