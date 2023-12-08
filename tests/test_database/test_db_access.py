from database.db_access import DbAccess
from database.database_connector import DatabaseConnection
from unittest.mock import MagicMock
from unittest import mock


class TestDbAcces:
    def test_read_from_database_with_params(self):
        mock_database_connection = MagicMock(spec=DatabaseConnection)
        with mock.patch(
            "database.db_access.DatabaseConnection"
        ) as mock_database_connection:
            mock_cursor = MagicMock()
            mock_database_connection().__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            DbAccess.read_from_database("", "data")

            assert mock_cursor.execute.call_count == 1
            assert mock_cursor.fetchall.call_count == 1

    def test_read_from_database_without_params(self):
        mock_database_connection = MagicMock(spec=DatabaseConnection)
        with mock.patch(
            "database.db_access.DatabaseConnection"
        ) as mock_database_connection:
            mock_cursor = MagicMock()
            mock_database_connection().__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            DbAccess.read_from_database("")

            assert mock_cursor.execute.call_count == 1
            assert mock_cursor.fetchall.call_count == 1

    def test_write_to_database_with_params(self):
        mock_database_connection = MagicMock(spec=DatabaseConnection)
        with mock.patch(
            "database.db_access.DatabaseConnection"
        ) as mock_database_connection:
            mock_cursor = MagicMock()
            mock_database_connection().__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            DbAccess.write_to_database("", "data")

            assert mock_cursor.execute.call_count == 1

    def test_write_to_database_without_params(self):
        mock_database_connection = MagicMock(spec=DatabaseConnection)
        with mock.patch(
            "database.db_access.DatabaseConnection"
        ) as mock_database_connection:
            mock_cursor = MagicMock()
            mock_database_connection().__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            DbAccess.write_to_database("")

            assert mock_cursor.execute.call_count == 1
