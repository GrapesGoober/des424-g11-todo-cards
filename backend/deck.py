import mysql.connector
from pydantic import BaseModel
from datetime import datetime

def connect_to_db() -> mysql.connector.MySQLConnection:
    """
    Returns mysql connection to `interns_db` as root user.
    """
    # these configs are defined in compose.yaml
    return mysql.connector.connect(
        host="mysql", # connects to mysql container, instead of normally via "localhost"
        user="root",
        password="",
        database="todocards"
    )

def create_deck(mydb, deck_info, userid):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        INSERT INTO `deck` (`deckName`, `deckDescription`, `deckOwnerID`) 
        VALUES (%s, %s)
        """,
        (deck_info["deckName"], deck_info["deckDescription"])
    )

    deck_id = mycursor.lastrowid
    return True

def edit_deck():
    pass

def delete_deck():
    pass

def add_user_to_deck():
    pass

def remove_user_from_deck():
    pass

