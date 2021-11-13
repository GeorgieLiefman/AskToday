from marshmallow import validate
from main import ma 
from models.posts import Post
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length

class PostSchema(ma.SQLAlchemyAutoSchema):
    post_id = auto_field(dump_only = True)
    post_title = auto_field(required = True, validate = Length(min = 1))

    class Meta:
        model = Post
        load_instance = True

post_schema = PostSchema()
posts_schema = PostSchema(many = True)