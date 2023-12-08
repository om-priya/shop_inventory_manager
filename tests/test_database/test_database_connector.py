from database.database_connector import DatabaseConnection
import pytest
import sqlite3


class TestDatabaseCOnnection:
    def test_connection_status(self):
        with DatabaseConnection(":memory:") as conn:
            assert conn is not None

    def test_exception_sqlite(self):
        with pytest.raises(sqlite3.Error):
            with DatabaseConnection(":memory:") as conn:
                raise sqlite3.Error
