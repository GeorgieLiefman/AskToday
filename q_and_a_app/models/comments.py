from main import db
from models.users import User

# Many-to-many relationship
liked_comments = db.Table(
        'liked',
        db.Column('user_id', db.Integer, db.ForeignKey('flasklogin-users.id'), primary_key=True),
        db.Column('comment_id', db.Integer, db.ForeignKey('comments.comment_id'), primary_key=True)
)


class Comment(db.Model):
    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    commentor_id = db.Column(db.Integer, db.ForeignKey('flasklogin-users.id'))

    # one to one realtionship
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), unique = True)


    likers = db.relationship(
                User,
                secondary = liked_comments,
                backref = db.backref('liked_comments'),
                lazy="joined"
        )