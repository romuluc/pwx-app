# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_restless import APIManager

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.app_context().push()

    migrate = Migrate(app, db)

    from app import models

    # temporary route
    @app.route('/')
    def home():
        return 'PWX App!'

    # admin initialization
    admin = Admin(app)
    admin.add_view(ModelView(models.Category, db.session))
    admin.add_view(ModelView(models.Product, db.session))

    #api initialization
    manager = APIManager(app, flask_sqlalchemy_db=db)
    includes_cat = ['id', 'name', 'is_active', 'products', 'products.name']
    manager.create_api(models.Category, include_columns=includes_cat, methods=['GET', 'POST', 'PUT', 'DELETE'])
    includes_prod = ['id', 'name', 'price', 'category', 'category.name']
    manager.create_api(models.Product, include_columns=includes_prod,  methods=['GET', 'POST', 'PUT', 'DELETE'])

    return app

