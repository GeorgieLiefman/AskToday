from flask import Blueprint, request, redirect, abort, url_for, current_app
from pathlib import Path
from models.posts import Post
import boto3
from flask_login import login_required, current_user

post_images = Blueprint('post_images', __name__)

# Post an image to a post
@post_images.route("/feed/<int:id>/image/", methods=["POST"])
@login_required
def update_image(id):
    post = Post.query.get_or_404(id)

    if current_user.id != post.creator_id:
        abort(403, "You do not have permission to update the image on this post.")

    if "image" in request.files:
        image = request.files["image"]

        if Path(image.filename).suffix != ".png":
            return abort(404, description="Invalid file type")

        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        bucket.upload_fileobj(image, post.image_filename)
        return redirect(url_for("posts.get_feed", id=id))

    return abort(400, description="No image")