# error handling as decorator
from config.prompt_message import PromptMessage
def validation_exception(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            if res is False:
                raise Exception
        except Exception:
            print(PromptMessage.INVALID_INPUT)
        finally:
            return res

    return wrapper
