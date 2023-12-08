from transactions.transaction import Transaction
from database.database_connector import DatabaseConnection
from unittest.mock import MagicMock
from unittest import mock


class TestTransaction:
    def test_save_info(self):
        mock_database_connection = MagicMock(spec=DatabaseConnection)
        with mock.patch(
            "transactions.transaction.DatabaseConnection"
        ) as mock_database_connection:
            mock_cursor = MagicMock()
            mock_database_connection().__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            Transaction.save_info("")

            assert mock_cursor.execute.call_count == 2

    @mock.patch("transactions.transaction.year_validator", return_value="2002")
    @mock.patch(
        "transactions.transaction.DAO.read_from_database",
        return_value=[("om",), ("priya",)],
    )
    def test_get_sales(self, mock_data, mock_year, capsys):
        Transaction.get_sales("")
        captured = capsys.readouterr()

        assert "The sales for the year 2002 is om" in captured.out
