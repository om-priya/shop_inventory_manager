import pytest
from fastapi.testclient import TestClient
from database.db_access import DbAccess
from config.product_query import DatabaseConfig
from config.user_query import UserQuery
from app import app
import builtins


@pytest.fixture
def mock_decryption(monkeypatch):
    monkeypatch.setattr(
        "controller.auth_controller.decrypt_password",
        lambda en_password: bytes(en_password, "utf-8"),
    )


@pytest.fixture
def create_test_user_info(monkeypatch):
    monkeypatch.setattr(DatabaseConfig, "DB_PATH", "test.db")
    user_data = (
        "testuser",
        "test user name",
        "testuser@gmail.com",
        "test user phone",
        "m",
        "tester",
        "testing shop",
        "Test@123",
    )
    DbAccess.write_to_database(UserQuery.CREATE_USER_TABLE)
    DbAccess.write_to_database(UserQuery.INSERT_USER_DATA, user_data)
    yield
    DbAccess.write_to_database("DELETE FROM user")


class TestAuthRouter:
    client = TestClient(app)

    def test_login_route_success(self, mock_decryption, create_test_user_info, monkeypatch):
        response = self.client.post(
            "api/v1/login", json={"email": "testuser@gmail.com", "password": "Test@123"}
        )
        assert response.status_code == 200
        assert response.json()["success"] == True

    def test_login_route_failure(self, mock_decryption, create_test_user_info, monkeypatch):
        response = self.client.post(
            "api/v1/login", json={"email": "testuser@gmail.com", "password": "Fail@123"}
        )
        assert response.status_code == 404
        assert response.json()["success"] == False
