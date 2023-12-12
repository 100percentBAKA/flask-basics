from . import db
##? import db from the current package ( import from __init__.py )
from flask_login import UserMixin
##? UserMixin is a class provided by the Flask-Login extension, which is commonly used for managing user authentication in Flask applications. 
from sqlalchemy.sql import func
##?  provides a collection of SQL functions that can be used in SQLAlchemy queries


class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    ##? func.now() --> current time, func.current_date()  --> current date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class User(db.Model, UserMixin):
    ##? By Convention, class names begin with 'Capital Letter' but in sql, the class names are lowercased table names
    ##? For example: 'User' class is converted into 'user' table
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True)
    ##? string of length 150 and no user can have same email 
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    notes = db.relationship('Note')
    ##? one 'User' can have many 'Notes' representing one to many rel
    ##? every time a user creates a note, that note id is added into 'notes'


