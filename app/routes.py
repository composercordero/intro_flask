from app import app
from flask import render_template, redirect, url_for
from app.forms import SignUpForm


# Add a route
@app.route('/')
def index():
    numbers = [1,2,3,4,5]
    return render_template('index.html', first_name = 'Carlos', numbers = numbers)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Get the data from the form
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(first_name, last_name, username, email, password)

        # redirect back to the home page    
        return redirect(url_for('index'))
    
    return render_template('signup.html', form=form)
