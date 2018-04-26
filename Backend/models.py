from app import db

"""
This file contains all the Database models that this algorithm uses. They have the column properties and table relations
All of them implment the __init__ method as a class constructor, __repr__ method returns a string representation of the model
they also implement the serialize property. This property transforms the model into a serializeable format, in this case,
it's a list containing the attributes of the model

"""

class Feature(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	description =  db.Column(db.Text)
	client_id = db.Column(db.Integer)
	product_area_id = db.Column(db.Integer)
	target_date = db.Column(db.DateTime)

	def __init__(self, title,description,client_id,target_date,product_area_id):
		self.title = title
		self.description = description
		self.client_id = client_id
		self.product_area_id = product_area_id
		self.target_date = target_date

	@property
	def serialize(self):
	   """Return object data in easily serializeable format"""
	   return [self.id,self.title,self.description,self.client_id,self.product_area_id,dump_datetime(self.target_date)]	

	def __repr__(self):
		return '{"id": ' + str(self.id) + ', "title": ' + self.title + ', "client_id": ' + str(self.client_id) + \
		', "product_area_id": ' + str(self.product_area_id) + ' }'

class Client(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	def __init__(self, name):
		self.name = name

	@property
	def serialize(self):
	   """Return object data in easily serializeable format"""
	   return [self.id,self.name]

	def __repr__(self):
		return '{"id": ' + str(self.id) + ', "name": ' + self.name + ' }'


class ProductArea(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	area = db.Column(db.String(80))

	def __init__(self, area):
		self.area = area

	@property
	def serialize(self):
	   """Return object data in easily serializeable format"""
	   return [self.id,self.area]	

	def __repr__(self):
		return {"id":self.id, "area": self.area}

class ClientPriority(db.Model):

	feature_id = db.Column(db.Integer, db.ForeignKey('feature.id'), primary_key=True)
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'), primary_key=True)
	priority = db.Column(db.Integer)

	def __init__(self, feature_id, client_id, priority):
		self.feature_id = feature_id
		self.client_id = client_id
		self.priority = priority

	@property
	def serialize(self):
	   """Return object data in easily serializeable format"""
	   return [self.feature_id,self.client_id, self.priority]	

	def __repr__(self):
		return '{"feature_id": ' + str(self.feature_id) + ', "client_id": ' + str(self.client_id) + ', "priority": ' + str(self.priority) +' }'
