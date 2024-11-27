# This is the script app.py, which is the entry point for the flask app
# This file contains the logic for routes, sessions, handling requests
# This file does not contain the logic for handling database queries & business logic

from flask import Flask, request, jsonify, session
import mysql.connector
import cards, user, decks, admin, dashboard

# sets up some flask stuff (oh, and CORS too)
app = Flask(__name__)
app.secret_key = "some really useless key lol"

# a preliminary check for login status, only excluded for non-priviledged requests
@app.before_request
def check_login():
    # only apply to previledged requests
    if request.endpoint not in ['login', 'logout', 'ping', 'signup']:
        # simply check for username status (if it's set)
        if "username" not in session:
            return jsonify(False)
        
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="user",
        password="user123",
        database="TodoCards"
    )

def admin_connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="superadmin",
        password="superadmin123",
        database="TodoCards"
    )

# a debugging route that responds with "pong"
@app.route("/api/ping", methods=["POST"])
def ping():
    response = jsonify({"message": "pong"})
    return response

# authenticates a user and sets a session variable "userid"
@app.route("/api/login", methods=["POST"])
def login():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    username = jsonbody.get("username")
    password = jsonbody.get("password")

    # login function returns either true or false
    status = user.login(mydb, username, password)
    if status: 
        session["username"] = username
    elif "username" in session:
        session.pop("username")

    if admin.check_is_admin(mydb, username):
        status = "isAdmin"

    mydb.close()
    return jsonify(status)

# removes login info from session cookie
@app.route("/api/logout", methods=["POST"])
def logout():
    if "username" in session:
        session.pop('username', default=None)
    return "null"

@app.route("/api/signup", methods=["POST"])
def signup():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    username = jsonbody.get("username")
    password = jsonbody.get("password")

    status = user.signup(mydb, username, password)
    if status: 
        session["username"] = username
    elif "username" in session:
        session.pop("username")
    mydb.close()

    return jsonify(status)

# retrieve a list of decks
@app.route("/api/get-decks-list", methods=["POST"])
def get_decks_list():
    mydb = connect_to_db()
    username = session.get("username")
    result = decks.get_decks_list(mydb, username)
    mydb.close()
    return jsonify(result)

# retrieve a list of data for dashboard
@app.route("/api/get-dashboard-data", methods=["POST"])
def get_dashboard():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    deck_id = jsonbody.get("deckId")
    allCount = dashboard.get_all_cards(mydb, deck_id)
    finishCount = dashboard.get_finished_cards(mydb, deck_id)
    mydb.close()
    result = [allCount, finishCount]
    return jsonify(result)

# retrieve a list of cards using deckId. 
@app.route("/api/get-cards-list", methods=["POST"])
def get_cards_list():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    deck_id = jsonbody.get("deckId")
    username = session.get("username")
    result = cards.get_cards_list(mydb, deck_id, username)
    mydb.close()
    return jsonify(result)

# retrieve a list of subcards using cardId. 
@app.route("/api/get-subcards-list", methods=["POST"])
def get_subcards_list():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    card_id = jsonbody.get("cardId")
    username = session.get("username")
    result = cards.get_subcards_list(mydb, card_id, username)
    mydb.close()
    return jsonify(result)

@app.route("/api/finish-card", methods=["POST"])
def finish_card():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    card_id = jsonbody.get("cardId")
    is_unfinished = jsonbody.get("isUnfinished")
    username = session.get("username")
    result = cards.finish_card(mydb, card_id, is_unfinished, username)
    mydb.close()
    return jsonify(result)

@app.route("/api/finish-subcard", methods=["POST"])
def finish_subcard():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    subcard_id = jsonbody.get("subcardId")
    is_unfinished = jsonbody.get("isUnfinished")
    username = session.get("username")
    result = cards.finish_subcard(mydb, subcard_id, is_unfinished, username)
    mydb.close()
    return jsonify(result)

@app.route("/api/edit-deck", methods=["POST"])
def edit_deck():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    deck_info = jsonbody.get("deckInfo")
    username = session.get("username")
    status = decks.edit_deck(mydb, deck_info, username)
    mydb.close()
    return jsonify(status)

