from main import ma 
from models.comments import Comment
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length, Range

class CommentSchema(ma.SQLAlchemyAutoSchema):
    comment_id = auto_field(dump_only = True)
    text = auto_field(required = True, validate = Length(min = 1))
   

    class Meta:
        model = Comment
        load_instance = True

comment_schema = CommentSchema()
comments_schema = CommentSchema(many = True)


