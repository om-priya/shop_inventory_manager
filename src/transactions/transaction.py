from database.database_connector import DatabaseConnection
from database.db_access import DbAccess as DAO
from config.transaction_query import TransactionQuery
from utils.product_validator import year_validator
from utils.sql_exception_handler import exception_handler


class Transaction:
    @exception_handler
    @staticmethod
    def save_info(order_details):
        with DatabaseConnection("store.db") as connection:
            cursor = connection.cursor()
            cursor.execute(TransactionQuery.CREATE_TABLE)
            cursor.execute(TransactionQuery.SAVE_INFO, order_details)

    @exception_handler
    @staticmethod
    def get_sales(user_id):
        year = int(year_validator())
        params = (user_id, year)
        sales_amount = DAO.read_from_database(TransactionQuery.GET_SALES, params)
        print(f"The sales for the year {year} is {sales_amount[0][0]}")
