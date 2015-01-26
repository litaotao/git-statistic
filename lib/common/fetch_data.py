# -*-coding: utf8 -*-

"""
    fetch_data.py
    ~~~~~~~~~~~~

    For all the data people need almost are the same, and it's time
    consuming to get data from API each time. So a wise choice is to 
    download the data needed in local in advanced.

    :Author: taotao.li
    :last updated: Jan.26th.2014
"""

import os
import json
import github as gh


class FetchData(object):
	"""Get the raw data of a language, first it will try to find
		in local ../data directory, then it would use Github API to 
		fetch data and store it in local if there isn't data in the 
		filesystem.
		data file format: language-createDate.json
	"""
	def __init__(self, language):
		self.language = language
		self.data_file = None
		self.language_data = None
		
	def get_data():
		all_data_file = os.listdir('../data')
		
		for i in all_data_file:
			if self.language in i:
				self.data_file = i
				break
		if self.data_file:
			f = file('../data/{}'.format(self.data_file), 'r')
			self.language_data = json.load(f)
			f.close()
		else:
			self.language_data = self._get_data()
		
		return self.language_data

	def _get_data():
		pass


