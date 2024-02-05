import pytest
from fastapi.testclient import TestClient
from database.db_access import DbAccess
from config.product_query import ProductQuery, DatabaseConfig
from router.public_routes.auth_router import get_user_id_from_token


from app import app


async def mock_get_user_id_from_token():
    return "testuser"


app.dependency_overrides[get_user_id_from_token] = mock_get_user_id_from_token


@pytest.fixture
def insert_into_test_db_product(monkeypatch):
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
    DbAccess.write_to_database(ProductQuery.CREATE_PRODUCT_TABLE)
    DbAccess.write_to_database(ProductQuery.INSERT_PRODUCT_QUERY, data1)
    yield
    DbAccess.write_to_database("DELETE FROM product")


class TestAdminProductRouter:
    client = TestClient(app)

    def test_get_all_products(self, insert_into_test_db_product):
        response = self.client.get(
            "api/v1/admin/products", headers={"Authorization": "Bearer some-token"}
        )
        assert response.status_code == 200
        assert response.json()["success"] == True

    def test_get_all_products_not_found(self, monkeypatch):
        monkeypatch.setattr(DatabaseConfig, "DB_PATH", "test.db")
        response = self.client.get(
            "api/v1/admin/products", headers={"Authorization": "Bearer some-token"}
        )
        assert response.status_code == 404
        assert response.json()["success"] == False

    def test_get_single_product(self, insert_into_test_db_product):
        response = self.client.get(
            "api/v1/admin/products/product1",
            headers={"Authorization": "Bearer some-token"},
        )
        assert response.status_code == 200
        assert response.json()["success"] == True

    def test_get_single_product_not_found(self, monkeypatch):
        monkeypatch.setattr(DatabaseConfig, "DB_PATH", "test.db")
        response = self.client.get(
            "api/v1/admin/products/product1",
            headers={"Authorization": "Bearer some-token"},
        )
        assert response.status_code == 404
        assert response.json()["success"] == False

    def test_create_product_success(self, monkeypatch):
        monkeypatch.setattr(DatabaseConfig, "DB_PATH", "test.db")
        response = self.client.post(
            "api/v1/admin/products",
            headers={"Authorization": "Bearer some-token"},
            json={
                "name": "TestProduct",
                "price": "25.00",
                "quantity": "23",
                "discount": "2.00",
                "category": "test",
            },
        )
        assert response.status_code == 201
        assert response.json()["success"] == True
        DbAccess.write_to_database("DELETE FROM product")

    def test_put_update_product(self, insert_into_test_db_product):
        response = self.client.put(
            "api/v1/admin/products/product1",
            headers={"Authorization": "Bearer some-token"},
            json={
                "name": "TestProduct",
                "price": "25.00",
                "quantity": "23",
                "discount": "2.00",
                "category": "test",
            },
        )
        assert response.status_code == 200
        assert response.json()["success"] == True

    def test_put_update_product_not_found(self, insert_into_test_db_product):
        response = self.client.put(
            "api/v1/admin/products/product2",
            headers={"Authorization": "Bearer some-token"},
            json={
                "name": "TestProduct",
                "price": "25.00",
                "quantity": "23",
                "discount": "2.00",
                "category": "test",
            },
        )
        assert response.status_code == 404
        assert response.json()["success"] == False

    def test_delete_product_route_success(self, insert_into_test_db_product):
        response = self.client.delete(
            "api/v1/admin/products/product1",
            headers={"Authorization": "Bearer some-token"},
        )
        assert response.status_code == 200
        assert response.json()["success"] == True

    def test_delete_product_route_not_found(self, monkeypatch):
        monkeypatch.setattr(DatabaseConfig, "DB_PATH", "test.db")
        response = self.client.delete(
            "api/v1/admin/products/product1",
            headers={"Authorization": "Bearer some-token"},
        )
        assert response.status_code == 404
        assert response.json()["success"] == False
