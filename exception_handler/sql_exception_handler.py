import sqlite3


# exception handling for sqlite operations
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except sqlite3.OperationalError:
            print("Error While Executing the query")
            res = None
        except Exception:
            print("Some Error Occured Try Again!! ")
            res = None
        finally:
            return res

    return wrapper
