from main import ma 
from models.posts import Post
from marshmallow_sqlalchemy import auto_field, load_instance_mixin

class PostSchema(ma.SQLAlchemyAutoSchema):
    post_id = auto_field(dump_only = True)

    class Meta:
        model = Post
        load_instance = True

post_schema = PostSchema()
posts_schema = PostSchema(many = True)