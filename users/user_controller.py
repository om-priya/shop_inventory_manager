import maskpass
from users.user import ShopOwner
import validators.user_validator
from database import DatabaseConnection
from exception_handler.sql_exception_handler import exception_handler
from encryption.encryption import *
from loggers.general_logger import GeneralLogger
from query.user_query import UserQuery

# ***** To Generate Key For Encryption *****
# key = Fernet.generate_key()
# with open("encrypt_key.key", "wb") as file_key:
#     file_key.write(key)


# Check For Login Users
@exception_handler
def check_login():
    email = input("Enter Your Email: ")
    entered_password = maskpass.advpass()

    with DatabaseConnection("users.db") as connection:
        cursor = connection.cursor()
        params = (email,)
        cursor.execute(UserQuery.LOGIN_QUERY, params)
        user_info = cursor.fetchone()
        # decrypting the db password
        db_password = decrypt_password(user_info[0])
        user_id = user_info[1]

    # Converting the entered_pass to bytes and then comparing
    byte_enter_pass = bytes(entered_password, "utf-8")
    if byte_enter_pass == db_password:
        return [True, user_id]
    GeneralLogger.info("Unsuccessfull Login", "users.log")
    return [False, ""]


# Creating Owner Object and encrypting password and storing it in users.db
@exception_handler
def signup():
    owner_object = {}
    owner_object["name"] = validators.user_validator.name_validator().lower()
    owner_object["email"] = validators.user_validator.email_validator().lower()
    owner_object["phone"] = validators.user_validator.phone_validator()
    owner_object["gender"] = validators.user_validator.gender_validator().upper()
    owner_object["role"] = "owner"
    owner_object["shop_name"] = validators.user_validator.shop_validator().lower()
    owner_object["password"] = encrypt_password(
        validators.user_validator.password_validator()
    )

    new_owner = ShopOwner(owner_object)
    new_owner.save_user()
    print("Owner Created SuccessFully You Can Log In Now")
