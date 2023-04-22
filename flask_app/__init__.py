from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config


DATABASE_URI = config('DATABASE_URI')

app = Flask(__name__) # creates a flask app with the name of the file as a parameter
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # configure database path
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app) # initialize sqlalchemy object
migrate = Migrate(app, db)

from flask_app import routes







