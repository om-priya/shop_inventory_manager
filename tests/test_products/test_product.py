from products.product import Products, create_product
from database.database_connector import DatabaseConnection
from unittest.mock import MagicMock
from unittest import mock

product_owner_info = {
    "name": "Om Priya",
    "price": "34.00",
    "quantity": "23",
    "discount": "3.00",
    "category": "beverages",
    "user_id": "asdf12AS",
}


class TestProducts:
    test_dummy_product_obj = Products(product_owner_info)

    def test_save_product(self):
        # mock_cursor = mock_database_connection_for_user
        mock_database_connection = MagicMock(spec=DatabaseConnection)
        with mock.patch(
            "products.product.DatabaseConnection"
        ) as mock_database_connection:
            mock_cursor = MagicMock()
            mock_database_connection().__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            self.test_dummy_product_obj.save_product()

            assert mock_cursor.execute.call_count == 2

    @mock.patch("products.product.Products.save_product", return_value="Saved")
    @mock.patch("products.product.category_validator", return_value="beverages")
    @mock.patch("products.product.discount_validator", return_value="2.00")
    @mock.patch("products.product.quantity_validator", return_value="23")
    @mock.patch("products.product.price_validator", return_value="12.00")
    @mock.patch("products.product.name_validator", return_value="OMPRIYA")
    def test_create_product(
        self,
        mock_name,
        mock_price,
        mock_quantity,
        mock_discount,
        mock_category,
        mock_save_product,
        capsys,
    ):
        create_product("")
        captured = capsys.readouterr()

        assert "Product ADDED SUCCESSFULLY" in captured.out
