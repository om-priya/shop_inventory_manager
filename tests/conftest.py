import pytest

from config.product_query import DatabaseConfig


# @pytest.fixture(scope="session")
# def change_db(monkeypatch):
#     monkeypatch.setattr(DatabaseConfig, "DB_PATH", "test.db")


# TestDbAccess.write_to_database(ProductQuery.CREATE_PRODUCT_TABLE)
#     # id, name, price, quantity, discount, category, created_date, user_id
#     data1 = (
#         "product1",
#         "product name1",
#         "25.00",
#         "25",
#         "2.00",
#         "test",
#         "02-02-2024",
#         "testuser",
#     )
#     data2 = (
#         "product2",
#         "product name2",
#         "15.00",
#         "15",
#         "1.00",
#         "test",
#         "01-02-2024",
#         "testuser",
#     )
#     data3 = (
#         "product3",
#         "product name3",
#         "12.00",
#         "10",
#         "4.00",
#         "test",
#         "03-02-2024",
#         "testuser",
#     )
#     TestDbAccess.write_to_database(ProductQuery.INSERT_PRODUCT_QUERY, data1)
#     TestDbAccess.write_to_database(ProductQuery.INSERT_PRODUCT_QUERY, data2)
#     TestDbAccess.write_to_database(ProductQuery.INSERT_PRODUCT_QUERY, data3)
#     monkeypatch.setattr(
#         "database.db_access.DbAccess.read_from_database",
#         TestDbAccess.read_from_database,
#     )
#     monkeypatch.setattr(
#         "database.db_access.DbAccess.write_to_database",
#         TestDbAccess.write_to_database,
#     )
#     yield
#     # Drop Table
#     TestDbAccess.write_to_database("DELETE FROM product")
