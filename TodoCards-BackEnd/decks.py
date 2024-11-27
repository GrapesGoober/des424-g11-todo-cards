#from datetime import date
import admin 
import random
import string
from datetime import datetime #, timedelta
# This is the script cards.py, which will be handling all-things decks
# This includes: getting, creating, editing, finishing, and deleting decks
    

# Utility function to check access for your deck_id
def check_deck_view_access(mydb, deck_id, username): 
    # check if user is admin----------------------------
    mycursor = mydb.cursor()
    if admin.check_is_admin(mydb, username) == True:
        return True 


    # check if user has view access----------------------
    mycursor.execute(
        """
        SELECT 
            deckId, username, accessType
        FROM access 
        WHERE deckId = %s
        """, (deck_id,))
    
    result = mycursor.fetchall()
    mycursor.close()
    mydb.commit()

    for row in result:
        if (row[1] == username and (row[2] == "view" or row[2] == "edit")):
            return True
    return False

# Utility function to check access for your deck_id
def check_deck_edit_access(mydb, deck_id, username):
    
    # check if user is admin----------------------------
    mycursor = mydb.cursor()
    if admin.check_is_admin(mydb, username) == True:
        return True 

    # check if user has edit access----------------------------

    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            deckId, username, accessType
        FROM access WHERE deckId = %s
        """, (deck_id,))
    
    result = mycursor.fetchall()
    mycursor.close()
    mydb.commit()
    for row in result:
        if (row[1] == username and row[2] == "edit"):
            return True
    return False

# Retrieve all decks that the user has view or edit access to
def get_decks_list(mydb, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            deck.deckid, deck.deckName, 
            deck.deckdescription, 
            (SELECT MIN(cardDue) FROM card WHERE card.deckid = deck.deckid AND card.cardIsFinished = '0') as nearestDue, 
            (select GROUP_CONCAT(DISTINCT card.cardColor) as cardColors FROM card WHERE card.deckid = deck.deckid GROUP BY deck.deckid) as card_colors,
            access.accessType
        FROM deck, access
        WHERE deck.deckid = access.deckid
              AND access.username = %s
        """, (username,))
    
    result = mycursor.fetchall()
    for i, r in enumerate(result):
        if r[3] != None:
            formatted_nearest_due = r[3].strftime("%Y-%m-%d")
            #formatted_nearest_due = int(r[3])
        else:
            formatted_nearest_due = ""

        if r[4] != None:
            card_colors = r[4].split(',')
        else:
            card_colors = []
            
        result[i] = {
            "deckId": int(r[0]),
            "deckName": r[1],
            "deckDescription": r[2],
            "nearestDue" : formatted_nearest_due,
            "cardColors" : card_colors,
            "editable" : r[5] == "edit"
        }
        #print(result[i]) 
    mycursor.close()
    mydb.commit()
    return result
    #---------------------------------------


# Edits a deck using deck_info
# must also check for edit access of that deck_id
# returns True or False
def edit_deck(mydb, deck_info, username):

    if check_deck_edit_access(mydb, int(deck_info["deckId"]), username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
            UPDATE deck
            SET deckName = %s,
                deckDescription = %s

            WHERE deckid = %s
            """,
            (deck_info["deckName"], deck_info["deckDescription"], int(deck_info["deckId"]))
        )
        mycursor.close()
        mydb.commit()
        return True
    return False



# deletes a deck using deck_id
# must also check for edit access of that deck_id
# returns True or False
def delete_deck(mydb, deck_id, username):
    if check_deck_edit_access(mydb, deck_id, username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                DELETE FROM deck
                WHERE deckid = %s
                """, (deck_id,)
        )
        mycursor.close()
        mydb.commit()
        return True
    return False



# Generates a unique sharecode, inserts to share table, and returns it
# must also check for edit access of that deck_id to get sharecode
# returns share code, or false

