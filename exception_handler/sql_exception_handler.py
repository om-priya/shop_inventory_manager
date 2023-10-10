def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception:
            print("Some Error Occured Try Again!! ")
            res = None
        finally:
            return res

    return wrapper
