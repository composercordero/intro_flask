from flask import Flask

# Create an instance of the flask class
app = Flask(__name__)

# Add a route
@app.route("/")
def hello_world():
    return "<p>Hello, World!<p/>"

@app.route('/new')
def new():
    return 'This is a new route!'