from flask import Flask

# Create an instance of the flask class
app = Flask(__name__)

# Configure our app with a secret key
app.config['SECRET_KEY'] = 'random_token'

# import all of the routes from the routes files into the current package

from app import routes

# Must be imported at the bottom of the file