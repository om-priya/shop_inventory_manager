class TransactionQuery:
    CREATE_TABLE = """CREATE TABLE IF NOT EXISTS billing(
                               tId TEXT,
                               pId TEXT,
                               owner_Id TEXT,
                               quantity INTEGER,
                               amount REAL,
                               year TEXT,
                               month TEXT
                )"""

    SAVE_INFO = """INSERT INTO billing (
                            tID, 
                            pId, 
                            owner_id, 
                            quantity, 
                            amount, 
                            year, 
                            month
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)"""

    GET_SALES = """SELECT SUM(amount) FROM billing WHERE owner_id = (?) GROUP BY year HAVING year = (?)"""
