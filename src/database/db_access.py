from database.database_connector import DatabaseConnection


class DbAccess:
    @staticmethod
    def read_from_database(query, params=None):
        with DatabaseConnection("store.db") as conn:
            cursor = conn.cursor()
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            res_data = cursor.fetchall()
        return res_data

    @staticmethod
    def write_to_database(query, params=None):
        with DatabaseConnection("store.db") as conn:
            cursor = conn.cursor()
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
