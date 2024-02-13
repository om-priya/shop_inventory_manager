from database.db_access import DbAccess as DAO
from config.product_query import ProductQuery
import logging

logger = logging.getLogger(__name__)


# To showcase all the products
def show_products():
    products_data = DAO.read_from_database(ProductQuery.FETCH_ALL_PRODUCT)
    return products_data


# Find Product by name
def find_product(product_id):
    params = (product_id,)
    product = DAO.read_from_database(ProductQuery.FETCH_SINGLE_PRODUCT, params)

    return product


# To get product by name
def get_product_by_id_public(product_id):
    product = find_product(product_id)
    return product
