#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from application import app as application


# if starting directly, put into debug mode
if '__main__' == __name__:
	logging.basicConfig(level=logging.DEBUG)
	application.run(debug=True, port=8000)
