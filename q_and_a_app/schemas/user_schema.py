from main import ma
from models.users import User
from marshmallow_sqlalchemy import auto_field
from marshmallow import fields, exceptions, validate
from werkzeug.security import generate_password_hash

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field(dump_only = True)
    name = auto_field(required = True, validate = validate.Length(min=1))
    email = auto_field(required = True, validate = validate.Email())
    password = fields.Method(required = True, load_only = True, deserialize = "load_password")
    country = auto_field(required = True, validate = validate.Length(min=1))

    followed_posts = ma.Nested(
        "PostSchema",
        only=("post_id", "post_title")
    )

    liked_comments = ma.Nested(
        "CommentSchema",
        only=("comment_id", "text")
    )

    def load_password(self, password):
        if len(password) > 6:
            return generate_password_hash(password, method="sha256")
        raise exceptions.ValidationError("Password must be at least 6 characters.")

user_schema = UserSchema()
users_schema = UserSchema(many = True)
user_update_schema = UserSchema(partial = True)

