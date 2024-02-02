import re
import logging
from config.prompt_message import PromptMessage

logger = logging.getLogger(__name__)


def validator(pattern, input_data):
    x = re.fullmatch(pattern, input_data)
    if x == None:
        logger.warning("Invalid Input", "users.log")
        print(PromptMessage.INVALID_INPUT)
        return False
    return True


# Accepted Syntax - Don't Know
def password_validator(password):
    validated = validator(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$",
        password,
    )
    if validated:
        return True
    return False
