"""
This Project aims to provide the shop owner all the functionality though which he can easily manage his store
The features of this application are as follows:
1> Provide Complete information regarding product
2> Shop Owner Authentication
3> logging feature for different errors 
"""
from products.product import create_product
from products import product_controller
from users import user_controller
from display_menu import *


def main():
    print("******* Welcome User *******")
    who_are_you = input("Are you a owner or user? ").lower()
    logged_in = False
    user_id = ""
    # Showing Owner Functionality
    if who_are_you == "owner":
        logged_in = False
        user_id = ""
        while logged_in == False or logged_in == None:
            user_request = int(input("Enter 1 for login and 2 for signup: "))
            # Checking for logged in usser
            if user_request == 1:
                logged_in, user_id = user_controller.check_login()
            # Signup and Logged in
            elif user_request == 2:
                user_controller.signup()
                logged_in, user_id = user_controller.check_login()
            else:
                print("Invalid Input/Credentials")
        owner_display_menu()
        owner_input = int(input("Enter Your Query: "))
        while owner_input != 6:
            match owner_input:
                case 1:
                    create_product(user_id)
                case 2:
                    product_controller.show_products(user_id)
                case 3:
                    product_controller.update_product(user_id)
                case 4:
                    product_controller.delete_product(user_id)
                case 5:
                    product_controller.get_product_by_name(user_id)
                case _:
                    print("Invalid Input")
            owner_display_menu()
            owner_input = int(input("Enter Your Query: "))

    # Showing User Functionality
    elif who_are_you == "user":
        user_display_menu()
        user_input = int(input("Enter Your Query: "))

        while user_input != 3:
            match user_input:
                case 1:
                    product_controller.show_products(user_id)
                case 2:
                    product_controller.get_product_by_name(user_id)
                case _:
                    print("Invalid Input")
            user_display_menu()
            user_input = int(input("Enter Your Query: "))

    else:
        print("Enter either owner or user")
        main()


# Calling Main Function
if __name__ == "__main__":
    main()


"""
*********** FeedBacks **************
1> Look into the loggers -- Done
2> Try to shift your query to different file and then import it to the file to use it -- Done just check ki phate na
3> Learn about Singelton (try to implement it)
(By Self)
4> Make Query Safe some inner checks as well -- Done
"""
