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
    GET_ALL_PRODUCT = "SELECT * FROM product WHERE user_id = (?)"
    FIND_PRODUCT_BY_ID = "SELECT * FROM product WHERE id = (?) AND user_id = (?)"
    UPDATE_PRODUCT = "UPDATE product SET name = (?), price = (?), quantity = (?), discount = (?), category = (?) WHERE id = (?) AND user_id = (?)"
    DELETE_PRODUCT = "DELETE FROM product WHERE id = (?) AND user_id = (?)"
    UPDATE_PRODUCT_TRANSACTION = (
        "UPDATE product SET quantity = (?) WHERE user_id = (?) AND id = (?)"
    )
    FETCH_ALL_PRODUCT = "SELECT p.id, p.name, p.price, p.quantity, u.shop_name FROM product as p JOIN user as u ON p.user_id = u.Id"
    FETCH_SINGLE_PRODUCT = "SELECT * FROM product WHERE id = (?)"


class DatabaseConfig:
    DB_PATH = "store.db"
    TEST_DB = "test.db"
