from app import app, db
from flask import render_template, redirect, url_for
from app.forms import SignUpForm
from app.models import User


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
        
        # Check User table to see if there are any users with username or email
        check_user = db.session.execute(db.select(User).where( (User.username==username) | (User.email==email) )).scalar()
        if check_user:
            print('A user with that username/password already exists')
            return redirect(url_for('signup'))

        # Create a new instance of the User class with data from form
        new_user = User(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
        # Add the new_user object to the database
        db.session.add(new_user)
        db.session.commit()
        # redirect back to the home page    
        return redirect(url_for('index'))
    
    return render_template('signup.html', form=form)
