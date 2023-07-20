from flask import Blueprint
from app.models.User import User
from app.blueprints.user.UserSchema import UserSchema

user = Blueprint('user', __name__, url_prefix="/users")


@user.get("/")
def get_all_users():
    all_users = User.query.all()
    return UserSchema().dump(all_users, many=True)


@user.post("/")
def create_user():
    user = User(name="sanjeev", email="bhusalsanjeev23@gmail.com")
    user.save()
    print(user)
    return ""
