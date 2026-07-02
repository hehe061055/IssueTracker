from DatabaseManager import run
from UserManager import ListUsers, AddUser, EditUser, RemoveUser
import os
import time


global message
message = ""

def cls():
    os.system("cls")




# USERS - line 18 to 85

def displayUsers():
    cls()
    data = ListUsers()
    global message
    if message!="":
        print(message+"\n\n")
        message=False

    print(" __________________________________________________________\n|ID____|Username______________________|Role________________|\n|      |                              |                    |")#40_ 
    for USER in data:
        ID = USER[0]
        NAME = USER[1]
        ROLE = USER[2]
        line = f"|{ID:_<6}|{NAME:_<30}|{ROLE:_<20}|"
        print(line)
        continue


def userPage():
    displayUsers()    
    userIn = int(input("\n\n--Users--\n1. Add User\n2. Edit User\n3. Remove User\n4. Return\n\nPlease select a number:\n>"))
    if userIn==4:
        return 1
    elif userIn==1:
        displayUsers()
        username = input("Name of User:")
        role = input("Role of User:")
        AddUser(username, role)
        displayUsers()
    elif userIn==2:
        displayUsers()
        ID = int(input("Which user do you wish to edit? (Give their ID):\n>"))
        USER = run(f"SELECT users.name, users.role FROM users WHERE users.id=={ID}", "fetch")[0]
        displayUsers()
        print(USER)
        userIn = int(input(f"1. Edit Username({USER[0]})\n2. Edit Role({USER[1]})\n3. Edit Both\n\n>"))
        displayUsers()
        if userIn==1:
            newName = input(f"What is the new username for {USER[0]}?\n>")
            EditUser(ID, newName)
        elif userIn==2:
            newRole = input(f"What is the new Role of {USER[0]}, from {USER[1]}?\n>")
            EditUser(ID, role=newRole)
        elif userIn==3:
            newName = input(f"What is the new username for {USER[0]}?\n>")
            newRole = input(f"What is the new Role of {USER[0]}, from {USER[1]}?\n>")
            EditUser(ID, newName, newRole)
    elif userIn==3:
        displayUsers()
        ID = input("Which user do you wish to remove? (Give their ID or type * to PERMANENTLY DELETE all users):\n>")
        if ID=="*":
            ID="*"
            confirm = input(f"Are you sure you wish to PERMANENTLY REMOVE all users? (Y/N)").lower()
        else:
            ID=int(ID)
            USER = run(f"SELECT users.name, users.role FROM users WHERE users.id=={ID}", "fetch")[0]
            confirm = input(f"Are you sure you wish to remove {USER[0]} with the role {USER[1]}, and ID {ID}? (Y/N)").lower()

        if confirm=="y":
            RemoveUser(ID)
        else:
            print(f"Cancelling. {USER[0]} has not been removed. (Recieved N or unknown character)"if ID!="*"else"Cancelling. No users have been removed. (Recieved N or unknown character)")

    else:
        global message
        message = "invalid input"
        
    return 0










while True:
    cls()
    selection = int(input("\n\n--Menu--\n1. Users\n2. Projects\n3. Issues\n4. Exit\n\nPlease select a number:\n>"))
    if selection==1:
        cls()
        a = 0
        while a==0:
            a = userPage()
    elif selection==2:
        break
    elif selection==3:
        break
    elif selection==4:
        exit()
    else:
        print("Invalid Selection")
        continue