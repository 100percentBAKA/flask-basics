import re 
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db 

auth = Blueprint('auth', __name__)
##? setting up a blueprint from our auth in Flask application

def is_valid_email(email):
    
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    match = re.match(email_regex, email)
    return bool(match)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_values = {}
    ##? initializing an empty dict
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        login_values = {
            'email': email,
        }

        user = User.query.filter_by(email=email).first()
        if user:
            # if check_password_hash(user.password, password):
            ##! hashing not working
            if user.password == password:
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                ##? logs in and remembers the user (until the server is running)
                return redirect(url_for("views.home"))
            else:
                flash('Incorrect Password', category='input_error')
        else:
            flash('User email is not registered yet', category="input_error")

    return render_template("login.html", **login_values, user=current_user)

@auth.route('/logout')
@login_required
##? until and unless the user is logged in, log out must not be displayed
def logout():
    logout_user()
    ##? logs the user out 
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    form_values = {}
    ##? Initialize empty dictionary 

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        form_values = {
            'email': email,
            'firstName': first_name
        }

        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists', category='input_error')
        elif not is_valid_email(email):
            flash('Invalid Email entry found', category = 'input_error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='input_error')
            form_values['password1'] = ''
            form_values['password2'] = ''
        else:
            # hashed_password = generate_password_hash(password1, method='sha256')
            ##! hashing not working 
            new_user = User(email=email, first_name=first_name, password=password1)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created Successfully', category='success')
            return redirect(url_for("views.home"))
            ##? url_for(<blueprint_name>, <function_name>)

    return render_template("signup.html", **form_values, user=current_user)
    ##? **form_values --> dictionary unpacking 