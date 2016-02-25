#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can override all defaults in "settings.py"
from defaults import *
try:
	from settings import *
except:
	pass

from flask import Flask, request, redirect, abort, jsonify

app = Flask(__name__)


@app.route('/')
def index():
	return jsonify(status='ok', services=['/api'])


