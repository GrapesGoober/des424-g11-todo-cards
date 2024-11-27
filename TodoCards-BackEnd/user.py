# This is the script user.py, which will be handling all-things users
# This includes: authentication, changing usernames & password, 
import os, hashlib, hmac
import string

# global variable for consistant salt size
SALT_SIZE = 16

# Authentication function to generate password hash
# Note that the salt is simply concatenated to the hash
def hash_password(password):
    salt = os.urandom(SALT_SIZE)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return f"{int.from_bytes(pw_hash + salt, 'big'):096x}"

# Authentication function to generate password hash
# using indexing to retrieve the salt
def is_password_correct(pw_salt_hash, password):
    byte_hash = bytes.fromhex(pw_salt_hash)
    salt = byte_hash[-SALT_SIZE:]
    pw_hash = byte_hash[:-SALT_SIZE]
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )

# authenticates a user using username and password,
# returns True or False
def login(mydb, username, password):

    with mydb.cursor() as mycursor:
        mycursor.execute(
            """
            SELECT password FROM user WHERE username = %s
            """, (username,))
        
        result = mycursor.fetchall()
        if len(result) != 0:
            return is_password_correct(result[0][0], password)
        else:
            return False

# check for not-duplicate username then insert a new user
# returns True or False
def signup(mydb, username, password):

    hs_pwd = hash_password(password)

    with mydb.cursor() as mycursor:

        mycursor.execute("SELECT COUNT(*) FROM user WHERE username = %s", (username,))
        
        result = mycursor.fetchall()
        if result[0][0] != 0:
            return "username duplicate"
        
        #check if username is valid
        characters = string.ascii_letters + string.digits + "_"
        for i in username:
            if i not in characters:
                return "invalid username"
        
        #check if password is valid
        for i in password:
            if i not in characters:
                return "invalid password"

        mycursor.execute("INSERT INTO user VALUES (%s, %s)", (username, hs_pwd))
        mydb.commit()

        #return login(mydb, username, password)
        return True
    
