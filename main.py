import functions

def main():
    CreateOrLog = input("What would you like to do LOGIN(1)/SIGNUP(2) ")
    
    #Log into userxx
    if CreateOrLog == "1":
        username = input("What is the username: ")
        realUserName = username
        password = input("What is the password: ")
        username, password = functions.encrypt_string_sha256(username) , functions.encrypt_string_sha256(password)
        functions.login(username,password,realUserName)

    #Create a newUser
    elif CreateOrLog == "2":
        username = input("What is the username: ")
        password = input("What is the password: ")
        functions.sign_up(username,password)




if __name__ == "__main__":
    main()