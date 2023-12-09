from flask import Blueprint

auth = Blueprint('auth', __name__)
##? setting up a blueprint from our auth in Flask application

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup')
def signup():
    return "<p>Sign Up</p>"