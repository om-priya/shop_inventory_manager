class UserQuery:
    CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS user(
                               Id TEXT,
                               name TEXT,
                               email TEXT UNIQUE,
                               phone TEXT,
                               gender TEXT,
                               role TEXT,
                               shop_name TEXT,
                               password TEXT
                )"""
    INSERT_USER_DATA = """INSERT INTO user
                            (Id, name, email, phone, gender, role, shop_name, password)
                            VALUES
                            (?,?,?,?,?,?,?,?)"""
    LOGIN_QUERY = "SELECT password, Id FROM user WHERE email = (?)"
