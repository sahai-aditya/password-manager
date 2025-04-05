# This module is responsible for getting input from the user with basic processing

import getpass

"""
Rich library will be implemented later for a better CLI experience.
"""


def get_signin_info():
    """
    Returns (username, password) given by user.
    Called when user wants to sign in.
    """
    username = input("\nUsername\n>>> ").strip()
    password = getpass.getpass(prompt="\nPassword\n>>> ").strip()

    return (username, password)

def get_signup_info():
    """
    Returns (username, password) given by the user.
    Called when the user wants to sign up.
    """
    username = input("\nUsername\n>>> ").strip()
    password = getpass.getpass(prompt="\nPassword\n>>> ").strip()
    confirm_password  = getpass.getpass(prompt="\nConfirm password\n>>> ").strip()

    while password != confirm_password:
        print("\nPasswords do not match, please try again!")
        password = getpass.getpass(prompt="\nPassword\n>>> ").strip()
        confirm_password  = getpass.getpass(prompt="\nConfirm password\n>>> ").strip()

    return (username, password)
