"""This module is resp"""
import re
from utils.validation_exception import validation_exception
import logging
from config.prompt_message import PromptMessage

logger = logging.getLogger(__name__)


# validator for all the fields
@validation_exception
def validator(pattern, input_data):
    """General Validator which return either True or False"""
    x = re.fullmatch(pattern, input_data)
    if x is None:
        logger.warning("Invalid Input")
        return False
    return True


# Accepted Syntax: <string> <string>
def name_validator():
    """Name Validator Function"""
    name = ""
    validated = False
    while validated is False:
        name = input(PromptMessage.PROMPT_PRODUCT_MESSAGE.format("name"))
        validated = validator(r"^[A-Za-z]+([\ A-Za-z]+)*", name)
    return name


# Accepted Syntax: <number>.<number>
def price_validator():
    """Price Validator Function"""
    price = ""
    validated = False
    while validated is False:
        price = input(PromptMessage.PROMPT_PRODUCT_MESSAGE.format("price"))
        validated = validator(r"[0-9]*[.][0-9]*", price)
    return price


# Accepted Syntax: <number>
def quantity_validator():
    """Quantity Validator Function"""
    quantity = ""
    validated = False
    while validated is False:
        quantity = input(PromptMessage.PROMPT_PRODUCT_MESSAGE.format("quantity"))
        validated = validator(r"\d+", quantity)
    return quantity


# Accepted Syntax: <number>.<number>
def discount_validator():
    """Discount Validator Function"""
    discount = ""
    validated = False
    while validated is False:
        discount = input(PromptMessage.PROMPT_PRODUCT_MESSAGE.format("discount"))
        validated = validator(r"[0-9]*[.][0-9]*", discount)
    return discount


# Accepted Syntax: <string> <string>
def category_validator():
    """Category Validator Function"""
    category = ""
    validated = False
    while validated is False:
        category = input(PromptMessage.PROMPT_PRODUCT_MESSAGE.format("category"))
        validated = validator(r"^[A-Za-z]+([\ A-Za-z]+)*", category)
    return category


# Accepted Syntax: <number> (len = 4)
def year_validator():
    """Year Validator Function"""
    year = ""
    validated = False
    while validated is False:
        year = input(PromptMessage.YEAR_INPUT_PROMPT)
        validated = validator(r"[0-9]{4}$", year)
    return year
