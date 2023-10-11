import re
import maskpass
from exception_handler.validation_exception import validation_exception
from loggers.general_logger import GeneralLogger


@validation_exception
def validator(pattern, input_data):
    x = re.search(pattern, input_data)
    if x == None:
        GeneralLogger.warning("Invalid Input", "users.log")
        print("Invalid Input")
        return False
    return True


# Accepted Syntax: <string> <string>
def name_validator():
    validated = False
    name = ""
    while validated == False:
        name = input("Enter the name of the user: ")
        validated = validator("^[A-Za-z]+([\ A-Za-z]+)*", name)
    return name


# Accepted Syntax: <alphanumeric>@<alphanumeric>.<rootUrl>
def email_validator():
    validated = False
    email = ""
    while validated == False:
        email = input("Enter the email of the user: ")
        validated = validator("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}", email)
    return email


# Accepted Syntax: <M/F>
def gender_validator():
    gender = ""
    validated = False
    while validated == False:
        gender = input("Enter gender of user (M/F): ").upper()
        validated = validator("[M,F]{1}$", gender)
    return gender


# Accepted Syntax: <int>{10}
def phone_validator():
    phone_no = ""
    validated = False
    while validated == False:
        phone_no = input("Enter the phone_no of the user: ")
        validated = validator("^[0-9]{10}$", phone_no)
    return phone_no


# Accepted Syntax: <name> <name>
def shop_validator():
    shop = ""
    validated = False
    while validated == False:
        shop = input("Enter the Shop Name: ")
        validated = validator("^[A-Za-z]+([\ A-Za-z]+)*", shop)
    return shop


# Accepted Syntax - Don't Know
def password_validator():
    password = ""
    validated = False
    while validated == False:
        password = maskpass.advpass()
        validated = validator(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$",
            password,
        )
    return password