# get_sharecode generates a unique sharecode.
# must check giver's username access
# use any randomization you wish
# generate an expiration time as well
# must be unique (can't have duplicate codes, lol)
def get_sharecode(mydb, access_type, deck_id, username):
    
    if check_deck_edit_access(mydb, deck_id, username) == True:
        expires = 3
        length = 15
        characters = string.ascii_letters + string.digits
        # print(characters) = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
        unique_code = ''.join(random.choice(characters) for i in range(length))

        mycursor = mydb.cursor()
        mycursor.execute(
        """
        SELECT * 
        FROM share
        WHERE code = %s 
        """, (unique_code, ))
        result = mycursor.fetchall()
        mycursor.close()
        mydb.commit()

        if not result:
            mycursor = mydb.cursor()
            mycursor.execute(
            """
            INSERT INTO share(code, deckid, type, expires) values
                (%s, %s, %s, DATE_ADD(NOW(), INTERVAL %s MINUTE))

            """, (unique_code, deck_id, access_type, expires))
            mycursor.close()
            mydb.commit()
            return unique_code

    return False



# Recieves a sharecode and allow access
# must check sharecode integrity (expiration and deck exists)
# then a new access record onto access table
# returns if success = dict(deckId: 2)// if false = {}

# check that code exists, hasn't expired, and that the code giver still has edit access
# add access to the user
def recieve_sharecode(mydb, sharecode, username):
    select_cursor = mydb.cursor()
    select_cursor.execute(
        """
        SELECT code, deckid, type, expires
        FROM share
        WHERE code = %s
        """, (sharecode, ))

    result = select_cursor.fetchall()
    select_cursor.close()
    mydb.commit()

    if not result:
        return False
    
    else:
        for i, r in enumerate(result):

            #check expires 
            receive_code_time = datetime.now()
            share_code_time = r[3]
            delta_time_min = (receive_code_time - share_code_time).total_seconds() / 60

            if delta_time_min <= 3:
                #insert into access table
                insert_cursor = mydb.cursor()

                # Check to prevent duplicate access - three possible cases
                # Case 1, already exists, no action
                # Case 2, not exist, insert
                insert_cursor.execute(
                """
                SELECT * FROM access
                WHERE
                    username = %s AND
                    deckId = %s AND
                    accessType = %s;
                """, (username, r[1], r[2]))
                should_be_empty = insert_cursor.fetchall()
                if should_be_empty != []:
                    return {
                        "deckId": int(r[1])
                    }


                insert_cursor.execute(
                """
                INSERT INTO access(username, deckId, accessType) values
                    (%s, %s, %s)

                """, (username, r[1], r[2]))
                insert_cursor.close()
                mydb.commit()
                return {
                    "deckId": int(r[1])
                }
    return False
    

def create_deck(mydb, deck_info, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        INSERT INTO `deck` (`deckName`, `deckDescription`) 
        VALUES (%s, %s)
        """,
        (deck_info["deckName"], deck_info["deckDescription"])
    )

    deck_id = mycursor.lastrowid
    addAccess(mydb, deck_id, "edit", username)
    return True


'''
Note that this will not generate a duplicate access record when another already exists. 
If the target access already exists, simply do nothing and return true. 
(also, this function does not need to check access for the access giver. 
Since this function will be used only by create_deck and recieve_sharecode, 
both of these functions will check the giver's access beforehand)
'''
def addAccess(mydb, deck_id, access_type, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            username, deckid, accessType 
        FROM access
        WHERE username = %s
            AND deckid = %s
            AND accessType = %s
        """, (username, deck_id, access_type))
    
    result = mycursor.fetchall()
    mycursor.close()
    mydb.commit()

    if not result:
        mycursor = mydb.cursor()
        mycursor.execute(
            """
            INSERT INTO `access` (`username`, `deckId`, `accessType`) 
            VALUES (%s, %s, %s)
            """,
            (username, deck_id, access_type)
        )
        mycursor.close()
        mydb.commit()

    #else:
        #print("record exists")
    return True


def get_access_list(mydb, deck_id, username):
    if check_deck_edit_access(mydb, deck_id, username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                SELECT username, accessType FROM access
                WHERE deckId = %s AND username != %s
            """, (deck_id, username)
            )

        result = {}
        for i, r in enumerate(mycursor.fetchall()):
            if r[1] not in result:
                result[r[1]] = []
            result[r[1]].append(r[0])
        
        mycursor.close()
        mydb.commit()
        return result
    return False


def remove_access(mydb, deck_id, removee_username, remover_username):
    if check_deck_edit_access(mydb, deck_id, remover_username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                DELETE FROM access
                WHERE deckid = %s
                    AND username = %s
                """, (deck_id, removee_username)
            )
        mycursor.close()
        mydb.commit()
        return True
    else:
        print("remover_username does not have access")
    return False
