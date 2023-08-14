from app import app
from flask import render_template

# Add a route
@app.route('/')
def index():
    numbers = [1,2,3,4,5]
    return render_template('index.html', first_name = 'Carlos', numbers = numbers)

@app.route('/new')
def new():
    return 'This is a new modified route!'