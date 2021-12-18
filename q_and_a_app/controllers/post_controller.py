from flask import Blueprint, request, render_template, redirect, url_for, current_app, abort
from main import db
from models.posts import Post
from schemas.post_schema import post_schema, posts_schema
import boto3
from flask_login import login_required, current_user


posts = Blueprint('posts', __name__)


# Homepage
@posts.route('/', methods=["GET"])
def home_page():
    data = {
        "page_title": "AskToday"
    }
    return render_template("homepage.html", page_data=data)


# Terms of Service page
@posts.route('/terms/', methods=["GET"])
def terms_of_service():
    data = {
        "page_title": "Terms of Service"
    }
    return render_template("terms_of_use.html", page_data=data)


# Get the feed
@posts.route('/feed/', methods=["GET"])
def get_feed():
    data = {
        "page_title": "Feed",
        "posts": posts_schema.dump(Post.query.order_by(Post.creator_id).all())
    }
    return render_template("feed.html", page_data = data)


#Submit a post
@posts.route('/feed/', methods=["POST"])
@login_required
def submit_post():
    new_post = post_schema.load(request.form)
    new_post.creator = current_user
    db.session.add(new_post)
    db.session.commit()
    print(post_schema.dump(new_post))
    return redirect(url_for("posts.get_feed"))



# Get a specific post
@posts.route('/feed/<int:id>/', methods=["GET"])
def get_post(id):
    post = Post.query.get_or_404(id)

    s3_client=boto3.client("s3")
    bucket_name=current_app.config["AWS_S3_BUCKET"]
    image_url = s3_client.generate_presigned_url(
        'get_object',
        Params={
            "Bucket": bucket_name,
            "Key": post.image_filename
        },
        ExpiresIn=100
    )

    data = {
        "page_title": "Post Detail",
        "post": post_schema.dump(post),
        "image": image_url
    }
    print(data)
    return render_template("post_detail.html", page_data = data)









# Edit a specific post
@posts.route('/feed/<int:id>/', methods=["POST"])
@login_required
def update_post(id):
    post = Post.query.filter_by(post_id=id)

    if current_user.id != post.first().creator_id:
        abort(403, "You do not have permission to edit this post!")

    updated_fields = post_schema.dump(request.form)
    if updated_fields:
        post.update(updated_fields)
        db.session.commit()

    data = {
        "page_title": "Post Detail",
        "post": post_schema.dump(post.first())
    }
    return render_template("post_detail.html", page_data = data)


# follow a post
@posts.route("/feed/<int:id>/follow/", methods=["Post"])
@login_required
def follow_post(id):
    post = Post.query.get_or_404(id)
    post.followers.append(current_user)
    db.session.commit()
    return redirect(url_for('users.user_detail'))

# Unfollow a post
@posts.route("/feed/<int:id>/unfollow/", methods=["Post"])
@login_required
def unfollow_post(id):
    post = Post.query.get_or_404(id)
    post.followers.remove(current_user)
    db.session.commit()
    return redirect(url_for('users.user_detail'))


# Delete a specific post
@posts.route('/feed/<int:id>/delete/', methods=["POST"])
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)

    if current_user.id != post.creator_id:
        abort(403, "You do not have permission to delete this post!")

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("posts.get_feed"))