from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS
import os

# Here is the where we configure our application, initialize objects like database and the flask_app itself

app = Flask(__name__) # creates a flask app with the name of the file as a parameter
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://doevida_user:SaNBGSFEl7mdH4NkatCYGCBvDS8Ucy87@dpg-chp4ph2k728ivvrq1o90-a.oregon-postgres.render.com/doevida' #os.environ.get("DATABASE_URI")
app.config["JWT_SECRET_KEY"] = 'zGEHihvhaCxwaOnLfsPB6isU96YQzbV4' #os.environ.get("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30) 
jwt__ = JWTManager(app)
db = SQLAlchemy(app) # initialize sqlalchemy object
migrate = Migrate(app, db)

from flask_app import routes