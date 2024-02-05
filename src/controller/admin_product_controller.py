from database.db_access import DbAccess as DAO
import logging
from config.product_query import ProductQuery
import sqlite3

logger = logging.getLogger(__name__)


def show_products(user_id):
    products_data = DAO.read_from_database(ProductQuery.GET_ALL_PRODUCT, (user_id,))
    return products_data


# Find Product by name


def find_product(product_id, user_id):
    params = (
        product_id,
        user_id.strip(),
    )
    product = DAO.read_from_database(ProductQuery.FIND_PRODUCT_BY_ID, params)

    return product


# To get product by name
def get_product_by_id(product_id, user_id):
    product = find_product(product_id, user_id)
    if not product:
        return None
    else:
        return product


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


def update_product(product_id, user_id, updated_field):
    # Check for it's existence
    product = find_product(product_id, user_id)
    if not product:
        logger.info(f"{product_id} Product Not Found", "products.log")
        raise ValueError

    params = (
        updated_field["name"],
        updated_field["price"],
        updated_field["quantity"],
        updated_field["discount"],
        updated_field["category"],
        product_id,
        user_id,
    )
    # Setting new value to the db
    DAO.write_to_database(ProductQuery.UPDATE_PRODUCT, params)
    logger.info(f"Rows Updated Successfully for {product_id}", "products.log")


# # Delete Product (only owner can perform)


def delete_product(product_id, user_id):
    product = find_product(product_id, user_id)
    if not product:
        logger.info(f"{product_id} Product Not Found", "products.log")
        raise ValueError
    params = (product_id, user_id.strip())
    DAO.write_to_database(ProductQuery.DELETE_PRODUCT, params)
    logger.info(f"{product_id} Deleted Successfully", "products.log")
