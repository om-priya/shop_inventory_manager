import maskpass
import shortuuid
from datetime import datetime
from users.user import ShopOwner
import validators.user_validator
from database import DatabaseConnection
from exception_handler.sql_exception_handler import exception_handler
from encryption.encryption import *
from loggers.general_logger import GeneralLogger
from query.user_query import UserQuery
from products import product_controller
from validators import product_validator
from transactions.transaction import Transaction

# ***** To Generate Key For Encryption *****
# key = Fernet.generate_key()
# with open("encrypt_key.key", "wb") as file_key:
#     file_key.write(key)


# Check For Login Users
@exception_handler
def check_login():
    email = input("Enter Your Email: ")
    entered_password = maskpass.advpass()

    with DatabaseConnection("users.db") as connection:
        cursor = connection.cursor()
        params = (email,)
        cursor.execute(UserQuery.LOGIN_QUERY, params)
        user_info = cursor.fetchone()
        # decrypting the db password
        db_password = decrypt_password(user_info[0])
        user_id = user_info[1]

    # Converting the entered_pass to bytes and then comparing
    byte_enter_pass = bytes(entered_password, "utf-8")
    if byte_enter_pass == db_password:
        return [True, user_id]
    GeneralLogger.info("Unsuccessfull Login", "users.log")
    return [False, ""]


# Creating Owner Object and encrypting password and storing it in users.db
@exception_handler
def signup():
    owner_object = {}
    owner_object["name"] = validators.user_validator.name_validator().lower()
    owner_object["email"] = validators.user_validator.email_validator().lower()
    owner_object["phone"] = validators.user_validator.phone_validator()
    owner_object["gender"] = validators.user_validator.gender_validator().upper()
    owner_object["role"] = "owner"
    owner_object["shop_name"] = validators.user_validator.shop_validator().lower()
    owner_object["password"] = encrypt_password(
        validators.user_validator.password_validator()
    )

    new_owner = ShopOwner(owner_object)
    new_owner.save_user()
    print("Owner Created SuccessFully You Can Log In Now")

@exception_handler
def buy_product(user_id):
    product_controller.show_products(user_id)
    user_req = input("Do you want to buy? (yes/no) ").lower().strip()
    user_order = []
    while user_req == "yes":
        name = input("Enter thw name of the product you want to buy: ").lower().strip()
        product = product_controller.find_product(name, user_id)
        if not product:
            print("Product not Found")
        else:
            req_quantity = int(product_validator.quantity_validator())
            while req_quantity > product[0][3]:
                print(f"Enter quantitiy less than or equal to {product[0][3]}")
                req_quantity = int(product_validator.quantity_validator())
        today = datetime.now()
        initial_quantity = int(product[0][3])
        order_tuple = (
            shortuuid.ShortUUID().random(length=8),  # tid
            product[0][0],  # pid
            user_id,  # ownerid
            req_quantity,  # quantity
            req_quantity * product[0][2],  # amount
            today.strftime("%Y"),  # year
            today.strftime("%B"),  # month
        )
        user_order.append(order_tuple)
        user_req = input("Do you want to buy more? (yes/no) ").lower().strip()

    final_req = input("Do you want to proceed with billing? (yes/no) ").lower().strip()
    while final_req != "yes" and final_req != "no":
        print("Enter either yes or no")
        final_req = (
            input("Do you want to proceed with billing? (yes/no)").lower().strip()
        )

    if final_req == "no":
        print("You just cancel your request !!")
        return

    # update product db
    for order in user_order:
        product_controller.update_productdb(user_id, initial_quantity - order[3], order[1])
        Transaction.save_info(order)

    print("Thank You For Shopping Do visit us Again ")
