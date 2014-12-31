# -*- coding: utf-8 -*-

from pymongo import MongoClient
import ConfigParser


# read statistic configurations
cf = ConfigParser.ConfigParser()
cf.read('../etc/statistic.cfg')
if cf.has_section('url'):
	pass
else:
	cf.read('../../etc/statistic.cfg')


# get the mercury fork url
git_url = cf.get('url', 'git')


mongo_client = MongoClient('localhost', 27017)


import server