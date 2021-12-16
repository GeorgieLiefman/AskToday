from main import db


class Comment(db.Model):
    __tablename__ = "comments"

        # These attributes specify what columns the table should have
    comment_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    commentor_id = db.Column(db.Integer, db.ForeignKey('flasklogin-users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))