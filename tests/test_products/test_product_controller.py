from products.product_controller import (
    show_products,
    find_product,
    get_product_by_name,
    helper,
    update_product,
    delete_product,
    update_product_quantity,
)
from unittest import mock


class TestProductController:
    mock_data = [("om",), ("priya",)]

    def test_show_products_with_no_user_id(self, capsys):
        show_products("")
        captured = capsys.readouterr()
        assert "Ask the Owner to Logged In First Shop is Closed" in captured.out

    @mock.patch(
        "products.product_controller.DAO.read_from_database", return_value=mock_data
    )
    def test_show_products_with_user_id(self, mock_data, capsys):
        show_products("abdsed")
        captured = capsys.readouterr()
        assert "om" in captured.out

    def test_find_product_with_no_user_id(self, capsys):
        find_product("coco-cola", "")
        captured = capsys.readouterr()
        assert "Ask the Owner to Logged In First Shop is Closed" in captured.out

    @mock.patch(
        "products.product_controller.DAO.read_from_database", return_value=mock_data
    )
    def test_find_product_with_user_id(self, mock_data):
        excpected = [("om",), ("priya",)]
        actual = find_product("coco-cola", "abc")
        assert excpected == actual

    @mock.patch("builtins.input", return_value="coco-cola")
    @mock.patch("products.product_controller.find_product", return_value=None)
    def test_get_product_by_name_with_no_product(
        self, mock_find_product, mock_input, capsys
    ):
        get_product_by_name("abc")
        captured = capsys.readouterr()
        assert "Product Not Found" in captured.out

    @mock.patch("builtins.input", return_value="coco-cola")
    @mock.patch("products.product_controller.find_product", return_value=mock_data)
    def test_get_product_by_name_with_product(self, mock_deco, mock_input, capsys):
        get_product_by_name("asfed")
        captured = capsys.readouterr()
        assert "om" in captured.out

    def test_helper_with_invalid_data(self):
        expected = False
        actual = helper("dance")
        assert expected == actual

    def test_helper_with_valid_data(self):
        expected = True
        actual = helper("discount")
        assert expected == actual

    def test_update_product(self, monkeypatch, capsys):
        options = ["dummy_name", "name"]
        monkeypatch.setattr("builtins.input", lambda *args: options.pop(0))
        monkeypatch.setattr(
            "products.product_controller.find_product", lambda *args: "dummy product"
        )
        monkeypatch.setattr(
            "products.product_controller.product_validator.name_validator",
            lambda *args: "Om Priya",
        )
        monkeypatch.setattr(
            "products.product_controller.DAO.write_to_database", lambda *args: None
        )
        update_product("")
        captured = capsys.readouterr()
        assert "Rows UPDATED SUCCESSFULLY" in captured.out

    def test_delete_product(self, monkeypatch, capsys):
        options = ["dummy_name", "name"]
        monkeypatch.setattr("builtins.input", lambda *args: options.pop(0))
        monkeypatch.setattr(
            "products.product_controller.find_product", lambda *args: "dummy product"
        )
        monkeypatch.setattr(
            "products.product_controller.DAO.write_to_database", lambda *args: None
        )
        delete_product("abc")
        captured = capsys.readouterr()
        assert "Product DELETED SUCCESSFULLY" in captured.out

    def test_update_product_quantity(self, monkeypatch):
        monkeypatch.setattr(
            "products.product_controller.DAO.write_to_database", lambda *args: None
        )
        update_product_quantity("abc")
