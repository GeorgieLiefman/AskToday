from marshmallow import validate
from main import ma 
from models.posts import Post
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length, Range

class PostSchema(ma.SQLAlchemyAutoSchema):
    post_id = auto_field(dump_only = True)
    post_title = auto_field(required = True, validate = Length(min = 1))
    post_content = auto_field(validate = Length(min = 1))
    likes = auto_field(required = False, validate = Range(0, 10000))
    creator = ma.Nested("UserSchema")

    class Meta:
        model = Post
        load_instance = True

post_schema = PostSchema()
posts_schema = PostSchema(many = True)