from database import DatabaseConnection
from query.transaction_query import TransactionQuery
from validators.product_validator import year_validator
from exception_handler.sql_exception_handler import exception_handler


class Transaction:
    @exception_handler
    @staticmethod
    def save_info(order_details):
        with DatabaseConnection("billings.db") as connection:
            cursor = connection.cursor()
            cursor.execute(TransactionQuery.CREATE_TABLE)
            cursor.execute(TransactionQuery.SAVE_INFO, order_details)

    @exception_handler
    @staticmethod
    def get_sales(user_id):
        year = int(year_validator())
        with DatabaseConnection("billings.db") as connection:
            cursor = connection.cursor()
            params = (user_id, year)
            cursor.execute(TransactionQuery.GET_SALES, params)
            sales_amount = cursor.fetchone()
            print(f"The sales for the year {year} is {sales_amount[0]}")
