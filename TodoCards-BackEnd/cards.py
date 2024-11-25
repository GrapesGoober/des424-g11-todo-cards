# This is the script cards.py, which will be handling all-things cards and subcards
# This includes: getting, creating, editing, finishing, and deleting cards and subcards
# Author: Panisara S 6422781326, Nachat K 6422770774

# using this access check function for the "create card" feature
#from decks import check_deck_view_access, check_deck_edit_access
import decks
from datetime import datetime

# Utility function to check access for your card_id
def check_card_view_access(mydb, card_id, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
            SELECT deckId
            FROM card 
            WHERE cardid = %s
            """, (card_id,)
    )
    
    result = mycursor.fetchall()
    mycursor.close()
    mydb.commit()
    for row in result:
        if (decks.check_deck_view_access(mydb, row[0], username) == True or decks.check_deck_edit_access(mydb, row[0], username) == True):
            return True
    return False


# Utility function to check access for your subcard_id
def check_subcard_view_access(mydb, subcard_id, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
            SELECT cardID
            FROM subcard
            WHERE scardid = %s
            """, (subcard_id,)
    )
    
    result = mycursor.fetchall()
    mycursor.close()
    mydb.commit()
    for row in result:
        if (check_card_view_access(mydb, row[0], username) == True or check_card_edit_access(mydb, row[0], username) == True):
            return True
    return False


# Utility function to check access for your card_id
def check_card_edit_access(mydb, card_id, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
            SELECT deckId
            FROM card 
            WHERE cardid = %s
            """, (card_id,)
    )
    
    result = mycursor.fetchall()
    mycursor.close()
    mydb.commit()
    for row in result:
        if (decks.check_deck_edit_access(mydb, row[0], username) == True):
            return True
    return False


# Utility function to check access for your subcard_id
def check_subcard_edit_access(mydb, subcard_id, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
            SELECT cardID
            FROM subcard
            WHERE scardid = %s
            """, (subcard_id,)
    )
    
    result = mycursor.fetchall()
    mycursor.close()
    mydb.commit()
    for row in result:
        if (check_card_edit_access(mydb, row[0], username) == True):
            return True
    return False

# Retrieve all cards within a deck
# must also check view access of the deck (using check_deck_view_access function)
# Otherwise, returns empty list
def get_cards_list(mydb, deck_id, username):

    if not decks.check_deck_view_access(mydb, deck_id, username):
        return False

    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            cardId, cardName, cardDescription, cardDue, cardIsFinished, cardcolor
        FROM card WHERE deckID = %s
        """, (deck_id,))
    
    result = mycursor.fetchall()
    for i, r in enumerate(result):
        if r[3] != None:
            format_due = r[3].strftime("%Y-%m-%d")
            #formatted_nearest_due = int(r[3])
        else:
            format_due = ""
        result[i] = {
            "cardId": int(r[0]),
            "cardName": r[1],
            "cardDescription": r[2],
            "cardDue": format_due,
            "cardIsFinished": r[4],
            "cardColor": r[5]
        }
        #print(result[i])

    mycursor.close()
    mydb.commit()
    return result

# Retrieve all subcards within a card
# must also check view access of that card_id
# Otherwise, returns empty list
def get_subcards_list(mydb, card_id, username):
    if not check_card_view_access(mydb, card_id, username):
        return False
    
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            scardid, scardName, scardIsFinished 
        FROM subcard 
        WHERE cardid = %s
        """, (card_id,))
    
    result = mycursor.fetchall()
    for i, r in enumerate(result):
        result[i] = {
            "subcardId": int(r[0]),  
            "subcardName": r[1],
            "subcardIsFinished": int(r[2]),
        }
        #print(result[i])

    mycursor.close()
    mydb.commit()
    return result

