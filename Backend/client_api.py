from flask_sqlalchemy import SQLAlchemy
from models import Client

#This file contians the functions that compose the client API 

"""
	The getClients function, doesn't take any parameters.
	the Client.query.all() returns a list of all the Clients in the Client table 
	the serialize function turns an instance of the Client object into a list with all it's attributes
	this list is appended by the listOfClients and the list of lists is returned by the function.
"""
def getClients():
	listOfClients = []
	listOfClients = [i.serialize for i in Client.query.all()]
	return listOfClients


"""
	The deleteCliente receives the id and a database session.
	It's a simple function that queries the database to find which element has the id and then delete it
	it returns false if there was an error or true if there wasn't
"""
def deleteClient(id,db_cursor):
	cursor = db_cursor

	try:
		Client.query.filter_by(id=id).delete()
		cursor.commit()	
	except Exception as e:
		print("[ERROR] Something went wrong.")
		print(e)
		return False
	else:
		return True

"""
	The addClient receives the name of the area as product_area and the database session.
	The function creates a Client object and adds it to the database
	it returns false if there was an error or true if there wasn't
"""
def addClient(name, db_cursor):								
	cursor = db_cursor

	try:
		client = Client(name)
		cursor.add(client)
		cursor.commit()
	except Exception as e:
		print("[ERROR] Something went wrong.")
		print(e)
		return False
	else:
		return True		