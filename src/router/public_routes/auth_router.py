from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from datetime import datetime, timedelta, timezone
from controller import auth_controller
from schema.schema import LoginSchema, SignUpSchema
import sqlite3
from utils.jwt_token import JwtHandler

auth_router = APIRouter(prefix="/api/v1")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login", auto_error=False)


async def get_user_id_from_token(token: Annotated[str, Depends(oauth2_scheme)]):
    if not token:
        raise HTTPException(
            status_code=401,
            detail={"success": False, "message": "Token is not provided"},
        )
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
            return JSONResponse(
                status_code=404, content={"success": False, "message": "Invalid User"}
            )
        expires_delta = timedelta(minutes=20)
        access_token = JwtHandler.generate_token(
            {
                "admin": True,
                "user_id": user_id,
                "exp": datetime.now(timezone.utc) + expires_delta,
            }
        )
        return JSONResponse(
            status_code=200, content={"success": True, "access_token": access_token}
        )
    except sqlite3.Error:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong in db"},
        )
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something went wrong"},
        )


@auth_router.post("/logout")
async def logout():
    return JSONResponse(
        status_code=200,
        content={"success": True, "message": "Logged Out Successfully"},
    )


@auth_router.post("/signup")
async def signup(user_info: SignUpSchema):
    try:
        owner_data = user_info.model_dump()
        auth_controller.sign_up(owner_data)
        return JSONResponse(
            status_code=201,
            content={"success": True, "message": "User Signed Up Successfully"},
        )
    except sqlite3.Error:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong in db"},
        )
    except Exception:
        JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something went wrong"},
        )
