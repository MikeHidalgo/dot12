#!/usr/bin/env python
# _____________________________________________________________________________
#  - This unpublished material is proprietary to the author(s).
#  - The methods and techniques described herein are
#  - considered trade secrets and/or confidential. Reproduction or
#  - distribution, in whole or in part, in any medium, is forbidden
#  - except by express written permission of the author(s).
#
#  - Copyright (C) - All Rights Reserved 2017 - 2027
#  - Unauthorized copying of this file, via any medium is strictly prohibited
#
#  - Written by Mike Hidalgo - MHidalgo@curvature.com  January 2018
#
#  - Initial draft - prof of concept ( poc ) - serial number checker
# _____________________________________________________________________________

# Needed Libraries
from flask import Flask
from flask import render_template
from flask import json
from flask import request
from pymongo import MongoClient
from pprint import pprint
import sys
from mongoprint import db_print

# _____________________________________________________________________________

# Flask init
app = Flask(__name__, static_url_path='/static')

# Connect to Mongo
client = MongoClient('127.0.0.1', 27017)

# Database Name
db = client.CTE_Metrics

# Collection Name
collection = db.pxeNetwork

# Record init
record = [{"oem": "xxx", "product_name": "xxx", "serial_number": "xxx", "system_ip_address": "xxx", "ipmi_ip_address": "xxx"}]

# _____________________________________________________________________________

@app.route('/')
def student():
	return render_template('index.html', result = record)

#   -----------------------------------------------------
@app.route('/serial_search',methods = ['POST', 'GET'])
def result2():
	if request.method == 'POST':
		serial = request.form["serial_number"]
		serial_search = collection.find({ "serial_number": serial }).sort([("_id", -1)]).limit(1);
		for record in serial_search:
			db_print(record)
			return render_template('index.html', result = record)
#			------------------------------------------------------
# _____________________________________________________________________________

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port=10000)

# _____________________________________________________________________________
# -
# - H569NBX
# - SGH429LKKH
# - USE827N2BF
# - BKRXQ52
# - SGH429LKKH
# -
# _____________________________________________________________________________
