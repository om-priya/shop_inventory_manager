# error handling as decorator
def validation_exception(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            if res == False:
                raise Exception
        except:
            print("Invalid Input")
        finally:
            return res

    return wrapper
