from flask import Blueprint

views = Blueprint('views', __name__)
##? setting up a blueprint from our views in Flask application

@views.route('/')
def home():
    return "<h1>Testing</h1>"