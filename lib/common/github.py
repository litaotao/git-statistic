# -*-coding: utf8 -*-

"""
    github.py
    ~~~~~~~~~~~~

    A simple implementation of github API v3.

    :Author: taotao.li
    :last updated: Jan.31st.2014
"""

import requests

prefix = 'https://api.github.com'



def extract_repos(repos):
	"""
	Extract meta data of each repo : 
		full_name
		id:
		private:
		fork:
		stargazers_count:
		watchers_count:
		forks_count:
		open_issues_count:
		watchers:
	"""
	res = {}
	tmp = {}
	for i in repos:
		name = i.get('full_name', 'None')
		tmp['id'] = i.get('id', 0)
		tmp['private'] = i.get('private', 0)
		tmp['isfork'] = i.get('fork', 0)
		tmp['stargazers_count'] = i.get('stargazers_count', 0)
		tmp['forks'] = i.get('forks_count', 0)
		tmp['issues'] = i.get('open_issues_count', 0)
		tmp['watchers'] = i.get('watchers', 0)
		tmp['stars'] = i.get('stargazers_count', 0)
		tmp['create'] = i.gt('created_at', '')
		res[name] = tmp

	return res


def get_repos(language):
	"""
	Get some meta data of a repos.
	For Github can only return up to 1000 when use a normal search, we had
		to use some tricks to get all the repos' data we need.
	Here we use the forks number to seperate each request url, to get all the
		repos' data. Of course, in this way, we need first get the max forks 
		number of repos written in our defined language. 
	"""
	## step 1. get the max forks number 
	suffix = '/search/repositories?q=language:{}&sort=forks&order=desc'
	url = (prefix + suffix).format(language)
	raw = requests.get(url)
	total_count = raw.get('total_count', 0)
	max_forks = raw.get('items', [{}])[0].get('forks_count', 0)

	## step 2. get all the repos written in a defined language

	suffix = '/search/repositories?q=language:{}+forks={}&page={}&per_page=100'

	for i in range(max_forks+1):

		url = (prefix + suffix).format(language, i, str(1))
		raw = requests.get(url)

		# do some data store operation

		links = raw.links
		if 'next' not in links:
			res = extract_repos(raw['items'])
			yield res

		while 'next' in links:
			raw = requests.get(url)
			links = next.links
			res = extract_repos(raw['items'])
			url = links['next']['url']
			yield res


def extract_commit(commit, owner=True):
	"""
	return list
	"""
	if owner:
		res = [i.get('total', 0) for i in commit]
	else:
		res = commit
	return res


def get_commit(owner, repos):
	suffix = '/repos/{}/{}/stats/commit_activit'
	url = (prefix + suffix).format(owner, repos)
	raw = requests.get(url)

	# do some date store operation here
	weekly_commit = extract_commit(raw)

	suffix = '/repos/{}/{}/stats/participation'
	url = (prefix + suffix).format(owner, repos)
	raw = requests.get(url)

	# do some date store operation here
	user_commit = extract_commit(raw, owner=False)

	return weekly_commit, user_commit










