from datetime import datetime
from tabulate import tabulate

from database.database_connector import DatabaseConnection
from utils import product_validator
from utils.sql_exception_handler import exception_handler
import logging
from config.product_query import ProductQuery
from config.prompt_message import PromptMessage

logger = logging.getLogger(__name__)


# To showcase all the products
@exception_handler
def show_products(user_id):
    print(user_id)
    if user_id == "":
        logger.warning("Someone Tried to enter the Shop", "users.log")
        print(PromptMessage.ASK_OWNER_TO_LOG_IN)
        return
    with DatabaseConnection("store.db") as connection:
        cursor = connection.cursor()
        params = (user_id,)
        cursor.execute(ProductQuery.GET_ALL_PRODUCT, params)

        products_data = cursor.fetchall()

    print(tabulate(products_data))


# Find Product by name
@exception_handler
def find_product(name, user_id):
    if user_id == "":
        logger.warning("Someone Tried to enter the Shop", "users.log")
        print(PromptMessage.ASK_OWNER_TO_LOG_IN)
        return
    with DatabaseConnection("store.db") as connection:
        cursor = connection.cursor()
        params = (name.lower(), user_id.strip())
        cursor.execute(ProductQuery.FIND_PRODUCT_BY_NAME, params)
        product = cursor.fetchall()
    return product


# To get product by name
def get_product_by_name(user_id):
    name = input(PromptMessage.PROMPT_PRODUCT_MESSAGE.format("name"))
    product = find_product(name, user_id)
    if not product:
        logger.info(f"{name} Product Not Found", "products.log")
        print(PromptMessage.NOT_FOUND.format("Product"))
    else:
        print(tabulate(product))


# Update Product (only owner can perform)
def helper(data):
    if (
        data == "name"
        or data == "price"
        or data == "discount"
        or data == "quantity"
        or data == "category"
    ):
        return True
    return False


@exception_handler
def update_product(user_id):
    # Take the name of the product
    name = input(PromptMessage.UPDATE_PRODUCT_FIELD.format("name")).lower()

    # Check for it's existence
    product = find_product(name, user_id)
    if not product:
        logger.info(f"{name} Product Not Found", "products.log")
        print(PromptMessage.NOT_FOUND.format("Product"))
        return

    # Taking field input and validating it
    updated_field = input(PromptMessage.UPDATE_PRODUCT_FIELD.format("field")).lower()
    while True:
        if helper(updated_field):
            break
        logger.info("Invalid Input For Field", "products.log")
        print(PromptMessage.INVALID_INPUT)
        updated_field = input(PromptMessage.UPDATE_PRODUCT_FIELD.format("field")).lower()

    # Calling function according to the updated_field
    value = None
    match updated_field:
        case "name":
            value = product_validator.name_validator()
        case "price":
            value = float(product_validator.price_validator())
        case "discount":
            value = float(product_validator.discount_validator())
        case "quantity":
            value = int(product_validator.quantity_validator())
        case "category":
            value = product_validator.category_validator()

    # Setting new value to the db
    with DatabaseConnection("store.db") as connection:
        cursor = connection.cursor()
        str(datetime.now().strftime("%d-%m-%Y"))
        cursor.execute(
            ProductQuery.UPDATE_PRODUCT.format(
                updated_field,
            ),
            (value, name),
        )
        logger.info(f"Rows Updated Successfully for {name}", "products.log")
        print(PromptMessage.UPDATE_ACTION.format("Rows"))


# Delete Product (only owner can perform)
@exception_handler
def delete_product(user_id):
    name = input(PromptMessage.DELETE_PRODUCT_PROMPT.format("name"))
    product = find_product(name, user_id)
    if not product:
        logger.info(f"{name} Product Not Found", "products.log")
        print(PromptMessage.NOT_FOUND.format("Product"))
        return
    with DatabaseConnection("store.db") as connection:
        cursor = connection.cursor()
        params = (name.lower(), user_id.strip())
        cursor.execute(ProductQuery.DELETE_PRODUCT, params)
    logger.info(f"{name} Deleted Successfully", "products.log")
    print(PromptMessage.DELETED_ACTION.format("Product"))


@exception_handler
def update_productdb(user_id, quantity, productId):
    with DatabaseConnection("store.db") as connection:
        cursor = connection.cursor()
        query = ProductQuery.UPDATE_PRODUCT_TRANSACTION
        params = (quantity, user_id, productId)
        cursor.execute(query, params)
