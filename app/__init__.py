from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Create an instance of the flask class
app = Flask(__name__)

# Configure our app with a secret key
app.config.from_object(Config)

# Create an instance of SQLAlchemy to represent the database

db = SQLAlchemy(app)

# Create an instance of Migrate to handle the database migrations of our flask app

migrate = Migrate(app, db)


# import all of the routes from the routes files into the current package

from app import routes

# Must be imported at the bottom of the file