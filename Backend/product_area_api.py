from flask_sqlalchemy import SQLAlchemy	
from models import ProductArea

#This file contians the functions that compose the Product Area API 

"""
	The getProductAreas function, doesn't take any parameters.
	the ProductArea.query.all() returns a list of all the ProductAreas in the ProductArea table 
	the serialize function turns an instance of the ProductArea object into a list with all it's attributes
	this list is appended by the listOfProductAreas and the list of lists is returned by the function.
"""
def getProductAreas():
	listOfProductAreas = []
	listOfProductAreas = [i.serialize for i in ProductArea.query.all()]
	return listOfProductAreas


"""
	The deleteProductAreas receives the id and a database session.
	It's a simple function that queries the database to find which element has the id and then delete it
	it returns false if there was an error or true if there wasn't
"""
def deleteProductAreas(id,db_cursor):
	cursor = db_cursor

	try:
		ProductArea.query.filter_by(id=id).delete()
		cursor.commit()
	except Exception as e:
		print("[ERROR] Something went wrong.")
		print(e)
		return False
	else:
		return True	

"""
	The addProductAreas receives the name of the area as product_area and the database session.
	The function creates a ProductArea object and adds it to the database
	it returns false if there was an error or true if there wasn't
"""
def addProductAreas(product_area, db_cursor):								
	cursor = db_cursor

	try:
		productArea = ProductArea(product_area)
		cursor.add(productArea)
		cursor.commit()
	except Exception as e:
		print("[ERROR] Something went wrong.")
		print(e)
		return False
	else:
		return True					