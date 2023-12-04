"""
This Project aims to provide the shop owner all the functionality though 
which he can easily manage his store
The features of this application are as follows:
1> Provide Complete information regarding product
2> Shop Owner Authentication
3> logging feature for different errors 
"""
import sys

from products.product import create_product
from products import product_controller
from users import user_controller
from display_menu import owner_display_menu, user_display_menu, prime_display
from transactions.transaction import Transaction
from config.prompt_message import PromptMessage
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.DEBUG,
    filename="logs.log",
)


def main():
    """This main function is responsible for running the app"""

    print(PromptMessage.WELCOME_MESSAGE)
    logged_in = False
    user_id = ""
    while True:
        prime_display()
        who_are_you = input(PromptMessage.YOUR_PREFERENCE)

        # Showing Owner Functionality
        if who_are_you == "1":
            while not logged_in:
                user_request = input(PromptMessage.LOGIN_SIGNUP_PROMPT)
                # Checking for logged in usser
                if user_request == "1":
                    logged_in, user_id = user_controller.check_login()
                # Signup and Logged in
                elif user_request == "2":
                    user_controller.signup()
                    logged_in, user_id = user_controller.check_login()
                else:
                    print(PromptMessage.INVALID_INPUT_CREDENTIALS)
            owner_display_menu()
            owner_input = input(PromptMessage.ENTER_QUERY)
            while owner_input != "7":
                match owner_input:
                    case "1":
                        create_product(user_id)
                    case "2":
                        product_controller.show_products(user_id)
                    case "3":
                        product_controller.update_product(user_id)
                    case "4":
                        product_controller.delete_product(user_id)
                    case "5":
                        product_controller.get_product_by_name(user_id)
                    case "6":
                        Transaction.get_sales(user_id)
                    case _:
                        print(PromptMessage.INVALID_INPUT)
                owner_display_menu()
                owner_input = input(PromptMessage.ENTER_QUERY)

        # Showing User Functionality
        elif who_are_you == "2":
            user_display_menu()
            user_input = input(PromptMessage.ENTER_QUERY)

            while user_input != "4":
                match user_input:
                    case "1":
                        product_controller.show_products(user_id)
                    case "2":
                        product_controller.get_product_by_name(user_id)
                    case "3":
                        user_controller.buy_product(user_id)
                    case _:
                        print(PromptMessage.INVALID_INPUT)
                user_display_menu()
                user_input = input(PromptMessage.ENTER_QUERY)

        elif who_are_you == "3":
            sys.exit()

        else:
            print(PromptMessage.WRONG_PROMPT)


# Calling Main Function
if __name__ == "__main__":
    main()
