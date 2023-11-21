from cryptography.fernet import Fernet

def encrypted(password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5G=')
    b_password = bytes(password, 'ascii')
    encrypted_password = f.encrypt(b_password)
    return encrypted_password.decode('ascii')

def decrypt(password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5G=')
    b_password = bytes(password, 'ascii')
    b_password_descrypt = f.encrypt(b_password)
    return b_password_descrypt.decode('ascii')