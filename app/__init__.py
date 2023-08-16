from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Create an instance of the flask class
app = Flask(__name__)

# Configure our app with a secret key
app.config.from_object(Config)

# Create an instance of SQLAlchemy to represent the database
db = SQLAlchemy(app)

# Create an instance of Migrate to handle the database migrations of our flask app
migrate = Migrate(app, db)

# Create an instance of LoginManager to handle authentication
login = LoginManager(app)

# import all of the routes from the routes files into the current package

from app import routes, models

# Must be imported at the bottom of the file

# Packages used today:
# pip install flask-migrate flask-wtf flask-sqlalchemy python-dotenv
# The flask database commands are:
# flask db init
# This initializes a migrations  folder which will store all your database metadata
# flask db migrate
# This command detects changes made to your database and makes a migration (creates a new version of your db changes)
# flask db upgrade
# This command will apply your changes to the database.