"""
This Module is used to show prompt in the console
"""
from config.prompt_message import PromptMessage


def owner_display_menu():
    """This function is responsible for showing owner display menu to the prompt"""
    print(PromptMessage.OWNER_DISPLAY_MENU)


def user_display_menu():
    """This function is responsible for showing user display menu to the prompt"""
    print(PromptMessage.USER_DISPLAY_MENU)


def prime_display():
    print(PromptMessage.PRIME_DISPLAY)
