from jose import jwt, JWTError
from fastapi import HTTPException


class JwtHandler:
    @staticmethod
    def generate_token(claims):
        token = jwt.encode(claims, "secretkey", algorithm="HS256")
        return token

    @staticmethod
    def decode_token(token):
        try:
            return jwt.decode(token, "secretkey")
        except JWTError:
            raise HTTPException(
                status_code=401,
                detail={"success": False, "message": "Invalid or missing Token"},
            )
