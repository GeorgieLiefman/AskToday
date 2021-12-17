from flask import Blueprint, request, render_template, redirect, url_for, current_app, abort, flash
from main import db
from models.posts import Post
from models.comments import Comment
from schemas.comment_schema import comment_schema, comments_schema
from schemas.post_schema import posts_schema, post_schema
import boto3
from flask_login import login_required, current_user

comments = Blueprint('comments', __name__)

# Create a comment
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
            db.session.add(comment)
            db.session.commit()

        else:
            flash('Post does not exist', category = 'error')

    return redirect(url_for('posts.get_feed'))













""" @comments.route("/feed/<int:id>/create_comment/", methods=["POST"])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash('Comment does not exist.', category='error')
    elif current_user.id != comment.commentor_id and current_user.id != comment.post.author:
        flash('You do not have permission to delte this comment', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()
        
        
    return redirect(url_for('posts.get_feed')) """


""" 
@comments.route("/feed/<int:id>/create_comment/", methods=["POST"])
@login_required
def create_comment(id):
    post = Post.query.filter_by(post_id=id)
    text = comment_schema.dump(request.form)

    if text:
        text.dump(text)
        db.session.commit()

    data = {
        "page_title": "Post Detail",
        "post": post_schema.dump(post),
        "comment": comment_schema.dump(text.first())
    }
    return render_template("post_detail.html", page_data = data)
 """


