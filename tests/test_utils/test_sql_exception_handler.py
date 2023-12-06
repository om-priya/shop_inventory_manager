from utils.sql_exception_handler import exception_handler
import sqlite3


def sql_error_func():
    raise sqlite3.OperationalError


def generic_error_func():
    raise Exception


class TestSqlExceptionHandler:
    def test_exception_handler_sql_error(self, capsys):
        exception_handler(sql_error_func)()
        captured = capsys.readouterr()
        assert "Error While Executing the query" in captured.out

    def test_exception_handler_generic_error(self, capsys):
        exception_handler(generic_error_func)()
        captured = capsys.readouterr()
        assert "Some Error Occured Try Again!! \n" in captured.out
