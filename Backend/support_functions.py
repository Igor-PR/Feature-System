import psycopg2
from flask_sqlalchemy import SQLAlchemy
from models import ClientPriority
from sqlalchemy import update

"""
	The addProductAreas receives a feature id, a client id, the client priority and the database session.
	The function gets all the ClientPriority objects related to the client id. Then, a list of priorities is created with
	the priority method from the selected ClientPriority objects
	This list is used for the setPriority function.
	It returns false if there was an error or true if there wasn't
"""
def defineClientePriority(feature_id, client_id, client_priority, db_cursor):
	
	cursor = db_cursor

	listOfPriorities = []

	try:
		listOfClientPriority = ClientPriority.query.filter_by(client_id=client_id).all()
		for clientPriority in listOfClientPriority:
			listOfPriorities.append(clientPriority.priority)	
	except Exception as e:
		print("[ERROR] Something went wrong.")
		print(e)
		return False
	else:
		setPriority(int(client_priority),listOfPriorities,db_cursor, client_id, feature_id = feature_id)

	return True


"""
	The setPriotiy function receives a priority, the list of priorities, the database session, 
	a client id and a feature id the defaults to None
	This function recursevely looks for the next available priority for that client.
"""
def setPriority(priority, listOfPriorities, db_cursor, client_id, feature_id = None):
	
	#Recursively looks if the priority is in the list, if it's not, it looks for the next one
	if priority in listOfPriorities:
		setPriority(priority + 1, listOfPriorities, db_cursor, client_id)

	cursor = db_cursor
	#If feature_id is not None(default value), it means it's a new value so it has to be inserted
	if feature_id is not None:
		clientPriority = ClientPriority(feature_id,client_id,priority)
		cursor.add(clientPriority)
		cursor.commit()

	#Else, it has to be altered. It selects the oldPriority/current priority in the db and updates with a new priority
	else:
		oldPriority = priority - 1

		#Looking for the element with the old priority
		clientPriority = ClientPriority.query.filter_by(priority = oldPriority,client_id=client_id).first()	
		#Setting the new priority
		clientPriority.priority = priority
		#Updating the new priority
		cursor.commit()