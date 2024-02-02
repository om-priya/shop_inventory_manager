import pytest
from controller.admin_product_controller import (
    show_products,
    find_product,
    get_product_by_id,
    helper,
    update_product,
    delete_product,
)
import sqlite3


@pytest.fixture
def mock_read_from_database(monkeypatch):
    monkeypatch.setattr(
        "controller.admin_product_controller.DAO.read_from_database",
        lambda *args: "data",
    )


class TestAdminProductController:
    def test_show_products(self, mock_read_from_database):
        result = show_products("abc")
        assert result == "data"

    def test_find_product(self, mock_read_from_database):
        result = find_product("abc", "abc")
        assert result == "data"

    def test_get_product_by_id(self, monkeypatch):
        monkeypatch.setattr(
            "controller.admin_product_controller.find_product",
            lambda *args: "data",
        )
        result = get_product_by_id("abc", "abc")
        assert result == "data"

    def test_get_product_by_id_not_found(self, monkeypatch):
        monkeypatch.setattr(
            "controller.admin_product_controller.find_product",
            lambda *args: None,
        )
        result = get_product_by_id("abc", "abc")
        assert result == None

    def test_helper_success(self):
        assert helper("name")

    def test_helper_failure(self):
        assert not helper("abc")

    def test_update_product_success(self, monkeypatch, mocker):
        monkeypatch.setattr(
            "controller.admin_product_controller.find_product",
            lambda *args: ["product", "product_id"],
        )
        updated_field = {
            "name": "test name",
            "price": "23.00",
            "quantity": "25",
            "discount": "2.00",
            "category": "test category",
        }
        mock_obj = mocker.Mock()
        mocker.patch("controller.admin_product_controller.DAO", mock_obj)

        update_product("abc", "abc", updated_field)

        assert mock_obj.write_to_database.call_count == 1

    def test_update_product_failure(self, monkeypatch):
        monkeypatch.setattr(
            "controller.admin_product_controller.find_product",
            lambda *args: None,
        )
        updated_field = {
            "name": "test name",
            "price": "23.00",
            "quantity": "25",
            "discount": "2.00",
            "category": "test category",
        }
        with pytest.raises(sqlite3.Error):
            update_product("abc", "abc", updated_field)

    def test_delete_product_success(self, monkeypatch, mocker):
        monkeypatch.setattr(
            "controller.admin_product_controller.find_product",
            lambda *args: ["product", "product_id"],
        )
        mock_obj = mocker.Mock()
        mocker.patch("controller.admin_product_controller.DAO", mock_obj)

        delete_product("abc", "abc")

        assert mock_obj.write_to_database.call_count == 1

    def test_delete_product_failure(self, monkeypatch):
        monkeypatch.setattr(
            "controller.admin_product_controller.find_product",
            lambda *args: None,
        )
        with pytest.raises(sqlite3.Error):
            delete_product("abc", "abc")
