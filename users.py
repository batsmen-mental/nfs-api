from flask import Blueprint
users = Blueprint("users", __name__)

@users.route('/')
def users_index():
    return ('{"userid":"123","username":"testuser","first_name":"Jim","last_name":"Smith"}',200)