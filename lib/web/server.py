# -*- coding: utf-8 -*-

from . import app, api


# import models for API interface
from models.github import Search_repo


# Restful API
api.add_resource(Search_repo, '/repo')










