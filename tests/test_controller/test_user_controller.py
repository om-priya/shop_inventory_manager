import pytest
from controller.user_controller import (
    show_products,
    find_product,
    get_product_by_id_public,
)


@pytest.fixture
def mock_read_from_database(monkeypatch):
    monkeypatch.setattr(
        "controller.user_controller.DAO.read_from_database",
        lambda *args: "data",
    )


class TestUserController:
    def test_show_products(self, mock_read_from_database):
        result = show_products()
        assert result == "data"

    def test_find_product(self, mock_read_from_database):
        result = find_product("abc")
        assert result == "data"

    def test_get_product_by_id(self, monkeypatch):
        monkeypatch.setattr(
            "controller.user_controller.find_product",
            lambda *args: "data",
        )
        result = get_product_by_id_public("abc")
        assert result == "data"
