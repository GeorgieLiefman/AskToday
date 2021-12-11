from main import ma 
from models.replies import Reply
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length, Range

class ReplySchema(ma.SQLAlchemyAutoSchema):
    reply_id = auto_field(dump_only = True)
    reply_content = auto_field(validate = Length(min = 1))
    
    class Meta:
        model = Reply
        load_instance = True

reply_schema = ReplySchema()
replies_schema = ReplySchema(many = True)
reply_update_schema = ReplySchema(partial = True)