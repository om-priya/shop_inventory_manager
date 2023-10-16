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


def main():
    """This main function is responsible for running the app"""

    print("******* Welcome User *******")
    logged_in = False
    user_id = ""
    while True:
        prime_display()
        who_are_you = input("Enter Your Prefereance: ")

        # Showing Owner Functionality
        if who_are_you == "1":
            while not logged_in:
                user_request = input("Enter 1 for login and 2 for signup: ")
                # Checking for logged in usser
                if user_request == "1":
                    logged_in, user_id = user_controller.check_login()
                # Signup and Logged in
                elif user_request == "2":
                    user_controller.signup()
                    logged_in, user_id = user_controller.check_login()
                else:
                    print("Invalid Input/Credentials")
            owner_display_menu()
            owner_input = input("Enter Your Query: ")
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
                        print("Invalid Input")
                owner_display_menu()
                owner_input = input("Enter Your Query: ")

        # Showing User Functionality
        elif who_are_you == "2":
            user_display_menu()
            user_input = input("Enter Your Query: ")

            while user_input != "4":
                match user_input:
                    case "1":
                        product_controller.show_products(user_id)
                    case "2":
                        product_controller.get_product_by_name(user_id)
                    case "3":
                        user_controller.buy_product(user_id)
                    case _:
                        print("Invalid Input")
                user_display_menu()
                user_input = input("Enter Your Query: ")

        elif who_are_you == "3":
            sys.exit()

        else:
            print("Please enter correct prompt")


# Calling Main Function
if __name__ == "__main__":
    main()
