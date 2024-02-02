import shortuuid
import logging
from datetime import datetime
from database.database_connector import DatabaseConnection
from config.product_query import ProductQuery
from config.prompt_message import PromptMessage
from config.product_query import DatabaseConfig

logger = logging.getLogger(__name__)


class Products:
    try:

        def __init__(self, product_obj):
            self.id = shortuuid.ShortUUID().random(length=8)
            self.name = product_obj["name"]
            self.price = product_obj["price"]
            self.quantity = product_obj["quantity"]
            self.discount = product_obj["discount"]
            self.category = product_obj["category"]
            self.user_id = product_obj["user_id"]

        # Saving Product to File
        def save_product(self):
            with DatabaseConnection(DatabaseConfig.DB_PATH) as connection:
                cursor = connection.cursor()
                cursor.execute(ProductQuery.CREATE_PRODUCT_TABLE)
                query = ProductQuery.INSERT_PRODUCT_QUERY
                data_tuple = (
                    self.id,
                    self.name,
                    float(self.price),
                    int(self.quantity),
                    float(self.discount),
                    self.category,
                    datetime.now().strftime("%d-%m-%Y"),
                    self.user_id,
                )
                cursor.execute(query, data_tuple)

    except Exception:
        print(PromptMessage.EXCEPTION_PROMPT_MESSAGE)
        logger.error("Something Went Wrong With Inserting Rows", "products.log")
