from main import ma 
from models.posts import Post
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length, Range

class PostSchema(ma.SQLAlchemyAutoSchema):
    post_id = auto_field(dump_only = True)
    post_title = auto_field(required = True, validate = Length(min = 1))
    post_content = auto_field(required = False)
    ranked_importance = auto_field(required = False, validate = Range(-1, 10))

    creator = ma.Nested(
        "UserSchema",
        only = ("id", "name", "email")
        )
        
    followers = ma.Nested(
        "UserSchema",
        only = ("id", "name", "email"),
        many = True
    )

    comments = ma.Nested(
        "CommentSchema",
        only = ("comment_id", "text", "commentor"),
        many = True
    )

    class Meta:
        model = Post
        load_instance = True

post_schema = PostSchema()
posts_schema = PostSchema(many = True)