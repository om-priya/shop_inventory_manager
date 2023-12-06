from users.user import ShopOwner
from unittest import mock
from unittest.mock import MagicMock
from database.database_connector import DatabaseConnection
import pytest


shop_owner_info = {
    "name": "Om Priya",
    "email": "ompriya@gmail.com",
    "phone": "8229070126",
    "gender": "M",
    "role": "owner",
    "shop_name": "Antriksh Kirana",
    "password": "Ompriya@2002",
}


class TestShopOwner:
    test_shop_owner_obj = ShopOwner(shop_owner_info)

    def test_save_user(self):
        # mock_cursor = mock_database_connection_for_user
        mock_database_connection = MagicMock(spec=DatabaseConnection)
        with mock.patch("users.user.DatabaseConnection") as mock_database_connection:
            mock_cursor = MagicMock()
            mock_database_connection().__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            self.test_shop_owner_obj.save_user()

            assert mock_cursor.execute.call_count == 2
