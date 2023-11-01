# import os
import json


# def download():
#     os.system('curl -L -o db.json "https://raw.githubusercontent.com/maksimtall/FIG-db/main/db.json"')


def openFile(fileName, mode):
    return open(fileName, mode)


def close(filein):
    filein.close()


def listAll(filein):
    for x in filein:
        print(x)


def getUserObj(filein):
    load = json.load(filein)
    return load


def overwrite(filein):
    filein.write("")


def write(data, filein):
    filein.write(data)
    filein.close


def WriteToJSON(obj, filein):
    filein.write(json.dumps(obj))


def newUserWrite(name, userInput, email, password, birth, file, userObj):
    # WriteToJSON(newFile, file)
    newUserObj = dict(
        name=name, user=userInput, email=email, password=password, birth=birth
    )

    file = openFile("db.json", "r")
    close(file)
    # print("prije", userObj)
    # userObj.update(dict(userInput=newUserObj))
    userObj[userInput] = newUserObj
    # print("poslje", userObj)


def login(file):
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


def WriteUser(askObj):
    newUserObj = askObj.get("newUser")
    # print(newUser)
    # LoginLoop()
    fileToWrite = openFile("db.json", "wt")
    WriteToJSON(newUserObj, fileToWrite)
    # userObj = getUserObj(file)
    # print(userObj)
    # if newUser:
    #     user = newUser.get("user")
    #     newFile = userObj[user] = newUser
    #     WriteToJSON(newFile, file)
    close(fileToWrite)
    print(askObj.get("signup"))


def userCheck(user):
    file = openFile("db.json", "r")
    fileObj = getUserObj(file)
    if fileObj.get(user) is None:
        return dict(userExt="Not fine")
    else:
        return dict(userExt="fine")
