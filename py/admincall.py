#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


class AdminCallError(Exception):
	def __init__(self, message, status_code):
		super().__init__(message)
		self.status_code = status_code


class AdminCall(object):
	""" Admin calls against the Sync Gateway.
	
	User accounts: http://developer.couchbase.com/documentation/mobile/1.1.0/develop/guides/sync-gateway/administering-sync-gateway/authorizing-users/index.html#accounts
	"""
	
	def __init__(self, base):
		self.base = base
	
	def user_create(self, username, userdata):
		""" Executes a POST against `_user` with the given userdata as JSON.
		On success, the sync gateway doesn't return data; same with this
		method.
		"""
		url = '{}/_user/'.format(self.base)
		userdata = {} if userdata is None else userdata
		userdata['name'] = username.replace(r'[^\w\3_]', '')
		res = requests.post(url, json=userdata)
		if res.status_code >= 400:
			raise AdminCallError(res.json().get('reason'), res.status_code)
	
	def user_info(self, username):
		""" Executes a GET against `_user/username`.
		"""
		url = '{}/_user/{}'.format(self.base, username)
		res = requests.get(url)
		res.raise_for_status()
		return res.json()
	
	def user_update(self, username, update):
		""" Executes a PUT against `_user/username` and the given data as JSON.
		"""
		url = '{}/_user/{}'.format(self.base, username)
		print('PUT', update)
		res = requests.put(url, json=update)
		res.raise_for_status()
		return res.json()
		

"""
authn + authz
$ curl -H "Content-Type: application/json" -X POST localhost:4985/eponyms/_session -d '{"name": "firstuser"}'
{"error":"not_found","reason":"No such user \"firstuser\""}

$ curl -H "Content-Type: application/json" -X PUT localhost:4985/eponyms/_user/firstuser -d '{"admin_roles": ["admin"]}'

$ curl -H "Content-Type: application/json" -X POST localhost:4985/eponyms/_session -d '{"name": "firstuser"}'
{"session_id":"97ec62ed6c46ad68cc0888ec8105a183cdd1f888","expires":"2016-02-25T22:36:39.400641211Z","cookie_name":"SyncGatewaySession"}
"""
