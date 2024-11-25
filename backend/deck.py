import mysql.connector
from typing import List
from pydantic import BaseModel
from datetime import datetime

class DeckInfo(BaseModel):
    name: str
    description: str

class DeckList(BaseModel):
    id: int
    name: str

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

def create_deck(body: DeckInfo, user: str) -> bool:
    db = connect_to_db()
    cursor = db.cursor()
    username = user
    
    try:
        # Create new deck
        cursor.execute(
            """
            INSERT INTO `deck` (`deckName`, `deckDescription`, `deckOwnerName`) 
            VALUES (%s, %s, %s)
            """,
            (body.name, body.description, username)
        )
        deck_id = cursor.lastrowid

        # Add the owner to the access table
        cursor.execute(
            """
            INSERT INTO `access` (`deckid`, `username`, `allow`) 
            VALUES (%s, %s, %s)
            """,
            (deck_id, username, True)
        )

        # Commit the changes to the database
        db.commit()

    except Exception as e:
        db.rollback()  # Roll back in case of an error
        print(f"Error: {e}")
        return False

    finally:
        # Close the cursor
        cursor.close()

    return True

def get_deck(user:str) -> List[DeckList]:
    db = connect_to_db()
    cursor = db.cursor()
    username = user

    cursor.execute(
        """
        SELECT `deck.deckid`, `deck.deckname` 
        FROM `deck` 
        JOIN `access` ON
        """
    )

def edit_deck():
    pass

def delete_deck(d):
    pass

def add_user_to_deck():
    pass

def remove_user_from_deck():
    pass

