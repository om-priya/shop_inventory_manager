from products.product import create_product
from database import DatabaseConnection
from tabulate import tabulate


# To showcase all the products
def show_products():
    with DatabaseConnection("products.db") as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM product")

        products_data = cursor.fetchall()

    print(tabulate(products_data))


# Find Product by name
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
    if len(product) == 0:
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


# def update_product():
#     name = input("Enter the name of product you want to be upgraded: ").lower()
#     product = find_product(name)
#     if len(product) == 0:
#         print("Product Not Found")
#         return
#     while True:
#         updated_field = input("Enter the field You want to update")
#         if helper(updated_field):
#             break
#     with DatabaseConnection("products.db") as connection:
#         cursor = connection.cursor()
#         query = "UPDATE product SET (?) = (?) WHERE name = '(?)'"


# Delete Product (only owner can perform)
def delete_product():
    name = input("Enter the name the product you want to delete: ")
    with DatabaseConnection("products.db") as connection:
        cursor = connection.cursor()
        query = "DELETE FROM product WHERE name = (?)"
        params = (name.lower(),)
        cursor.execute(query, params)
    print("Product Deleted Successfully")
