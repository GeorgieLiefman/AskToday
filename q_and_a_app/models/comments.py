from main import db


class Comment(db.Model):
    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    commentor_id = db.Column(db.Integer, db.ForeignKey('flasklogin-users.id'))

    # one to one realtionship
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), unique = True)