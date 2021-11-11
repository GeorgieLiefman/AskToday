from operator import pos
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

def create_app():
  
    app = Flask(__name__)

    app.config.from_object("config.app_config")

    db = SQLAlchemy(app)

    class Post(db.Model):
        __tablename__ = "posts"
        post_id = db.Column(db.Integer, primary_key=True)
        post_title = db.Column(db.String(80), unique=True, nullable=False)

        def __init__(self, post_title):
            self.post_title = post_title

        @property
        def serialize(self):
            return {
                "post_id": self.post_id,
                "post_title": self.post_title
            }






    db.create_all()

    # Homepage
    @app.route('/home/', methods=["PUT", "PATCH"])
    def home_page():
        return "This page will be a homepage for users to signup and login."


    # Get the feed
    @app.route('/feed/', methods=["GET"])
    def get_feed():
        feed = Post.query.all()
        return jsonify([post.serialize for post in feed])


    #Submit a post
    @app.route('/submit_post/', methods=["POST"])
    def submit_post():
        new_post = Post(request.json['post_title'])
        db.session.add(new_post)
        db.session.commit()
        return jsonify(new_post.serialize)

    # Get a specific post
    @app.route('/feed/<int:id>/', methods=["GET"])
    def get_post(id):
        post = Post.query.get_or_404(id)
        return jsonify(post.serialize)

    # Edit a specific post
    @app.route('/feed/<int:id>/', methods=["PUT", "PATCH"])
    def update_post(id):
        post = Post.query.filter_by(post_id=id)
        post.update(dict(post_title=request.json["post_title"]))
        db.session.commit()
        return jsonify(post.first().serialize)


    # Edit a specific post
    @app.route('/feed/<int:id>/', methods=["DELETE"])
    def delete_post(id):
        post = Post.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        return jsonify(post.serialize)

    return app
