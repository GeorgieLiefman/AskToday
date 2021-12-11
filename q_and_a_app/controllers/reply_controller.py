from main import db
from flask import Blueprint, request, render_template, redirect, url_for, current_app, abort
from models.replies import Reply
from models.posts import Post
from schemas.reply_schema import replies_schema, reply_schema
from flask_login import login_required, current_user

replies = Blueprint('replies', __name__)

@replies.route('/feed/<int:id>/', methods=["POST"])
@login_required
def submit_reply(id):
   pass



from flask import Blueprint, request, redirect, abort, url_for, current_app 
from pathlib import Path
from models.posts import Post
import boto3

post_images = Blueprint('post_images', __name__)

@post_images.route("/feed/<int:id>/image/", methods=["POST"])
def update_image(id):

    post = Post.query.get_or_404(id)

    if "image" in request.files:

        image = request.files["image"]

        if Path(image.filename).suffix != ".png":
            return abort(404, description="Invalid file type")

        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        bucket.upload_fileobj(image, post.image_filename)

        return redirect(url_for("posts.get_feed", id=id))

    return abort(400, description="No image")