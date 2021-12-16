from flask import Blueprint, request, render_template, redirect, url_for, current_app, abort, flash
from main import db
from models.posts import Post
from models.comments import Comment
from schemas.comment_schema import comment_schema, comments_schema
import boto3
from flask_login import login_required, current_user

comments = Blueprint('comments', __name__)

@comments.route("/feed/<int:id>/create_comment/", methods=["POST"])
@login_required
def create_comment(id):
    text = request.form.get('text')

    if not text:
        flash('Comment cannot be empty.', category='error')

    else:
        post = Post.query.get_or_404(id)
        if post:
            comment = Comment(text = text, commentor_id = current_user.id, post_id = id)
            new_comment = comment_schema.load(request.form)
            db.session.add(new_comment)
            db.session.commit()

        else:
            flash('Post does not exist', category = 'error')


    return redirect(url_for('posts.get_feed'))