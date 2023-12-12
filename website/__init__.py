from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
##? creating an SQLAlchemy object
DB_NAME = 'database.db'
login_manager = LoginManager()
##? creating LoginManager instance/object

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '86d5e797-60db-4ac2-bc17-668103f68be3'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)
    ##? initializing the db

    from .views import views
    from .auth import auth
    ##? importing the blueprints

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    ##? setting up the blueprints

    from .models import User, Note
    ##? importing ORMs before creating the DB
    create_database(app)

    login_manager.login_view = 'auth.login'
    ##? where to redirect if user not logged in
    login_manager.init_app(app)
    ##? initializing the login manager

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database created successfully")