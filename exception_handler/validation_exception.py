# error handling as decorator
def validation_exception(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            if res is False:
                raise Exception
        except Exception:
            print("Invalid Input")
        finally:
            return res

    return wrapper
