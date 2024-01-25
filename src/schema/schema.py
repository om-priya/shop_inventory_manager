from marshmallow import fields, Schema, validate


class LoginSchema(Schema):
    email = fields.String(
        required=True,
        validate=validate.Regexp("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}"),
    )
    password = fields.String(
        required=True,
        validate=validate.Regexp(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        ),
    )


class SignUpSchema(Schema):
    name = fields.String(
        required=True, validate=validate.Regexp("^[A-Za-z]+([\ A-Za-z]+)*")
    )
    email = fields.String(
        required=True,
        validate=validate.Regexp("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}"),
    )
    phone = fields.String(required=True, validate=validate.Regexp("^[0-9]{10}$"))
    gender = fields.String(required=True, validate=validate.Regexp("[M,F]{1}$"))
    role = fields.String(required=True, validate=validate.Regexp("\bowner\b"))
    shop_name = fields.String(
        required=True, validate=validate.Regexp("^[A-Za-z]+([\ A-Za-z]+)*")
    )
    password = fields.String(
        required=True,
        validate=validate.Regexp(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        ),
    )

class ProductSchema(Schema):
    name = fields.String(
        required=True, validate=validate.Regexp("^[A-Za-z]+([\ A-Za-z]+)*")
    )
    price = fields.String(
        required=True, validate=validate.Regexp("[0-9]*[.][0-9]*")
    )
    quantity = fields.String(
        required=True, validate=validate.Regexp("\d+")
    )
    discount = fields.String(
        required=True, validate=validate.Regexp("[0-9]*[.][0-9]*")
    )
    category = fields.String(
        required=True, validate=validate.Regexp("^[A-Za-z]+([\ A-Za-z]+)*")
    )

class GetSalesSchema(Schema):
    year = fields.Int(required=True, validate=validate.Regexp("[0-9]{4}$"))

class ProductIdSchema(Schema):
    product_id = fields.String(required=True, validate=validate.Regexp("^[A-Za-z0-9]{8}$"))