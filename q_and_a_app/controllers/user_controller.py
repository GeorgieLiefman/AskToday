from flask import Blueprint, request, render_template, redirect, url_for, abort
from main import db, lm
from models.users import User
from schemas.user_schema import user_schema, users_schema, user_update_schema
from flask_login import login_user, logout_user, login_required, current_user
from marshmallow import ValidationError

@lm.user_loader
def load_user(user):
    return User.query(user)

@lm.unauthorized_handler
def unauthorized():
    return redirect('/users/login/')

users = Blueprint("users", __name__)

# Displays index of all users
@users.route("/users/", methods=["GET"])
def get_user():
    data = {
        "page_title": "User Index",
        "users": users_schema.dump(User.query.all())
    }
    return render_template("user_index.html", page_data=data)