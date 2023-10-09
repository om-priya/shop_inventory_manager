import shortuuid
from validators.product_validator import *


class Products:
    try:

        def __init__(self, product_obj):
            self.id = shortuuid.uuid()[:5]
            self.name = product_obj["name"]
            self.price = product_obj["price"]
            self.quantity = product_obj["quantity"]
            self.discount = product_obj["discount"]
            self.category = product_obj["category"]

        # Saving Product to File
        def save_product(self):
            with open("products.txt", "a") as product_file:
                template = f"{self.id}, {self.name}, {self.price}, {self.quantity}, {self.discount}, {self.category}\n"
                product_file.write(template)

    except Exception:
        print(Exception.__name__)
        print("Something Went Wrong Try Again !!")


# Create Product Object and Save to txt file
def create_product():
    # Creating Product Object
    product_obj = {}
    product_obj["name"] = name_validator().lower()
    product_obj["price"] = price_validator()
    product_obj["quantity"] = quantity_validator()
    product_obj["discount"] = discount_validator()
    product_obj["category"] = category_validator().lower()

    new_product = Products(product_obj)
    new_product.save_product()
    print("Product Added Succesfully!!!")
