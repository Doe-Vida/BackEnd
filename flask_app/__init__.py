from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI')

app = Flask(__name__) # creates a flask app with the name of the file as a parameter
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # configure database path
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SECRET_KEY'] = "chave_secreta"
db = SQLAlchemy(app) # initialize sqlalchemy object
migrate = Migrate(app, db)

from flask_app import routes







