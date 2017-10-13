import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'pwxsecret'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pwx_app.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False