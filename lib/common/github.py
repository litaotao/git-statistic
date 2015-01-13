# -*-coding: utf8 -*-

"""
    github.py
    ~~~~~~~~~~~~

    A simple implementation of github API v3.

    :Author: taotao.li
    :last updated: Dec.31st.2014
"""

import requests



prefix = 'https://api.github.com'


def get_repos(language):
	suffix = '/search/repositories?q={}&page={}'
	url = (prefix + suffix).format(language, str(1))
	raw = requests.get(url)

	# do some data store operation

	links = raw.links
	while 'next' in links:
		url = links['next']['url']
		next = requests.get(url)

		# do some data store operation

		links = next.links

	return

def get_commit(owner, repos):
	suffix = '/repos/{}/{}/stats/commit_activit'
	url = (prefix + suffix).format(owner, repos)
	raw = requests.get(url)

	# do some date store operation here

	return 






