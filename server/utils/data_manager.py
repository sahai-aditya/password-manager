# This module has functions to interact with the sqlite3 database passwords table

import sqlite3
import os


DATABASE_FILE = os.path.join(os.getcwd(), "users_passwords.db")

def initialize_database():
    """
    Creates the database file if it does not exist and redefines the tables'
    structure.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    CREATE_USER_TABLE_QUERY = """CREATE TABLE USERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    PASSWORD TEXT,
    SALT TEXT
    );"""

    CREATE_PASSWORDS_TABLE_QUERY = """CREATE TABLE PASSWORDS (
    USER INTEGER NOT NULL,
    APP TEXT,
    PASSWORD TEXT,
    FOREIGN KEY (USER) REFERENCES USERS(ID)
    );"""

    cursor.execute(CREATE_USER_TABLE_QUERY)
    cursor.execute(CREATE_PASSWORDS_TABLE_QUERY)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()