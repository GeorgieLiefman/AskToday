from main import db

class Post(db.Model):
        __tablename__ = "posts"
        post_id = db.Column(db.Integer, primary_key=True)
        post_title = db.Column(db.String(80), unique=True, nullable=False)
        post_content = db.Column(db.String(200), server_default="No description provided...")

        
