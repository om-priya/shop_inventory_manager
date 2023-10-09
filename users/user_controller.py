from cryptography.fernet import Fernet
from users.user import ShopOwner
import validators.user_validator
import maskpass

# ***** To Generate Key For Encryption *****
# key = Fernet.generate_key()
# with open("encrypt_key.key", "wb") as file_key:
#     file_key.write(key)


# Check For Login Users
def check_login():
    email = input("Enter Your Email: ")
    entered_password = maskpass.advpass()

    try:
        with open("users.txt", "r") as file:
            user_list = file.readlines()
            for user in user_list:
                user = user.split(",")
                if email.strip().lower() == user[1].strip().lower():
                    decrypted_value = user[6].strip()
                    if entered_password == decrypted_value:
                        return True
            else:
                print("Owner Not Found")
                return False
    except FileNotFoundError:
        print("Currently No User Found")
        return False


# Creating Owner Object and storing it in users.txt
def signup():
    owner_object = {}
    owner_object["name"] = validators.user_validator.name_validator().lower()
    owner_object["email"] = validators.user_validator.email_validator().lower()
    owner_object["phone"] = validators.user_validator.phone_validator()
    owner_object["gender"] = validators.user_validator.gender_validator().upper()
    owner_object["role"] = "owner"
    owner_object["shop_name"] = validators.user_validator.shop_validator().lower()
    owner_object["password"] = validators.user_validator.password_validator()

    new_owner = ShopOwner(owner_object)
    new_owner.save_user()
    print("Owner Created SuccessFully You Can Log In Now")
