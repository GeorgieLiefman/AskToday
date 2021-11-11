from flask import Blueprint, jsonify, request
from main import db
from models.posts import Post

posts = Blueprint('posts', __name__)


# Homepage
@posts.route('/home/', methods=["PUT", "PATCH"])
def home_page():
    return "This page will be a homepage for users to signup and login."


# Get the feed
@posts.route('/feed/', methods=["GET"])
def get_feed():
    feed = Post.query.all()
    return jsonify([post.serialize for post in feed])


#Submit a post
@posts.route('/submit_post/', methods=["POST"])
def submit_post():
    new_post = Post(request.json['post_title'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.serialize)

# Get a specific post
@posts.route('/feed/<int:id>/', methods=["GET"])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.serialize)

# Edit a specific post
@posts.route('/feed/<int:id>/', methods=["PUT", "PATCH"])
def update_post(id):
    post = Post.query.filter_by(post_id=id)
    post.update(dict(post_title=request.json["post_title"]))
    db.session.commit()
    return jsonify(post.first().serialize)


# Edit a specific post
@posts.route('/feed/<int:id>/', methods=["DELETE"])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify(post.serialize)