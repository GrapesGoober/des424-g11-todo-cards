
def check_is_admin(mydb, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            username 
        FROM admin 
        WHERE username = %s
        """, (username,))
    is_admin = mycursor.fetchall()

    if is_admin:
        #print("is admin")
        mycursor.close()
        mydb.commit()
        return True
    return False


def delete_user(mydb, user, admin):
    if check_is_admin(mydb, admin) == True:
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                DELETE FROM user
                WHERE username = %s
                """, (user,)
        )
        mycursor.close()
        mydb.commit()
        return True
    return False


def admin_get_everything(mydb, username):
    if check_is_admin(mydb, username) == False:
        return False
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT deckid, deckName FROM deck ORDER BY deck.deckid")
    decks_list = mycursor.fetchall()
    for i, deck in enumerate(decks_list):
        decks_list[i] = {
            "deckId": deck[0],
            "deckName": deck[1]
        }
        
    mycursor.execute("SELECT username FROM user ORDER BY username")
    users = mycursor.fetchall()
    for i, user in enumerate(users):
        users[i] = user[0]

    mycursor.execute("SELECT accessId, username, deckid, accessType FROM access ORDER BY accessId")
    access_list = mycursor.fetchall()
    for i, access in enumerate(access_list):
        access_list[i] = {
            "accessId": access[0],
            "username": access[1],
            "deckId": access[2],
            "accessType": access[3],
        }

    output = {
        "deckslist": decks_list,
        "users": users,
        "accesslist": access_list
    }

    mycursor.close()
    mydb.commit()
    return output

