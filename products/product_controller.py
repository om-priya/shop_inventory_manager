from datetime import datetime
from tabulate import tabulate

from database import DatabaseConnection
from validators import product_validator
from exception_handler.sql_exception_handler import exception_handler
from loggers.general_logger import GeneralLogger
from query.product_query import ProductQuery


# To showcase all the products
@exception_handler
def show_products(user_id):
    print(user_id)
    if user_id == "":
        GeneralLogger.warning("Someone Tried to enter the Shop", "users.log")
        print("Ask the Owner to Logged In First Shop is Closed")
        return
    with DatabaseConnection("products.db") as connection:
        cursor = connection.cursor()
        params = (user_id,)
        cursor.execute(ProductQuery.GET_ALL_PRODUCT, params)

        products_data = cursor.fetchall()

    print(tabulate(products_data))


# Find Product by name
@exception_handler
def find_product(name, user_id):
    if user_id == "":
        GeneralLogger.warning("Someone Tried to enter the Shop", "users.log")
        print("Ask the Owner to Logged In First Shop is Closed")
        return
    with DatabaseConnection("products.db") as connection:
        cursor = connection.cursor()
        params = (name.lower(), user_id.strip())
        cursor.execute(ProductQuery.FIND_PRODUCT_BY_NAME, params)
        product = cursor.fetchall()
    return product


# To get product by name
def get_product_by_name(user_id):
    name = input("Enter the product name: ")
    product = find_product(name, user_id)
    if not product:
        GeneralLogger.info(f"{name} Product Not Found", "products.log")
        print("Product Not Found")
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
    name = input("Enter the name of product you want to be upgraded: ").lower()

    # Check for it's existence
    product = find_product(name, user_id)
    if not product:
        GeneralLogger.info(f"{name} Product Not Found", "products.log")
        print("Product Not Found")
        return

    # Taking field input and validating it
    updated_field = input("Enter the field You want to update: ").lower()
    while True:
        if helper(updated_field):
            break
        GeneralLogger.info("Invalid Input For Field", "products.log")
        print("Invalid Input")
        updated_field = input("Enter the field You want to update").lower()

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
    with DatabaseConnection("products.db") as connection:
        cursor = connection.cursor()
        str(datetime.now().strftime("%d-%m-%Y"))
        cursor.execute(
            ProductQuery.UPDATE_PRODUCT.format(
                updated_field,
            ),
            (value, name),
        )
        GeneralLogger.info(f"Rows Updated Successfully for {name}", "products.log")
        print("Rows Updated Successfully")


# Delete Product (only owner can perform)
@exception_handler
def delete_product(user_id):
    name = input("Enter the name the product you want to delete: ")
    product = find_product(name, user_id)
    if not product:
        GeneralLogger.info(f"{name} Product Not Found", "products.log")
        print("Product Not Found")
        return
    with DatabaseConnection("products.db") as connection:
        cursor = connection.cursor()
        params = (name.lower(), user_id.strip())
        cursor.execute(ProductQuery.DELETE_PRODUCT, params)
    GeneralLogger.info(f"{name} Deleted Successfully", "products.log")
    print("Product Deleted Successfully")


@exception_handler
def update_productdb(user_id, quantity, productId):
    with DatabaseConnection("products.db") as connection:
        cursor = connection.cursor()
        query = ProductQuery.UPDATE_PRODUCT_TRANSACTION
        params = (quantity, user_id, productId)
        cursor.execute(query, params)
