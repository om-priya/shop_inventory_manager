from utils.sql_exception_handler import exception_handler
from database.db_access import DbAccess as DAO
from config.product_query import ProductQuery
from config.prompt_message import PromptMessage
import logging
from tabulate import tabulate

logger = logging.getLogger(__name__)


# To showcase all the products
def show_products():
    products_data = DAO.read_from_database(ProductQuery.FETCH_ALL_PRODUCT)

    return products_data


# Find Product by name
def find_product(product_id):
    params = (product_id,)
    product = DAO.read_from_database(ProductQuery.FETCH_SINGLE_PRODUCT, params)

    return product


# To get product by name
def get_product_by_id_public(product_id):
    product = find_product(product_id)
    return product


# @exception_handler
# def buy_product(user_id):
#     show_products()
#     user_req = input("Do you want to buy? (yes/no) ").lower().strip()
#     user_order = []
#     while user_req == "yes":
#         name = input("Enter thw name of the product you want to buy: ").lower().strip()
#         product = find_product(name)
#         if not product:
#             print("Product not Found")
#         else:
#             req_quantity = int(product_validator.quantity_validator())
#             while req_quantity > product[0][3]:
#                 print(f"Enter quantitiy less than or equal to {product[0][3]}")
#                 req_quantity = int(product_validator.quantity_validator())
#         today = datetime.now()
#         initial_quantity = int(product[0][3])
#         order_tuple = (
#             shortuuid.ShortUUID().random(length=8),  # tid
#             product[0][0],  # pid
#             user_id,  # ownerid
#             req_quantity,  # quantity
#             req_quantity * product[0][2],  # amount
#             today.strftime("%Y"),  # year
#             today.strftime("%B"),  # month
#         )
#         user_order.append(order_tuple)
#         user_req = input("Do you want to buy more? (yes/no) ").lower().strip()

#     final_req = input("Do you want to proceed with billing? (yes/no) ").lower().strip()
#     while final_req != "yes" and final_req != "no":
#         print("Enter either yes or no")
#         final_req = (
#             input("Do you want to proceed with billing? (yes/no)").lower().strip()
#         )

#     if final_req == "no":
#         print("You just cancel your request !!")
#         return

#     # update product db
#     for order in user_order:
#         product_controller.update_product_quantity(
#             user_id, initial_quantity - order[3], order[1]
#         )
#         Transaction.save_info(order)

#     print("Thank You For Shopping Do visit us Again ")
