from flask import Blueprint, request, redirect, abort, url_for
from pathlib import Path
from models.posts import Post

post_images = Blueprint('post_images', __name__)

@post_images.route("/feed/<int:id>/image/", methods=["POST"])
def update_image(id):

    post = Post.query.get_or_404(id)

    if "image" in request.files:

        image = request.files["image"]

        if Path(image.filename).suffix != ".png":
            return abort(404, description="Invalid file type")

        image.save(f"static/{post.image_filename}")

        return redirect(url_for("posts.get_feed", id=id))

    return abort(400, description="No image")