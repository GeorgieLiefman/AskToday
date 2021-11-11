from main import db

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