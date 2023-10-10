from cryptography.fernet import Fernet


def get_key():
    with open("encrypt_key.key", "rb") as file:
        key = file.read()
        return key


def encrypt_password(password):
    password = bytes(password, "utf-8")
    f = Fernet(get_key())
    cipher_pass = f.encrypt(password)
    return cipher_pass


def decrypt_password(en_password):
    f = Fernet(get_key())
    plain_pass = f.decrypt(en_password)
    return plain_pass


#cipher = encrypt_password("Om Priya")
#print(decrypt_password(cipher))
