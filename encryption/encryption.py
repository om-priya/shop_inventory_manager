from cryptography.fernet import Fernet


# To get the key stored in .key file
def get_key():
    with open("encrypt_key.key", "rb") as file:
        key = file.read()
        return key


# Encrypt password using fernet
def encrypt_password(password):
    password = bytes(password, "utf-8")
    f = Fernet(get_key())
    cipher_pass = f.encrypt(password)
    return cipher_pass


# decrypt password using fernet
def decrypt_password(en_password):
    f = Fernet(get_key())
    plain_pass = f.decrypt(en_password)
    return plain_pass