@app.route("/api/edit-card", methods=["POST"])
def edit_card():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    card_info = jsonbody.get("cardInfo")
    username = session.get("username")
    status = cards.edit_card(mydb, card_info, username)
    mydb.close()
    return jsonify(status)

@app.route("/api/edit-subcard", methods=["POST"])
def edit_subcard():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    subcard_info = jsonbody.get("subcardInfo")
    username = session.get("username")
    status = cards.edit_subcard(mydb, subcard_info, username)
    return jsonify(status)

@app.route("/api/create-deck", methods=["POST"])
def create_deck():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    deck_info = jsonbody.get("deckInfo")
    username = session.get("username")
    status = decks.create_deck(mydb, deck_info, username)
    mydb.close()
    return jsonify(status)

@app.route("/api/create-card", methods=["POST"])
def create_card():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    card_info = jsonbody.get("cardInfo")
    deck_id = jsonbody.get("deckId") 
    username = session.get("username")
    status = cards.create_card(mydb, deck_id, card_info, username)
    mydb.close()
    return jsonify(status)

@app.route("/api/create-subcard", methods=["POST"])
def create_subcard():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    subcard_info = jsonbody.get("subcardInfo")
    card_id = jsonbody.get("cardId")
    username = session.get("username")
    status = cards.create_subcard(mydb, card_id, subcard_info, username)
    mydb.close()
    return jsonify(status)

@app.route("/api/delete-deck", methods=["POST"])
def delete_deck():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    deck_id = jsonbody.get("deckId")
    username = session.get("username")
    status = decks.delete_deck(mydb, deck_id, username)
    mydb.close()
    return jsonify(status)

@app.route("/api/delete-card", methods=["POST"])
def delete_card():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    card_id = jsonbody.get("cardId")
    username = session.get("username")
    status = cards.delete_card(mydb, card_id, username)
    mydb.close()
    return jsonify(status)

@app.route("/api/delete-subcard", methods=["POST"])
def delete_subcard():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    subcard_id = jsonbody.get("subcardId")
    username = session.get("username")
    status = cards.delete_subcard(mydb, subcard_id, username)
    mydb.close()
    return jsonify(status)

@app.route("/api/get-sharecode", methods=["POST"])
def get_sharecode():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    deck_id = jsonbody.get("deckId")
    access_type = jsonbody.get("accessType")
    username = session.get("username")
    result = decks.get_sharecode(mydb, access_type, deck_id, username)
    mydb.close()
    return jsonify(result)

@app.route("/api/get-access-list", methods=["POST"])
def get_access_list():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    deck_id = jsonbody.get("deckId")
    username = session.get("username")
    result = decks.get_access_list(mydb, deck_id, username)
    mydb.close()
    return jsonify(result)

@app.route("/api/remove-access", methods=["POST"])
def remove_access():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    deck_id = jsonbody.get("deckId")
    removee = jsonbody.get("username")
    remover = session.get("username")
    result = decks.remove_access(mydb, deck_id, removee, remover)
    mydb.close()
    return jsonify(result)

# Handles sharing
@app.route("/api/recieve-sharecode", methods=["POST"])
def recieve_sharecode():
    mydb = connect_to_db()
    jsonbody = request.get_json()
    sharecode = jsonbody.get("sharecode")
    print(sharecode)
    username = session.get("username")
    result = decks.recieve_sharecode(mydb, sharecode, username)
    mydb.close()
    return jsonify(result)

@app.route("/api/get-everything", methods=["POST"])
def get_everything():
    mydb = admin_connect_to_db()
    username = session.get("username")
    result = admin.admin_get_everything(mydb, username)
    mydb.close()
    return jsonify(result)

@app.route("/api/delete-user", methods=["POST"])
def delete_user():
    mydb = admin_connect_to_db()
    jsonbody = request.get_json()
    the_unlucky_user = jsonbody.get("username")
    admin_username = session.get("username")
    print(the_unlucky_user)
    result = admin.delete_user(mydb, the_unlucky_user, admin_username)
    mydb.close()
    return jsonify(result)

# the entry point of the code
if __name__ == "__main__":
    # runs app, default to 127.0.0.1 port 5000
    app.run(debug=True, host='0.0.0.0')