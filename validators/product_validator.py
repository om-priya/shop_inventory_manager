import re
from exception_handler.validation_exception import validation_exception

# validator for all the fields
@validation_exception
def validator(pattern, input_data):
    x = re.search(pattern, input_data)
    if x == None:
        return False
    return True


# Accepted Syntax: <string> <string>
def name_validator():
    name = ""
    validated = False
    while validated == False:
        name = input("Enter the name of the product: ")
        validated = validator("^[A-Za-z]+([\ A-Za-z]+)*", name)
    return name


# Accepted Syntax: <number>.<number>
def price_validator():
    price = ""
    validated = False
    while validated == False:
        price = input("Enter the price of the product: ")
        validated = validator("[0-9]*[.][0-9]*", price)
    return price


# Accepted Syntax: <number>
def quantity_validator():
    quantity = ""
    validated = False
    while validated == False:
        quantity = input("Enter the quantity of the product: ")
        validated = validator("\d+", quantity)
    return quantity


# Accepted Syntax: <number>.<number>
def discount_validator():
    discount = ""
    validated = False
    while validated == False:
        discount = input("Enter the discount of the product: ")
        validated = validator("[0-9]*[.][0-9]*", discount)
    return discount


# Accepted Syntax: <string> <string>
def category_validator():
    category = ""
    validated = False
    while validated == False:
        category = input("Enter the category of the product: ")
        validated = validator("^[A-Za-z]+([\ A-Za-z]+)*", category)
    return category
