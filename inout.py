from dbUse import *


def ask():
    file = openFile("db.json", "r")
    lisc = input(
        """_____________________________________________________
|                         |                         |
|       1 - Log in        |       2 - Sign in       |
|_________________________|_________________________|
|                                                   |
|               3 - Exit and close                  |
|___________________________________________________|
                      Choice:"""
    )
    if lisc == "1":
        file = openFile("db.json", "r")
        jsonDic = getUserObj(file)
        close(file)
        user = input("User Name:")

        # if 2 in jsonDic.values():
        if jsonDic.get(user) is not None:
            password = input("Password:")
            userObj = jsonDic.get(user)
            if userObj.get("password") == password:
                return userObj
            else:
                return dict(error="Wrong password")
        else:
            return dict(error="Wrong Username")

    elif lisc == "2":
        name = input("Name:")
        userInput = input("Username:")
        userCheckResolver(file, name, userInput)
    elif lisc == "3":
        return dict(exit="Logging out")
    else:
        print("Illegal Operation")
        ask()


def userCheckResolver(file, name, userInput):
    msg = userCheck(userInput)
    if msg == "fine":
        signup(file, name, userInput)
    else:
        print("User Exists")
        ask()


def signup(file, name, userInput):
    email = input("Email:")
    password = input("password:")
    birth = input("Year of birth:")
    userObj = getUserObj(file)
    newUserWrite(name, userInput, email, password, birth, file, userObj)
    return dict(signup="Signup successfull. Try to login", newUser=userObj)


# def WriteNo(name,user,email,password,birth):
#     ToWrite = {'name': name, 'username': user,'email': email,'password': password,'Year of birth': birth}
