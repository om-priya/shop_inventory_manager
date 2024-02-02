from controller.auth_controller import check_login, sign_up
from database.database_connector import DatabaseConnection


class TestAuthController:
    def test_sign_up(self, mocker):
        mock_shop_owner = mocker.Mock()
        mocker.patch(
            "controller.auth_controller.ShopOwner", return_value=mock_shop_owner
        )
        sign_up("abc")
        assert mock_shop_owner.save_user.call_count == 1

    def test_check_login_success(self, mocker, monkeypatch):
        mock_database_connection = mocker.MagicMock(spec=DatabaseConnection)
        mocker.patch(
            "controller.auth_controller.DatabaseConnection",
            return_value=mock_database_connection,
        )
        mock_cursor = mocker.MagicMock()
        mock_database_connection.__enter__.return_value.cursor.return_value = (
            mock_cursor
        )
        mock_database_connection.__exit__.return_value = None

        monkeypatch.setattr(
            "controller.auth_controller.decrypt_password",
            lambda password: bytes("password", "utf-8"),
        )
        is_valid, user_id = check_login("email", "password")

        assert mock_cursor.execute.call_count == 1
        assert is_valid
