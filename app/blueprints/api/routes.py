from . import api
from app import db
from app.models import Post
from flask import request

@api.route('/posts')
def get_posts():
    posts = db.session.execute(db.select(Post)).scalars().all()
    return [p.to_dict() for p in posts]

@api.route('/posts/<post_id>')
def get_post(post_id):
    post = db.session.get(Post, post_id)
    if post:
        return post.to_dict()
    else:
        return {'error': f'Post with an ID of {post_id} does not exist'}, 404
    
@api.route('/posts', methods=['POST'])
def create_post():
    # Check to see if the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application-type JSON'}
    # Get the data from the request body
    data = request.json

    # Validate incoming data
    required_fields = ['title', 'body']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    
    # Get the data from the body
    title = data.get('title')
    body = data.get('body')
    image_url = data.get('image_url')

    # Create a new Post instance with the data
    new_post = Post(title = title, body = body, image_url = image_url, user_id = 3)

    # add to the database
    db.session.add(new_post)
    db.session.commit()

    return new_post.to_dict(), 201