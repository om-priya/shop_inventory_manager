import sqlite3


# exception handling for sqlite operations
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except sqlite3.OperationalError:
            print("Error While Executing the query")
            res = [False, ""]
        except Exception:
            print("Some Error Occured Try Again!! ")
            res = [False, ""]
        finally:
            return res

    return wrapper
