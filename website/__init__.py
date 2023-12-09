from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '86d5e797-60db-4ac2-bc17-668103f68be3'

    from .views import views
    from .auth import auth
    ##? importing the blueprints

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    ##? setting up the blueprints

    return app