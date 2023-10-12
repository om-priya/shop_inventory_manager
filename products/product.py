import shortuuid
from validators.product_validator import *
from database import DatabaseConnection
from datetime import datetime
from loggers.general_logger import GeneralLogger
from query.product_query import ProductQuery


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
            with DatabaseConnection("products.db") as connection:
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
        print("Something Went Wrong")
        GeneralLogger.error("Something Went Wrong With Inserting Rows", "products.log")


# Create Product Object and Save to txt file
def create_product(user_id):
    # Creating Product Object
    product_obj = {}
    product_obj["name"] = name_validator().lower()
    product_obj["price"] = price_validator()
    product_obj["quantity"] = quantity_validator()
    product_obj["discount"] = discount_validator()
    product_obj["category"] = category_validator().lower()
    product_obj["user_id"] = user_id

    new_product = Products(product_obj)
    new_product.save_product()
    print("Product Added Succesfully!!!")
