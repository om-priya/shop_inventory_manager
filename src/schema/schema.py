from pydantic import BaseModel, Field, ValidationError, field_validator

from utils.user_validator import password_validator


class LoginSchema(BaseModel):
    email: str = Field(pattern=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}")
    password: str = Field(min_length=6, max_length=20)

    @field_validator("password")
    def validate_password(cls, value):
        if not password_validator(value):
            raise ValidationError("Password is not valid")
        return value


class SignUpSchema(BaseModel):
    name: str = Field(pattern=r"^[A-Za-z]+([\ A-Za-z]+)*")
    email: str = Field(pattern=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}")
    phone: str = Field(pattern=r"^[0-9]{10}$")
    gender: str = Field(pattern=r"[M,F]{1}$")
    role: str = Field(pattern=r"\bowner\b")
    shop_name: str = Field(pattern=r"^[A-Za-z]+([\ A-Za-z]+)*")
    password: str = Field(min_length=6, max_length=20)

    @field_validator("password")
    def validate_password(cls, value):
        if not password_validator(value):
            raise ValidationError("Password is not valid")
        return value


class ProductSchema(BaseModel):
    name: str = Field(pattern=r"^[A-Za-z]+([\ A-Za-z]+)*")
    price: str = Field(pattern=r"[0-9]*[.][0-9]*")
    quantity: str = Field(pattern=r"\d+")
    discount: str = Field(pattern=r"[0-9]*[.][0-9]*")
    category: str = Field(pattern=r"^[A-Za-z]+([\ A-Za-z]+)*")


class GetSalesSchema(BaseModel):
    year: str = Field(pattern=r"[0-9]{4}$")


class ProductIdSchema(BaseModel):
    product_id: str = Field(pattern=r"^[A-Za-z0-9]{8}$")
