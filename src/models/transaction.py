from database.database_connector import DatabaseConnection
from database.db_access import DbAccess as DAO
from config.transaction_query import TransactionQuery
from config.product_query import DatabaseConfig

class Transaction:
    @staticmethod
    def save_info(order_details):
        with DatabaseConnection(DatabaseConfig.DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(TransactionQuery.CREATE_TABLE)
            cursor.execute(TransactionQuery.SAVE_INFO, order_details)

    @staticmethod
    def get_sales(user_id, year):
        params = (user_id, year)
        sales_amount = DAO.read_from_database(TransactionQuery.GET_SALES, params)
        return sales_amount