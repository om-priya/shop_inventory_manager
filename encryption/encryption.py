"""This Module is responsible for handling all the functions related to encryption and decryption"""

from cryptography.fernet import Fernet
from loggers.general_logger import GeneralLogger

try:
    # To get the key stored in .key file
    def get_key():
        """To read key from the file in binary format"""
        with open("encrypt_key.key", "rb") as file:
            key = file.read()
            return key

    # Encrypt password using fernet
    def encrypt_password(password):
        """To encrypt the password"""
        password = bytes(password, "utf-8")
        f = Fernet(get_key())
        cipher_pass = f.encrypt(password)
        return cipher_pass

    # decrypt password using fernet
    def decrypt_password(en_password):
        """To decrypt the password"""
        f = Fernet(get_key())
        plain_pass = f.decrypt(en_password)
        return plain_pass

except Exception:
    GeneralLogger.critical("Something Wrong with Encryption", "users.log")
