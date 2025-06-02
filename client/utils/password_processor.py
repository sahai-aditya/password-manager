import argon2
from secrets import choice
import string


def create_salt():
    """
    Returns a 16 char salt.
    """
    CHARS = string.printable
    salt = ""

    for _ in range(16):
        salt += choice(CHARS)

    return salt

def get_secure_password(password):
    """
    Adds salt and pepper to a password and hashes it.
    Returns salt and hashed password.
    """
    salt = create_salt()
    pepper = choice(string.ascii_letters)
    salted_password = pepper + password + salt

    ph = argon2.PasswordHasher()
    hashed_password = ph.hash(salted_password)

    return {"salt": salt, "hashed-password": hashed_password}
