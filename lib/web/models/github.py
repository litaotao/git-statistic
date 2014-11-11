# -*- coding: utf-8 -*-

from flask import request, Response
from flask.ext.restful import Resource
import requests
from web import mongo_client, git_url



class Search_repo(Resource):
	'''
	language: writen by which language you want to see 
	sortby: stars, forks, watchers
	###
	store in mongo as key-value
	key: repo id return by git
	value: 
		name: repo full name
		is_fork: is this repo forked from another one
		create_at: time created this repo
		update_at: time last updated
		pushed_at: time last pushed
		homepage: home page for this repo
		size: 
		language: language mainly writen this repo
		has_wiki: is this repo has a wiki page
		open_issues: number of issues still opened
		watchers: number of people who watch this repo
		forks: number of people who forks this repo
		stars: number of people who vote this repo
	###
	to be added:
		total issues
		total pull requests
		people
		organizations
		locations
	'''
	def get():
		# parse url parameters
		language = request.args.get('language', 'none')
		sortby = request.args.get('sortby', 'none')

		# validate url
		if language is 'none' or language is 'none':
			return 'error'

		# build url
		kind = '/search/repositories?'
		para = 'q={}+language:{}&sort='.format(language, language, sortby)
		url = git_url + kind + para





