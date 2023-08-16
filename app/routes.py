from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm, PostForm
from app.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user


# Add a route
@app.route('/')
def index():
    posts = db.session.execute(db.select(Post).order_by(Post.date_created.desc())).scalars().all()
    return render_template('index.html', posts=posts)

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
            flash('A user with that username already exists')
            return redirect(url_for('signup'))

        # Create a new instance of the User class with data from form
        new_user = User(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
        # Add the new_user object to the database
        db.session.add(new_user)
        db.session.commit()
        flash(f'{new_user.username} has been created')
        # Log the user in
        login_user(new_user)

        # redirect back to the home page    
        return redirect(url_for('index'))
    
    return render_template('signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        #Query the User table for a user with that username
        user = db.session.execute(db.select(User).where(User.username==username)).scalar()
        # If we have a user AND the password is correct for that user
        if user is not None and user.check_password(password):
            # Log the user in via login_user function
            login_user(user)
            flash("You have successfully logged in")
            return redirect(url_for('index'))
        else:
            flash('Invalid username and/or password')
            return redirect(url_for('login'))
        
    return render_template('login.html', form=form)

@app.route('/create', methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        # Get the data from the form

        title = form.title.data
        body = form.body.data
        image_url = form.image_url.data or None

        # Create a new post instance

        new_post = Post(title=title, body=body, image_url=image_url, user_id = current_user.id)
        # Add that object to the database
        db.session.add(new_post)
        db.session.commit()

        flash(f"{new_post.title} has been created")
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have successfully logged out")
    return redirect(url_for('index'))

