"""This module is resp"""
import re
from exception_handler.validation_exception import validation_exception
from loggers.general_logger import GeneralLogger


# validator for all the fields
@validation_exception
def validator(pattern, input_data):
    """General Validator which return either True or False"""
    x = re.search(pattern, input_data)
    if x is None:
        GeneralLogger.warning("Invalid Input", "products.log")
        return False
    return True


# Accepted Syntax: <string> <string>
def name_validator():
    """Name Validator Function"""
    name = ""
    validated = False
    while validated is False:
        name = input("Enter the name of the product: ")
        validated = validator("^[A-Za-z]+([\ A-Za-z]+)*", name)
    return name


# Accepted Syntax: <number>.<number>
def price_validator():
    """Price Validator Function"""
    price = ""
    validated = False
    while validated is False:
        price = input("Enter the price of the product: ")
        validated = validator("[0-9]*[.][0-9]*", price)
    return price


# Accepted Syntax: <number>
def quantity_validator():
    """Quantity Validator Function"""
    quantity = ""
    validated = False
    while validated is False:
        quantity = input("Enter the quantity of the product: ")
        validated = validator("\d+", quantity)
    return quantity


# Accepted Syntax: <number>.<number>
def discount_validator():
    """Discount Validator Function"""
    discount = ""
    validated = False
    while validated is False:
        discount = input("Enter the discount of the product: ")
        validated = validator("[0-9]*[.][0-9]*", discount)
    return discount


# Accepted Syntax: <string> <string>
def category_validator():
    """Category Validator Function"""
    category = ""
    validated = False
    while validated is False:
        category = input("Enter the category of the product: ")
        validated = validator("^[A-Za-z]+([\ A-Za-z]+)*", category)
    return category


# Accepted Syntax: <number> (len = 4)
def year_validator():
    """Year Validator Function"""
    year = ""
    validated = False
    while validated is False:
        year = input("Enter the year: ")
        validated = validator("[0-9]{4}$", year)
    return year