# updates a card by setting isFinished = True
# must also check edit access of that card_id
# returns True if success, False otherwise
def finish_card(mydb, card_id, is_unfinished, username):
    if check_card_edit_access(mydb, card_id, username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                UPDATE card
                SET cardIsFinished = %s
                WHERE cardid = %s
                """, ( 0 if is_unfinished else 1, card_id,)
        )
        mycursor.close()
        mydb.commit()
        return True
    return False


# updates a subcard by setting isFinished = True
# must also check edit access of that subcard_id
# returns True if success, False otherwise
def finish_subcard(mydb, subcard_id, is_unfinished, username):
    
    if check_subcard_edit_access(mydb, subcard_id, username):
        print(is_unfinished, 0 if is_unfinished else 1)
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                UPDATE subcard
                SET scardIsFinished = %s
                WHERE scardid = %s
                """, ( 0 if is_unfinished else 1, subcard_id,)
        )
        mycursor.close()
        mydb.commit()
        return True
    return False

# updates a card with card_info
# must also check edit access of card_info["cardId"]
# returns True if success, False otherwise
def edit_card(mydb, card_info, username):  
    
    #print(card_info["cardid"])
    if check_card_edit_access(mydb, int(card_info["cardId"]), username):
        
        # format datestring into date object
        dateObj = datetime.strptime(card_info["cardDue"], "%Y-%m-%d")

        mycursor = mydb.cursor()
        mycursor.execute(
            """
            UPDATE card
            SET 
                cardName = %s,
                cardDescription = %s,
                cardDue = %s,
                cardIsFinished = %s,
                cardColor = %s
            WHERE cardid = %s
            """,
            (
             card_info["cardName"], 
             card_info["cardDescription"], 
             dateObj,
             card_info["cardIsFinished"], 
             card_info["cardColor"], 
             int(card_info["cardId"]))
        )
          
        mycursor.close()
        mydb.commit()
        return True
    return False



# updates a subcard with card_info
# must also check edit access
# returns True if success, False otherwise
def edit_subcard(mydb, subcard_info, username):
    if check_subcard_edit_access(mydb, int(subcard_info["subcardId"]), username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
            UPDATE subcard
            SET 
                scardName = %s
            WHERE scardid = %s
            """,
            (subcard_info["subcardName"], 
             int(subcard_info["subcardId"]) )
        )
          
        mycursor.close()
        mydb.commit()
        return True
    return False


# creates a new card within the deck
# must also check edit access for that deck_id
# returns True if success, False otherwise
def create_card(mydb, deck_id, card_info, username):
    if decks.check_deck_edit_access(mydb, deck_id, username):

        # format datestring into date object
        dateObj = datetime.strptime(card_info["cardDue"], "%Y-%m-%d")

        mycursor = mydb.cursor()
        mycursor.execute(
            """
            INSERT INTO `card` (`deckId`, `cardName`, `cardDescription`, `cardIsFinished`, `cardDue`, `cardColor`) 
            VALUES (%s, %s, %s, 0, %s, %s)
            """,
            (deck_id, card_info["cardName"], 
             card_info["cardDescription"], 
             dateObj, 
             card_info["cardColor"])
        )
          
        mycursor.close()
        mydb.commit()
    
        return True
    return False

# creates a new card within the deck
# must also check edit access for that card_id
# returns True if success, False otherwise
def create_subcard(mydb, card_id, subcard_info, username):
    if check_card_edit_access(mydb, card_id, username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
            INSERT INTO `subcard` (`cardId`, `scardName`, `scardIsFinished`) 
            VALUES (%s, %s, 0)
            """,
            (card_id, subcard_info["subcardName"], )
        )
          
        mycursor.close()
        mydb.commit()
        return True
    return False


# deletes a card within the deck
# must also check edit access for that card_id
# returns True if success, False otherwise
def delete_card(mydb, card_id, username):
    
    if check_card_edit_access(mydb, card_id, username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                DELETE FROM card
                WHERE cardid = %s
                """, (card_id,)
        )
        mycursor.close()
        mydb.commit()
        return True
    
    return False
    

# deletes a subcard within the card
# must also check edit access for that subcard_id
# returns True if success, False otherwise
def delete_subcard(mydb, subcard_id, username):

    if check_subcard_edit_access(mydb, subcard_id, username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                DELETE FROM subcard
                WHERE scardid = %s
                """, (subcard_id,)
        )
        mycursor.close()
        mydb.commit()
        return True
    
    return False