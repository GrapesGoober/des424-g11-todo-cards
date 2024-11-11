import sqlite3
from datetime import date


DB_FILE = 'backend\\database.db'

def singup_user(username: str, 
                password: str,
                dateOfBirth: date, #YYYY-MM-DD
                email: str):
    
    conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO users (username, password, dateOfBirth, email) VALUES (?, ?, ?, ?)",
            (username,), (password,), (dateOfBirth,), (email,) ) 
    
    conn.commit()
    conn.close()
    

def Is_username_exists(username: str):
    conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Query to check if the username exists
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    exists = cursor.fetchone() is not None

    conn.commit()
    conn.close()
    return exists

def user_login(username: str, password:str):
    conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM users WHERE username = ? AND password = ?", (username, password))
    exists = cursor.fetchone() is not None

    conn.commit()
    conn.close()
    return exists

def create_user_table():
    conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            date_of_birth DATE,
            email TEXT UNIQUE
        )
    ''')

    conn.commit()
    conn.close()