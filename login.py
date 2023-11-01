from dbUse import *
from inout import *

run = 1
# from inout import ask5

# ask()
# download()
# readall()

# file = openFile("db.json", "r")

# listAll(file)
# jsonDic = getUserObj(file)
# print(jsonDic)


def LoginLoop():
    askObj = ask()
    if askObj:
        if askObj.get("error") is not None:
            print(askObj.get("error"))
            LoginLoop()
        elif askObj.get("exit") is not None:
            print(askObj.get("exit"))
        elif askObj.get("signup") is not None:
            WriteUser(askObj)
            LoginLoop()
        else:
            print("Hello ", askObj.get("name"))

def loginstart():
    LoginLoop()

# ask()
# close(file)
# overwrite(file)
