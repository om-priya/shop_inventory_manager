import shortuuid
from validators.product_validator import *
from database import DatabaseConnection


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
            with DatabaseConnection("products.db") as connection:
                cursor = connection.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS product(
                               id TEXT,
                               name TEXT,
                               price REAL,
                               quantity INTEGER,
                               discount REAL,
                               category TEXT 
                )"""
                )
                query = """INSERT INTO product
                            (id, name, price, quantity, discount, category)
                            VALUES
                            (?,?,?,?,?,?)"""
                data_tuple = (
                    self.id,
                    self.name,
                    float(self.price),
                    int(self.quantity),
                    float(self.discount),
                    self.category,
                )
                cursor.execute(query, data_tuple)

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