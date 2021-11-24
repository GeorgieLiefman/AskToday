from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from main import db
from models.posts import Post
from schemas.post_schema import post_schema, posts_schema


posts = Blueprint('posts', __name__)


# Homepage
@posts.route('/', methods=["GET"])
def home_page():
    data = {
        "page_title": "Homepage"
    }
    return render_template("homepage.html", page_data=data)


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
    return redirect(url_for("posts.get_feed"))

# Get a specific post
@posts.route('/feed/<int:id>/', methods=["GET"])
def get_post(id):
    post = Post.query.get_or_404(id)
    data = {
        "page_title": "Post Detail",
        "post": post_schema.dump(post),
        "image": f"static/{post.image_filename}"
    }
    return render_template("post_detail.html", page_data = data)

# Edit a specific post
@posts.route('/feed/<int:id>/', methods=["POST"])
def update_post(id):
    post = Post.query.filter_by(post_id=id)
    updated_fields = post_schema.dump(request.form)
    if updated_fields:
        post.update(updated_fields)
        db.session.commit()

    data = {
        "page_title": "Post Detail",
        "post": post_schema.dump(post.first())
    }
    return render_template("post_detail.html", page_data = data)


# Delete a specific post
@posts.route('/feed/<int:id>/delete/', methods=["POST"])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("posts.get_feed"))