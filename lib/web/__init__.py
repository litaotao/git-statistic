# -*- coding: utf-8 -*-

from flask.ext.restful import Api
from flask import Flask 
from pymongo import MongoClient
import ConfigParser
from common import github_api_v3


# read statistic configurations
cf = ConfigParser.ConfigParser()
cf.read('../etc/statistic.conf')
if cf.has_section('mongo'):
	pass
else:
	cf.read('../../etc/statistic.conf')


# get the MongoDB url
mongo_host = cf.get('mongo', 'host')
mongo_port = cf.get('mongo', 'port')


# get the username and pwd
user = cf.get('user', 'user')
pwd = cf.get('user', 'pwd')


# store the configure
configure = {}
configure['mongo'] = zip(mongo_host, mongo_port)


# create a mongo client
mongo_client = MongoClient(mongo_host, int(mongo_port))


# create a github api client
git_client = github_api_v3.GitHub(username=user, password=pwd)


app = Flask(__name__)
api = Api(app)


import server


