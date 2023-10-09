from database import DatabaseConnection

# Human Class
class Human:
    try:

        def __init__(self, name, email, phone, gender):
            self.name = name
            self.email = email
            self.phone = phone
            self.gender = gender

    except Exception:
        print(Exception.__name__)
        print("Something Went Wrong Try Again !!")


# Owner Class inheriting human
class ShopOwner(Human):
    try:

        def __init__(self, owner_obj):
            super().__init__(
                owner_obj["name"],
                owner_obj["email"],
                owner_obj["phone"],
                owner_obj["gender"],
            )
            self.role = owner_obj["role"]
            self.shop_name = owner_obj["shop_name"]
            self.password = owner_obj["password"]

        # saving users to user-file
        def save_user(self):
            with DatabaseConnection("users.db") as connection:
                cursor = connection.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS user(
                               name TEXT,
                               email TEXT,
                               phone TEXT,
                               gender TEXT,
                               role TEXT,
                               shop_name TEXT,
                               password TEXT
                )"""
                )
                query = """INSERT INTO user
                            (name, email, phone, gender, role, shop_name, password)
                            VALUES
                            (?,?,?,?,?,?,?)"""
                data_tuple = (
                    self.name,
                    self.email,
                    self.phone,
                    self.gender,
                    self.role,
                    self.shop_name,
                    self.password
                )
                cursor.execute(query, data_tuple)

    except Exception:
        print(Exception.__name__)
        print("Something Went Wrong Try Again !!")
