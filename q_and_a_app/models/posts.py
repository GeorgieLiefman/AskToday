from main import db
from models.users import User
from models.comments import Comment

following = db.Table(
        'following',
        db.Column('user_id', db.Integer, db.ForeignKey('flasklogin-users.id'), primary_key=True),
        db.Column('post_id', db.Integer, db.ForeignKey('posts.post_id'), primary_key=True)
)

class Post(db.Model):
        __tablename__ = "posts"

        post_id = db.Column(db.Integer, primary_key=True)
        post_title = db.Column(db.String(200), nullable=False)
        post_content = db.Column(db.String(2000), nullable=True, server_default="No description provided...")
        ranked_importance = db.Column(db.Integer, nullable=False, server_default="0")

        comments = db.relationship(Comment, backref='post')
        creator_id = db.Column(db.Integer, db.ForeignKey('flasklogin-users.id'))

        followers = db.relationship(
                User,
                secondary = following,
                backref = db.backref('followed_posts'),
                lazy="joined"
        )

        @property
        def image_filename(self):
                return f"post_images/{self.post_id}.png"

        
