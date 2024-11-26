import admin
import random
import string
from datetime import datetime

def get_finished_cards(mydb, deck_id):
    # Create a cursor to execute the query
    mycursor = mydb.cursor()

    # SQL query to select finished cards
    mycursor.execute("""
        SELECT count(cardid)
        FROM card
        WHERE deckId = %s AND cardIsFinished = 1
    """, (deck_id,))

    # Fetch all the results
    result = mycursor.fetchone()
    finished_cards = result[0]

    # Close the cursor
    mycursor.close()

    # Return the finished cards
    return finished_cards

def get_all_cards(mydb, deck_id):
    # Create a cursor to execute the query
    mycursor = mydb.cursor()

    # SQL query to select all cards
    mycursor.execute("""
        SELECT count(cardid)
        FROM card
        WHERE deckId = %s
    """, (deck_id,))

    # Fetch all the results
    result = mycursor.fetchone()
    all_cards = result[0]

    # Close the cursor
    mycursor.close()

    # Return all cards
    return all_cards

