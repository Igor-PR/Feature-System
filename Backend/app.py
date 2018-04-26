# -------Library Imports ---
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

import psycopg2

import sys
import os

# ---------- Setting up the app -- 

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# = "postgres://azfbitfjpwhcxd:fb7dc17eab954baffe407dd7c9ad0a9190585bcead6272860a646206fa32d5c3@ec2-23-23-142-5.compute-1.amazonaws.com:5432/d6eo8ores81ca7"
# = os.environ['DATABASE_URL']
db = SQLAlchemy(app)



# --------------------
# ---- Importing the API--
from feature_api import *
from client_api import *
from product_area_api import *
#-----------------------------

"""
	The app implements 3 routes, /Features, /Clients, and /ProductAreas for the API. The methods supported are POST, GET and DELETE.
	For each method, a function has been implemented to handle the information. All these functions receive the necessary parameters
	to handle the database queries
	Each function return a jsonify(to handle the headers) answer
"""
@app.route('/Features', methods=['POST', 'GET', 'DELETE'])
@cross_origin()
def featureAPI():
	if request.method == 'POST':
		if addFeature(params = request.form, db_cursor = db.session):
			return jsonify("OK")
		else:
			return jsonify("Failed")
	if request.method == 'GET':
		response = getFeatures()
		return jsonify(response)
	if request.method == 'DELETE':
		id = request.form['id']		
		if deleteFeature(id = id, db_cursor = db.session):
			return jsonify("OK")
		else:
			return jsonify("Failed")			

@app.route('/Clients', methods=['POST', 'GET', 'DELETE'])
@cross_origin()
def clientAPI():
	if request.method == 'POST':
		name = request.form['name']
		if addClient(name = name, db_cursor = db.session):
			return jsonify("OK")
		else:
			return jsonify("Failed")
	if request.method == 'GET':
		response = getClients()
		return jsonify(response)
		
	if request.method == 'DELETE':
		id = request.form['id']	
		if deleteClient(id = id, db_cursor = db.session):
			return jsonify("OK")
		else:
			return jsonify("Failed")	

@app.route('/ProductAreas', methods=['POST', 'GET', 'DELETE'])
@cross_origin()
def productAreasAPI():		
	if request.method == 'POST':
		productArea = request.form['productArea']
		if addProductAreas(product_area = productArea, db_cursor = db.session):
			return jsonify("OK")
		else:
			return jsonify("Failed")
	if request.method == 'GET':
		response = getProductAreas()
		return jsonify(response)
	if request.method == 'DELETE':
		id = request.form['id']		
		if deleteProductAreas(id = id, db_cursor = db.session):
			return jsonify("OK")
		else:
			return jsonify("Failed")		
	
