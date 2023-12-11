import re 
from flask import Blueprint, render_template, request, flash 

auth = Blueprint('auth', __name__)
##? setting up a blueprint from our auth in Flask application

def is_valid_email(email):
    
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    match = re.match(email_regex, email)
    return bool(match)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", is_login = True)

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

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

        if not is_valid_email(email):
            flash('Invalid Email entry found', category = 'input_error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='input_error')
            form_values['password1'] = ''
            form_values['password2'] = ''
        else:
            flash('Account Created Successfully', category='success')

    return render_template("signup.html", **form_values)
    ##? **form_values --> dictionary unpacking 