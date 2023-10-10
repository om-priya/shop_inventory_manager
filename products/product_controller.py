from database import DatabaseConnection
from tabulate import tabulate
from validators import product_validator
from exception_handler.sql_exception_handler import exception_handler


# To showcase all the products
@exception_handler
def show_products():
    with DatabaseConnection("products.db") as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM product")

        products_data = cursor.fetchall()

    print(tabulate(products_data))


# Find Product by name
@exception_handler
def find_product(name):
    with DatabaseConnection("products.db") as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM product WHERE name = (?)"
        params = (name.lower(),)
        cursor.execute(query, params)
        product = cursor.fetchall()
    return product


# To get product by name
def get_product_by_name():
    name = input("Enter the product name: ")
    product = find_product(name)
    if len(product) == 0 or product == None:
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
def update_product():
    # Take the name of the product
    name = input("Enter the name of product you want to be upgraded: ").lower()

    # Check for it's existence
    product = find_product(name)
    if product == None:
        print("Product Not Found")
        return

    # Taking field input and validating it
    updated_field = input("Enter the field You want to update: ").lower()
    while True:
        if helper(updated_field):
            break
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

        cursor.execute(
            "UPDATE product SET {} = (?) WHERE name = (?)".format(updated_field),
            (value, name),
        )
        print("Rows Updated Successfully")


# Delete Product (only owner can perform)
@exception_handler
def delete_product():
    name = input("Enter the name the product you want to delete: ")
    with DatabaseConnection("products.db") as connection:
        cursor = connection.cursor()
        query = "DELETE FROM product WHERE name = (?)"
        params = (name.lower(),)
        cursor.execute(query, params)
    print("Product Deleted Successfully")
