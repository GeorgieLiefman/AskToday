from main import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from models.comments import Comment

class User(UserMixin, db.Model):
    __tablename__ = "flasklogin-users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(40), unique = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    #is_admin = db.Column(db.Boolean(), nullable = False, server_default = "False")

    posts = db.relationship(
        'Post', 
        backref="creator" ,
        lazy="joined"
    )

    comments = db.relationship(Comment, backref='user')
    # To access the list of posts created by Georgie, we call Georgie.posts
    # = [<Post 1>, <Post 2>, ...]

    # To access the creater of post_1, we call post_1.creator
    # = <User Georgie>

    def check_password(self, password):
        # Check's if the hash of the user's password is correct
        return check_password_hash(self.password, password)