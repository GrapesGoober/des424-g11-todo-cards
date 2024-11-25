import deck
from datetime import datetime

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
        if (deck.check_deck_view_access(mydb, row[0], username) == True or deck.check_deck_edit_access(mydb, row[0], username) == True):
            return True
    return False

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
        if (deck.check_deck_edit_access(mydb, row[0], username) == True):
            return True
    return False

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

def get_cards_list(mydb, deck_id, username):
    if not deck.check_deck_view_access(mydb, deck_id, username):
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
    mycursor.close()
    mydb.commit()
    return result

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
    mycursor.close()
    mydb.commit()
    return result

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

def edit_card(mydb, card_info, username):  
    if check_card_edit_access(mydb, int(card_info["cardId"]), username):
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

def create_card(mydb, deck_id, card_info, username):
    if deck.check_deck_edit_access(mydb, deck_id, username):
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
