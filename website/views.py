from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)
##? setting up a blueprint from our views in Flask application

@views.route('/')
@login_required
##? cannot redirect/return to the home page unless and until the user is logged in
def home():
    return render_template("home.html", user=current_user)