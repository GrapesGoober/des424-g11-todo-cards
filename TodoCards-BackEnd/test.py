import user
import decks
import cards
import inspect
import admin

# result = user.hash_password("password1234")
# print(result)
# print(user.is_password_correct(result, "password1234"))

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="TodoCards"
)
'''
assert cards.check_card_view_access(mydb, 7, "dean") == True
assert cards.check_card_view_access(mydb, 7, "fay") == True
assert cards.check_card_view_access(mydb, 4, "dean") == True
assert cards.check_card_view_access(mydb, 4, "fay") == False
assert cards.check_card_view_access(mydb, 4, "ajarn") == True
#assert cards.check_card_view_access(mydb, 1, "ajarn") == False

assert cards.check_subcard_view_access(mydb, 2, "bob") == False
assert cards.check_subcard_view_access(mydb, 3, "ajarn") == True
assert cards.check_subcard_view_access(mydb, 4, "dean") == True
assert cards.check_subcard_view_access(mydb, 3, "ajarn") == True
#assert cards.check_subcard_view_access(mydb, 1, "ajarn") == False

assert cards.check_card_edit_access(mydb, 7, "dean") == True
assert cards.check_card_edit_access(mydb, 7, "fay") == True
assert cards.check_card_edit_access(mydb, 4, "dean") == True
assert cards.check_card_edit_access(mydb, 4, "fay") == False
assert cards.check_card_edit_access(mydb, 4, "ajarn") == False
assert cards.check_card_edit_access(mydb, 7, "ajarn") == True
assert cards.check_card_edit_access(mydb, 1, "ajarn") == False

assert cards.check_subcard_edit_access(mydb, 2, "bob") == False
assert cards.check_subcard_edit_access(mydb, 3, "dean") == True
assert cards.check_subcard_edit_access(mydb, 4, "dean") == True
assert cards.check_subcard_edit_access(mydb, 6, "ajarn") == False
assert cards.check_subcard_edit_access(mydb, 5, "ajarn") == True
assert cards.check_subcard_edit_access(mydb, 1, "ajarn") == False


#decks.get_decks_list(mydb, "dean")
#cards.get_cards_list(mydb, 4, "dean")
#cards.get_subcards_list(mydb, 4, "fay")
#cards.get_subcards_list(mydb, 8, "cindy")

assert cards.finish_card(mydb, 4, "fay") == False
'''


'''
assert cards.delete_card(mydb, 9, "cindy") == False
#assert cards.delete_card(mydb, 9, "dean") == True
assert cards.delete_card(mydb, 11, "dean") == False
assert cards.delete_card(mydb, 12, "dean") == True
'''


'''
cards.delete_subcard(mydb, 10, "cindy")
cards.delete_subcard(mydb, 8, "dean")
'''

'''
assert decks.delete_deck(mydb, 8, "dean") == False
assert decks.delete_deck(mydb, 9, "ajarn") == False
#assert decks.delete_deck(mydb, 8, "ajarn") == True


assert cards.finish_card(mydb, 11, "dean") == False
assert cards.finish_card(mydb, 6, "cindy") == False
assert cards.finish_card(mydb, 6, "fay") == True
assert cards.finish_card(mydb, 11, "cindy") == True
assert cards.finish_card(mydb, 7, "ajarn") == True


assert cards.finish_subcard(mydb, 4, "ajarn") == False
assert cards.finish_subcard(mydb, 6, "ajarn") == False
assert cards.finish_subcard(mydb, 6, "cindy") == True
assert cards.finish_subcard(mydb, 4, "dean") == True

#decks.get_decks_list(mydb, "bob")

#print(decks.delete_deck(mydb, 10, "ajarn"))
assert cards.get_cards_list(mydb, 3, "dean") == False

#print(cards.get_subcards_list(mydb, 4, "dean"))


#print(decks.get_decks_list(mydb, "dean"))
'''

'''
assert cards.edit_card(mydb, {"cardId": 5, 
                       "deckId" : 4,
                       "cardName": "deanCard2newwww",
                       "cardDescription": "Hello Mars",
                       "cardDue": "2023-11-30",
                       "cardIsFinished": "1",
                       "cardColor": "lightblue"},
                "fay") == True
'''


# assert cards.edit_subcard(mydb, {"subcardId": 3, 
#                                 "cardId": 4,
#                                 "subcardName" : "deancard1subcard1New",
#                                 "subcardIsFinished": "0"},
#                                 "dean") == True

# assert decks.edit_deck(mydb, {"deckId": 3, 
#                             "deckName": "cindyDecktestEdit",
#                             "deckDescription" : "ayo aloha"},
#                             "dean") == False

# assert decks.edit_deck(mydb, {"deckId": 3, 
#                             "deckName": "cindyDecktestEdit",
#                             "deckDescription" : "i love nicki minaj"},
#                             "cindy") == True


# assert cards.create_card(mydb, 4, {"cardName": "deanCard3",
#                                 "cardDescription": "testAdding",
#                                 "cardDue": "2023-11-30",
#                                 "cardIsFinished": "1",
#                                 "cardColor": "pink"},
#                                  "ajarn") == False
'''
assert cards.create_card(mydb, 4, {"cardName": "deanCard4",
                                "cardDescription": "testAdding2",
                                "cardDue": "2023-11-20",
                                "cardIsFinished": "0",
                                "cardColor": "lightblue"},
                                 "dean") == True
'''


assert cards.create_subcard(mydb, 8, {"subcardName": "cindyCard1Subcard3",
                                    "subcardIsFinished": "0"},
                                    "dean") == False

assert cards.create_subcard(mydb, 8, {"subcardName": "cindyCard1Subcard3",
                                    "subcardIsFinished": "0"},
                                    "fay") == False
'''
assert cards.create_subcard(mydb, 8, {"subcardName": "cindyCard1Subcard4",
                                    "subcardIsFinished": "1"},
                                    "cindy") == True
'''

'''
decks.create_deck(mydb, 
                    {"deckName": "ajarnDeck1", "deckDescription": "UwU"}, 
                    {"accessType": "edit"},
                    "ajarn") 
'''
#assert decks.delete_deck(mydb, 15, "ajarn") == False



'''
decks.create_deck(mydb, 
                    {"deckName": "ajarnDeckforStudentToview", "deckDescription": "UwU"},
                    {
                        "bob" : "edit",
                        "cindy" : "edit",
                        "dean" : "edit",
                        "fay" : "edit"
                    },
                    "ajarn")
'''


#decks.removeAccess(mydb, 18, "cindy", "bob")



assert decks.check_deck_view_access(mydb, 5, "dean") == False
assert decks.check_deck_view_access(mydb, 14, "admin1") == True

#print(decks.check_deck_view_access(mydb, 5, "admin1"))

#assert decks.check_deck_edit_access(mydb, 5, "fay") == True


# assert decks.check_deck_edit_access(mydb, 13, "admin2") == True


assert admin.delete_user(mydb, "testdelete3", "ajarn") == False


# print(admin.admin_get_everything(mydb, "admin3"))

# admin.check_is_admin(mydb, "admin1") == True
# admin.check_is_admin(mydb, "admin2") == True
# admin.check_is_admin(mydb, "admin3") == True
# admin.check_is_admin(mydb, "admin4") == True




