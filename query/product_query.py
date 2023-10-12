class ProductQuery:
    CREATE_PRODUCT_TABLE = """CREATE TABLE IF NOT EXISTS product(
                               id TEXT,
                               name TEXT,
                               price REAL,
                               quantity INTEGER,
                               discount REAL,
                               category TEXT,
                               created_date TEXT,
                               user_id TEXT
                )"""
    INSERT_PRODUCT_QUERY = """INSERT INTO product
                            (id, name, price, quantity, discount, category, created_date, user_id)
                            VALUES
                            (?,?,?,?,?,?,?,?)"""
    GET_ALL_PRODUCT = "SELECT * FROM product WHERE user_id = ?"
    FIND_PRODUCT_BY_NAME = "SELECT * FROM product WHERE name = (?) AND user_id = (?)"
    UPDATE_PRODUCT = "UPDATE product SET {} = (?) WHERE name = (?)"
    DELETE_PRODUCT = "DELETE FROM product WHERE name = (?) AND user_id = (?)"
