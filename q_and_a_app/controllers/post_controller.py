from flask import Blueprint, jsonify, request, render_template
from main import db
from models.posts import Post
from schemas.post_schema import post_schema, posts_schema


posts = Blueprint('posts', __name__)


# Homepage
@posts.route('/home/', methods=["PUT", "PATCH"])
def home_page():
    return "This page will be a homepage for users to signup and login."


# Get the feed
@posts.route('/feed/', methods=["GET"])
def get_feed():
    data = {
        "page_title": "Feed",
        "posts": posts_schema.dump(Post.query.all())
    }
    return render_template("feed.html", page_data = data)


#Submit a post
@posts.route('/feed/', methods=["POST"])
def submit_post():
    new_post = post_schema.load(request.form)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(post_schema.dump(new_post))

# Get a specific post
@posts.route('/feed/<int:id>/', methods=["GET"])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post_schema.dump(post))

# Edit a specific post
@posts.route('/feed/<int:id>/', methods=["PUT", "PATCH"])
def update_post(id):
    post = Post.query.filter_by(post_id=id)
    updated_fields = post_schema.dump(request.json)
    if updated_fields:
        post.update(updated_fields)
        db.session.commit()
    return jsonify(post_schema.dump(post.first()))


# Edit a specific post
@posts.route('/feed/<int:id>/', methods=["DELETE"])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify(post_schema.dump(post))