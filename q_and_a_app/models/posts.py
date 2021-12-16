from main import db
from models.users import User
from models.comments import Comment


# Generic template for a many to many relationship
following = db.Table(
        'following',
        db.Column('user_id', db.Integer, db.ForeignKey('flasklogin-users.id'), primary_key=True),
        db.Column('course_id', db.Integer, db.ForeignKey('posts.post_id'), primary_key=True)
)


class Post(db.Model):
        # The tablename attributes species what the name of the table should exist in the database.
        __tablename__ = "posts"

        # These attributes specify what columns the table should have
        post_id = db.Column(db.Integer, primary_key=True)
        post_title = db.Column(db.String(80), unique=True, nullable=False)
        post_content = db.Column(db.String(500), server_default="No description provided...")
        likes = db.Column(db.Integer, nullable=False, server_default="0")

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

        
