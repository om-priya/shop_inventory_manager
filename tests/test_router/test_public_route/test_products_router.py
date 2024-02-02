import pytest
from fastapi.testclient import TestClient
from database.db_access import DbAccess
from config.product_query import ProductQuery, DatabaseConfig

# from
from app import app

client = TestClient(app)


@pytest.fixture()
def insert_into_test(monkeypatch):
    monkeypatch.setattr(DatabaseConfig, "DB_PATH", "test.db")
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
    data2 = (
        "product2",
        "product name2",
        "15.00",
        "15",
        "1.00",
        "test",
        "01-02-2024",
        "testuser",
    )
    data3 = (
        "product3",
        "product name3",
        "12.00",
        "10",
        "4.00",
        "test",
        "03-02-2024",
        "testuser",
    )
    DbAccess.write_to_database(ProductQuery.CREATE_PRODUCT_TABLE)
    DbAccess.write_to_database(ProductQuery.INSERT_PRODUCT_QUERY, data1)
    DbAccess.write_to_database(ProductQuery.INSERT_PRODUCT_QUERY, data2)
    DbAccess.write_to_database(ProductQuery.INSERT_PRODUCT_QUERY, data3)
    yield
    DbAccess.write_to_database("DELETE FROM product")


class TestProductRoutePublic:
    client = TestClient(app)

    # @pytest.mark.usefixtures("insert_into_test")
    def test_get_all_products_seccess(self, insert_into_test):
        response = self.client.get("/api/v1/products")
        print(response.json())
        assert response.status_code == 200
