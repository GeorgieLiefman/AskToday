from flask import Blueprint, request, redirect, url_for, flash, abort
from main import db
from models.posts import Post
from models.comments import Comment
from schemas.comment_schema import comment_schema, comments_schema
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


# Like a comment
@comments.route("/feed/<int:id>/like_comment/", methods=["POST"])
@login_required
def like_comment(id):
    comment = Comment.query.filter_by(comment_id=id).first()
    comment.likers.append(current_user)
    db.session.commit()
    return redirect(url_for('users.user_detail'))


# Unlike a comment
@comments.route("/feed/<int:id>/unlike_comment/", methods=["POST"])
@login_required
def unlike_comment(id):
    comment = Comment.query.filter_by(comment_id=id).first()
    comment.likers.remove(current_user)
    db.session.commit()
    return redirect(url_for('users.user_detail'))


# Delete a comment
@comments.route('/feed/<int:id>/delete_comment/', methods=["POST"])
@login_required
def delete_post(id):
    comment = Comment.query.filter_by(comment_id=id).first()
    if current_user.id != comment.commentor_id:
        abort(403, "You do not have permission to delete this comment!")
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("posts.get_feed"))
