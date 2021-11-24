from main import db

class Post(db.Model):
        # The tablename attributes species what the name of the table should exist in the database.
        __tablename__ = "posts"

        # These attributes specify what columns the table should have
        post_id = db.Column(db.Integer, primary_key=True)
        post_title = db.Column(db.String(80), unique=True, nullable=False)
        post_content = db.Column(db.String(500), server_default="No description provided...")
        likes = db.Column(db.Integer, nullable=False, server_default="0")

        @property
        def image_filename(self):
                return f"post_images/{self.post_id}.png"

        
