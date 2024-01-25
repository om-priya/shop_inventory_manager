from fastapi import APIRouter

from controller import user_controller, auth_controller
from response_class.response_format import SuccessResponse, ErrorResponse
from schema.schema import LoginSchema, SignUpSchema

# blp = Blueprint(
#     "Login-SignUp",
#     __name__,
#     url_prefix="/",
#     description="Login SignUp Operations",
# )

auth_router = APIRouter(prefix="/api/v1")


@auth_router.post("/login")
async def login():
    return {"message": "Log In SuccessFully"}


@auth_router.post("/logout")
async def logout():
    return {"message": "Log Out SuccessFully"}


@auth_router.post("/signup")
async def signup():
    return {"message": "Signed Up SuccessFully"}


# @blp.route("/login")
# class Login(MethodView):
#     @blp.arguments(LoginSchema)
#     def post(self, user_data):
#         valid_user, user_id = auth_controller.check_login(
#             user_data["email"], user_data["password"]
#         )
#         if not valid_user:
#             return {"code": 404, "message": "Invalid User"}
#         access_token = create_access_token(identity={"admin": True, "user_id": user_id})
#         return jsonify(access_token=access_token)


# @blp.route("/logout")
# class LogOut(MethodView):
#     def post(self):
#         pass


# @blp.route("/signup")
# class SignUp(MethodView):
#     @blp.arguments(SignUpSchema)
#     def post(self, owner_data):
#         try:
#             auth_controller.sign_up(owner_data)
#         except Exception:
#             pass
