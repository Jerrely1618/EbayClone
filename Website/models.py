from . import db 
from flask_login import UserMixin
from datetime import datetime


class UserApplication(db.Model):
    name = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True,primary_key = True)
    password = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50),unique=True)
    credit_card = db.Column(db.String(50))
    
class ItemsApplication(db.Model):
    title = db.Column(db.String(50),unique=True,primary_key = True)
    keywords = db.Column(db.String(50))
    time = db.Column(db.String(50))
    priceRange = db.Column(db.String(50))

class Users(db.Model,UserMixin):
    name = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True,primary_key=True)
    password = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50),unique=True)
    credit_card = db.Column(db.String(50))
    
class Reports(db.Model,UserMixin):
    title = db.Column(db.String(50),primary_key=True)
    description = db.Column(db.String(50))
    
class Complaints(db.Model,UserMixin):
    user = db.Column(db.String(50),primary_key=True)
    description = db.Column(db.String(50))

class ItemsListed(db.Model):
    title = db.Column(db.String(50),unique=True,primary_key = True)
    keywords = db.Column(db.String(50))
    time = db.Column(db.DateTime,default=datetime.utcnow)
    priceRange = db.Column(db.String(50))
    picName = db.Column(db.Text)
    img = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    
