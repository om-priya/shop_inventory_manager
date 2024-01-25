from database.database_connector import DatabaseConnection
from config.user_query import UserQuery
from utils.encryption import *
from users.user import ShopOwner
import logging


def check_login(email, password):
    with DatabaseConnection("store.db") as connection:
        cursor = connection.cursor()
        params = (email,)
        cursor.execute(UserQuery.LOGIN_QUERY, params)
        user_info = cursor.fetchone()
        # decrypting the db password
        db_password = decrypt_password(user_info[0])

    # Converting the entered_pass to bytes and then comparing
    byte_enter_pass = bytes(password, "utf-8")
    if byte_enter_pass == db_password:
        return True, user_info[1]
    logger.info("Unsuccessfull Login")
    return False, "Not Valid"


def sign_up(owner_object):
    new_owner = ShopOwner(owner_object)
    new_owner.save_user()
