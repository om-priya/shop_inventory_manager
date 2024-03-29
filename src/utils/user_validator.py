import re
import maskpass
from utils.validation_exception import validation_exception
import logging
from config.prompt_message import PromptMessage

logger = logging.getLogger(__name__)


@validation_exception
def validator(pattern, input_data):
    x = re.fullmatch(pattern, input_data)
    if x == None:
        logger.warning("Invalid Input", "users.log")
        print(PromptMessage.INVALID_INPUT)
        return False
    return True


# Accepted Syntax: <string> <string>
def name_validator():
    validated = False
    name = ""
    while validated == False:
        name = input(PromptMessage.PROMPT_USER_MESSAGE.format("name"))
        validated = validator(r"^[A-Za-z]+([\ A-Za-z]+)*", name)
    return name


# Accepted Syntax: <alphanumeric>@<alphanumeric>.<rootUrl>
def email_validator(email):
    validated = validator(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}", email)
    if validated:
        return True
    return False


# Accepted Syntax: <M/F>
def gender_validator():
    gender = ""
    validated = False
    while validated == False:
        gender = input(PromptMessage.PROMPT_USER_MESSAGE.format("gender")).upper()
        validated = validator(r"[M,F]{1}$", gender)
    return gender


# Accepted Syntax: <int>{10}
def phone_validator():
    phone_no = ""
    validated = False
    while validated == False:
        phone_no = input(PromptMessage.PROMPT_USER_MESSAGE.format("Phone Number"))
        validated = validator(r"^[0-9]{10}$", phone_no)
    return phone_no


# Accepted Syntax: <name> <name>
def shop_validator():
    shop = ""
    validated = False
    while validated == False:
        shop = input(PromptMessage.SHOP_NAME_PROMPT)
        validated = validator(r"^[A-Za-z]+([\ A-Za-z]+)*", shop)
    return shop


# Accepted Syntax - Don't Know
def password_validator(password):
    validated = validator(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$",
        password,
    )
    if validated:
        return True
    return False
