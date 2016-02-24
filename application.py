#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, abort, jsonify

app = Flask(__name__)


@app.route('/')
def index():
	return jsonify(status='ok', services=['/api'])


