from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from datetime import datetime, timedelta
from time import timezone
from controller import user_controller, auth_controller
from schema.schema import LoginSchema, SignUpSchema
import sqlite3
from utils.jwt_token import JwtHandler

auth_router = APIRouter(prefix="/api/v1")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


async def get_user_id_from_token(token: Annotated[str, Depends(oauth2_scheme)]):
    decoded_data = JwtHandler.decode_token(token)
    return decoded_data["user_id"]


# LoginSchema
@auth_router.post("/login")
async def login(user_info: LoginSchema):
    try:
        valid_user, user_id = auth_controller.check_login(
            user_info.email, user_info.password
        )
        if not valid_user:
            return JSONResponse(status_code=404, content={"message": "Invalid User"})
        expires_delta = timedelta(minutes=20)
        access_token = JwtHandler.generate_token(
            {
                "admin": True,
                "user_id": user_id,
                "exp": datetime.now(timezone.utc) + expires_delta,
            }
        )
        return JSONResponse(status_code=200, content={"access_token": access_token})
    except sqlite3.Error:
        return JSONResponse(
            status_code=500, content={"message": "something went wrong in db"}
        )
    except Exception:
        return JSONResponse(
            status_code=500, content={"message": "Something went wrong"}
        )


@auth_router.post("/logout")
async def logout():
    return {"message": "Log Out SuccessFully"}


@auth_router.post("/signup")
async def signup(user_info: SignUpSchema):
    try:
        owner_data = user_info.model_dump()
        auth_controller.sign_up(owner_data)
    except sqlite3.Error:
        return JSONResponse(
            status_code=500, content={"message": "something went wrong in db"}
        )
    except Exception:
        JSONResponse(status_code=500, content={"message": "Something went wrong"})
