from database.database_connector import DatabaseConnection
from config.transaction_query import TransactionQuery

with DatabaseConnection("store.db") as connection:
    cursor = connection.cursor()
    cursor.execute(TransactionQuery.CREATE_TABLE)
