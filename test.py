with open("encrypt_key.key", "rb") as file:
    key = file.read()
    print(key)
    print(type(key))

