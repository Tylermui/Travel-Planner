from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

 # need to make a html page object, or something like that using AJAX....
class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lat =  db.Column(db.Float)
    lng =  db.Column(db.Float)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    pages = db.relationship('Page')
