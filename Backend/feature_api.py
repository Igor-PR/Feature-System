from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from models import *
from support_functions import *

#This file contians the functions that compose the Features API 

"""
	The addFeature receives the form with the attributes of the feature as params and the database session.
	The function extract the information from the from and creates a Feature object and adds it to the database
	After adding to the database, it defines the client priority according to the specifications, if something goes
	wrong, it deletes the added feature from the database
	It returns false if there was an error or true if there wasn't
"""
def addFeature(params, db_cursor):
	title = params['title']
	description = params['description']
	client_id = params['client_id']
	client_priority = params['client_priority']
	target_date = datetime.strptime(params['date'],'%m/%d/%Y %I:%M %p')
	product_area_id = params['product_area']

	cursor = db_cursor

	try:
		feature = Feature(title,description,client_id,target_date,product_area_id)
		cursor.add(feature)
		cursor.commit()
	except Exception as e:
		print("[ERROR] Something went wrong.")
		print(e)
		return False
	else:
		feature_id = feature.id
		result = defineClientePriority(feature_id,client_id,client_priority,db_cursor)

		if not result:
			deleteFeature(feature_id,db_cursor)

		return True

"""
	The getFeatures function, doesn't take any parameters.
	the Feature.query.all() returns a list of all the Feature in the Feature table and they are added to the list 
	for every Feature obejct in the list, all it's attributes are appended to a list of elements. Every attribute of the 
	Feature model that references another model is used to query the database for that model information, simulation a JOIN query
	the the list of lists with the elements is returned by the function.
"""
def getFeatures():
	listOfFeatures = []
	listOfElements = []

	try:
		listOfFeatures = Feature.query.all()
	except Exception as e:
		print("[ERROR] Something went wrong.")
		print(e)
	else:
		for feature in listOfFeatures:
			array = []
			array.append(feature.id)
			array.append(feature.title)
			array.append(feature.description)
			#Query the Client database and get the name for that id
			client = Client.query.filter_by(id=feature.client_id).first()
			array.append(client.name)
			#Query the ClientPriority database and get the name for that client
			clientPriority = ClientPriority.query.filter_by(feature_id=feature.id,client_id=feature.client_id).first()
			array.append(clientPriority.priority)
			#Query the ProductArea database and get the name for that product_area_id
			productArea = ProductArea.query.filter_by(id=feature.product_area_id).first()
			array.append(productArea.area)
			array.append(feature.target_date)
			listOfElements.append(array)


	return listOfElements

"""
	The deleteFeature receives the id and a database session.
	It's a simple function that queries the database to find which element has the id and then delete it
	it returns false if there was an error or true if there wasn't
"""
def deleteFeature(id,db_cursor):
	cursor = db_cursor

	try:
		Feature.query.filter_by(id=id).delete()
		cursor.commit()
	except Exception as e:
		print("[ERROR] Something went wrong.")
		print(e)
		return False
	else:
		return True		