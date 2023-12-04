class PromptMessage:
    WELCOME_MESSAGE = "******* Welcome User *******"
    YOUR_PREFERENCE = "Enter Your Prefereance: "
    LOGIN_SIGNUP_PROMPT = "Enter 1 for login and 2 for signup: "
    INVALID_INPUT_CREDENTIALS = "Invalid Input/Credentials"
    ENTER_QUERY = "Enter Your Query: "
    INVALID_INPUT = "Invalid Input"
    WRONG_PROMPT = "Please enter correct prompt"
    OWNER_DISPLAY_MENU = """What do you want to do? (select options)
    1> Add Product
    2> Show All Product
    3> Update Product
    4> Delete Product
    5> Get Product By Name
    6> Get Sales by Year
    7> Quit App
    """
    USER_DISPLAY_MENU = """What do you want to do? (select options)
            1> Show All Product
            2> Get Product By Name
            3> Buy Product
            4> Quit App
        """
    PRIME_DISPLAY = """Who are You?
            1> Owner
            2> User
            3> Quit
        """
    PROMPT_PRODUCT_MESSAGE = "Enter the {} of the product: "
    PROMPT_USER_MESSAGE = "Enter the {} of the user: "
    YEAR_INPUT_PROMPT = "Enter the year: "
    SHOP_NAME_PROMPT = "Enter the Shop Name: "
    EXCEPTION_PROMPT_MESSAGE = "Something Went Wrong Try Again !!"
    SUCCESS_ACTION = "{} ADDED SUCCESSFULLY"
    UPDATE_ACTION = "{} UPDATED SUCCESSFULLY"
    DELETED_ACTION = "{} DELETED SUCCESSFULLY"
    ASK_OWNER_TO_LOG_IN = "Ask the Owner to Logged In First Shop is Closed"
    NOT_FOUND = "{} Not Found"
    UPDATE_PRODUCT_FIELD = "Enter the {} of product you want to be upgraded: "
    DELETE_PRODUCT_PROMPT = "Enter the {} the product you want to delete: "
