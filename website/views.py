from flask import Blueprint, render_template

views = Blueprint('views', __name__)
##? setting up a blueprint from our views in Flask application

@views.route('/')
def home():
    return render_template("home.html")