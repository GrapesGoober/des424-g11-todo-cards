
import sqlite3

# I'm thinking we have 2 database instances
# 1 - AWS database (say, RDS) for deployment
# 2 - local sqlite for development
# These two should be easily swapped, but how can we do that?
# Dependency injection? Functional Dep-inj? Python supports first class funcs
# - First class funcs
# - Objects
# - Static Methods 
# we need a DB connect function

DB_FILE = 'backend\\database.db'

def record_text_to_db(text):
    conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Insert the text into the table
    cursor.execute("INSERT INTO text_records (text) VALUES (?)", (text,))

    conn.commit()
    conn.close()

def create_table():
    conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS text_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
        )
    ''')

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
    
def user_login(username: str, password:str):
    conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM users WHERE username = ? AND password = ?", (username, password))
    exists = cursor.fetchone() is not None

    conn.commit()
    conn.close()
    return exists
    
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
    