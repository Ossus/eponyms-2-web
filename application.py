#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# you can override all defaults in "settings.py"
from defaults import *
try:
	from settings import *
except:
	pass

import logging
import py.admincall as admincall
from flask import Flask, request, redirect, abort, jsonify

app = Flask(__name__)


@app.route('/')
def index():
	return jsonify(status='ok', services=['/api/v1'])


# MARK: - Admin

@app.route('/api/v1a/<username>', methods=['GET', 'PUT', 'POST'])
def api_v1a_user(username):
	try:
		call = _admin_call()
		data = None
		if 'PUT' == request.method:
			update = request.get_json()
			data = call.user_update(username, update=update)
		elif 'POST' == request.method:
			update = request.get_json()
			call.user_create(username, update)
		else:
			data = call.user_info(username)
		return jsonify(status='ok', data=data)
	except admincall.AdminCallError as e:
		logging.error("`api_v1a_user()`: {}".format(e))
		return jsonify(status=str(e.status_code), reason=str(e)), e.status_code
	except Exception as e:
		logging.error("`api_v1a_user()`: {}".format(e))
		#raise e
		return jsonify(status='Server Error'), 500
	

def _admin_call():
	return admincall.AdminCall('{}/{}'.format(sync_gateway_admin_url, sync_gateway_database))


# MARK: - App

@app.errorhandler(404)
def page_not_found(e):
	return jsonify(status='Not Found'), 404

