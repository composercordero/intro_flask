from app import app

# Add a route
@app.route("/")
def hello_world():
    return "<p>Hello, World!<p/>"

@app.route('/new')
def new():
    return 'This is a new modified route!'