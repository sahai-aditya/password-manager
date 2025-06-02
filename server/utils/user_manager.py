# This module has functions to interact with the sqlite3 database users table

import os
import sqlite3
import argon2
import string


DATABASE_FILE = os.path.join(os.getcwd(), "users_passwords.db")

def create_user(username, password, salt):
    """
    Adds a user to the users table. password parameter takes in hashed passwords.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    query = f"INSERT INTO USERS (NAME, PASSWORD, SALT) VALUES ('{username}', '{password}', '{salt}')"
    cursor.execute(query)

    conn.commit()
    conn.close()

def find_user(username):
    """
    Returns id if username found otherwise returns false.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM USERS WHERE NAME='{username}';")
    user = cursor.fetchall()
    conn.close()


    if user != []:
        return user[0][0]

    return False

def delete_user(user_id):
    """
    Deletes user from id. Assumes that find_user gave this id and does not do checks.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM USERS WHERE ID={user_id};")
    conn.commit()
    conn.close()

def check_credentials(username, password):
    """
    Checks if user with given username and password exist. password parameter takes in unhashed password.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM USERS WHERE NAME='{username}';")
    user = cursor.fetchall()[0]
    conn.close()

    if user == []:
        return False

    user_id, _, hashed_password, salt = user
    salted_password = password + salt
    ph = argon2.PasswordHasher()

    for char in string.ascii_letters:
        try:
            ph.verify(hashed_password, char + salted_password)
        except argon2.exceptions.VerifyMismatchError:
            continue
        else:
            return True

    return False
