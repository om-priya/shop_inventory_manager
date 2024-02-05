import pytest
from fastapi.testclient import TestClient
from database.db_access import DbAccess
from config.product_query import ProductQuery, DatabaseConfig
from config.user_query import UserQuery

from app import app

@pytest.fixture
def insert_into_testdb_success(monkeypatch):
    monkeypatch.setattr(DatabaseConfig, "DB_PATH", "test.db")
    user_data = (
        "testuser",
        "test user name",
        "test user email",
        "test user phone",
        "m",
        "tester",
        "testing shop",
        "testingpassword",
    )
    data1 = (
        "product1",
        "product name1",
        "25.00",
        "25",
        "2.00",
        "test",
        "02-02-2024",
        "testuser",
    )
    DbAccess.write_to_database(ProductQuery.CREATE_PRODUCT_TABLE)
    DbAccess.write_to_database(ProductQuery.INSERT_PRODUCT_QUERY, data1)
    DbAccess.write_to_database(UserQuery.CREATE_USER_TABLE)
    DbAccess.write_to_database(UserQuery.INSERT_USER_DATA, user_data)
    yield
    DbAccess.write_to_database("DELETE FROM product")
    DbAccess.write_to_database("DELETE FROM user")


@pytest.fixture
def insert_into_testdb_failure_no_product(monkeypatch):
    monkeypatch.setattr(DatabaseConfig, "DB_PATH", "test.db")
    user_data = (
        "testuser",
        "test user name",
        "test user email",
        "test user phone",
        "m",
        "tester",
        "testing shop",
        "testingpassword",
    )
    data1 = (
        "product1",
        "product name1",
        "25.00",
        "25",
        "2.00",
        "test",
        "02-02-2024",
        "test different id",
    )
    DbAccess.write_to_database(ProductQuery.CREATE_PRODUCT_TABLE)
    DbAccess.write_to_database(UserQuery.CREATE_USER_TABLE)
    DbAccess.write_to_database(UserQuery.INSERT_USER_DATA, user_data)
    DbAccess.write_to_database(ProductQuery.INSERT_PRODUCT_QUERY, data1)
    yield
    DbAccess.write_to_database("DELETE FROM product")
    DbAccess.write_to_database("DELETE FROM user")


class TestProductRoutePublic:
    client = TestClient(app)

    def test_get_all_products_seccess(self, insert_into_testdb_success):
        response = self.client.get("/api/v1/products")
        assert response.json()["success"] == True
        assert response.status_code == 200

    def test_get_all_products_failure(self, insert_into_testdb_failure_no_product):
        response = self.client.get("/api/v1/products")
        assert response.json()["success"] == False
        assert response.status_code == 404

    def test_get_single_product_success(self, insert_into_testdb_success):
        response = self.client.get("/api/v1/products/product1")
        assert response.json()["success"] == True
        assert response.status_code == 200

    def test_get_single_product_not_found(self, insert_into_testdb_success):
        response = self.client.get("/api/v1/products/product2")
        assert response.json()["success"] == False
        assert response.status_code == 404
