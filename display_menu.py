"""
This Module is used to show prompt in the console
"""


def owner_display_menu():
    """This function is responsible for showing owner display menu to the prompt"""
    print(
        """What do you want to do? (select options)
    1> Add Product
    2> Show All Product
    3> Update Product
    4> Delete Product
    5> Get Product By Name
    6> Get Sales by Year
    7> Quit App
    """
    )


def user_display_menu():
    """This function is responsible for showing user display menu to the prompt"""
    print(
        """What do you want to do? (select options)
            1> Show All Product
            2> Get Product By Name
            3> Buy Product
            4> Quit App
        """
    )


def prime_display():
    print(
        """Who are You?
            1> Owner
            2> User
            3> Quit
        """
    )
