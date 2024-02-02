import shortuuid

from database.database_connector import DatabaseConnection
import logging
from config.user_query import UserQuery
from config.prompt_message import PromptMessage
from config.product_query import DatabaseConfig


logger = logging.getLogger(__name__)


# Human Class
class Human:
    try:

        def __init__(self, name, email, phone, gender):
            self.name = name
            self.email = email
            self.phone = phone
            self.gender = gender

    except Exception:
        print(Exception.__name__)
        print(PromptMessage.EXCEPTION_PROMPT_MESSAGE)


# Owner Class inheriting human
class ShopOwner(Human):
    def __init__(self, owner_obj):
        super().__init__(
            owner_obj["name"],
            owner_obj["email"],
            owner_obj["phone"],
            owner_obj["gender"],
        )
        self.role = owner_obj["role"]
        self.shop_name = owner_obj["shop_name"]
        self.password = owner_obj["password"]

    # saving users to user-file
    def save_user(self):
        with DatabaseConnection(DatabaseConfig.DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(UserQuery.CREATE_USER_TABLE)
            data_tuple = (
                shortuuid.ShortUUID().random(length=8),
                self.name,
                self.email,
                self.phone,
                self.gender,
                self.role,
                self.shop_name,
                self.password,
            )
            cursor.execute(UserQuery.INSERT_USER_DATA, data_tuple)
