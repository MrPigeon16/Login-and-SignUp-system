import hashlib
import os
DB_PATH = "UserDB.txt"
MIN_USERNAME_LEN = 3
MIN_PASSWORD_LEN = 5
GOOD = 1
BAD = 0
FIRST_SPLIT_SIGN = ";"
SECOND_SPLIT_SIGN = "-"

def encrypt_string_sha256(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature



def sign_up(username,password):
    enc_username = encrypt_string_sha256(username)
    if(user_in_db(enc_username)):
        print("THIS USER NAME IS ALREADY EXITSING!!!")
        return BAD
    else:
        if(username_meet_the_req(username) and password_meet_the_req(password)):
            encrypt_user_name, encrypt_password = encrypt_string_sha256(username) , encrypt_string_sha256(password)
            add_to_DB(encrypt_user_name,encrypt_password)
        else:
            print("The password not meet the req, Please try a diffrent password!")
            return BAD

def user_in_db(username):
    the_db = get_db()
    if(username in the_db.keys()):
        return GOOD
    else:
        return BAD
    
    
def username_meet_the_req(username):
    if len(username) > MIN_USERNAME_LEN:
        return GOOD
    else:
        return BAD
    
def password_meet_the_req(password):
    
    if len(password) > MIN_USERNAME_LEN:
        return GOOD
    else: 
        return BAD
    
def add_to_DB(usnername,password):
    with open(DB_PATH,"a") as DB:
        DB.write(f"{usnername}-{password};")
        return GOOD



#--------------------------------#


def login(username,password,realUsername):
    
    
    username_and_password_db = get_db()
    try:
        if(username_and_password_db[username] == password):
            print(f"Welcome {realUsername}!")
            return GOOD
        
    except Exception as e:
        print("There is no such user with that NAME, BUT you can create one with this name!")
            

    else:
        print("One of the inputs are wrong")
        return BAD
            

def get_db():
    username_And_Passwords = {}
    with open(DB_PATH,"r") as DB:
        x = DB.read().split(";")
        x.pop(-1)
        for i in x:
            username_And_Passwords[(i.split("-"))[0]] = (i.split("-"))[1]
    return username_And_Passwords
