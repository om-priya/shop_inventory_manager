from flask_jwt_extended import get_jwt
from flask import abort


def check_admin(admin_func):
    def wrapper(*args, **kwargs):
        jwt = get_jwt()
        jwt_sub = jwt.get("sub")
        if not jwt_sub.get("admin"):
            return {"code":404,"message":"Token was not provided"}
        else:
            return admin_func(*args, **kwargs)

    return wrapper
