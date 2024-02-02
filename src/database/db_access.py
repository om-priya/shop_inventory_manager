from database.database_connector import DatabaseConnection
from config.product_query import DatabaseConfig

class DbAccess:
    @staticmethod
    def read_from_database(query, params=None):
        with DatabaseConnection(DatabaseConfig.DB_PATH) as conn:
            cursor = conn.cursor()
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            res_data = cursor.fetchall()
        return res_data

    @staticmethod
    def write_to_database(query, params=None):
        with DatabaseConnection(DatabaseConfig.DB_PATH) as conn:
            cursor = conn.cursor()
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
