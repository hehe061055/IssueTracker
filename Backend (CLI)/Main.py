from DatabaseManager import *
import os
import time

global message;message = ""

def cls():
    os.system("cls")


# USERS - line 16 to 81 ================================================================================================================================

def displayUsers():
    cls()
    data = UserCmds.ListUsers()
    global message
    if message!="":
        print(message+"\n\n")
        message=False

    print(" __________________________________________________________\n|ID____|Username______________________|Role________________|\n|      |                              |                    |")#40_ 
    for USER in data:
        ID = USER[0]
        NAME = USER[1]
        ROLE = USER[2]
        line = f"|{ID: <6}|{NAME: <30}|{ROLE: <20}|".replace(" ","_")
        print(line)
        continue
def userPage(): #-------------------------------------------------------------------------------------------------------------------------------------------
    
    displayUsers()    
    userIn = int(input("\n\n--Users--\n1. Add User\n2. Edit User\n3. Remove User\n4. Return\n\nPlease select a number:\n>"))
    if userIn==4:
        return 1
    elif userIn==1:
        os.system("title Add User")
        displayUsers()
        username = input("Name of User:")
        role = input("Role of User:")
        UserCmds.AddUser(username, role)
        displayUsers()
    elif userIn==2:
        os.system("title Edit User")
        displayUsers()
        ID = int(input("Which user do you wish to edit? (Give their ID):\n>"))
        USER = Run(f"SELECT users.name, users.role FROM users WHERE users.id={ID}", "fetch")[0]
        displayUsers()
        print(USER)
        userIn = int(input(f"1. Edit Username({USER[0]})\n2. Edit Role({USER[1]})\n3. Edit Both\n\n>"))
        displayUsers()
        if userIn==1:
            newName = input(f"What is the new username for {USER[0]}?\n>")
            UserCmds.EditUser(ID, newName)
        elif userIn==2:
            newRole = input(f"What is the new Role of {USER[0]}, from {USER[1]}?\n>")
            UserCmds.EditUser(ID, role=newRole)
        elif userIn==3:
            newName = input(f"What is the new username for {USER[0]}?\n>")
            newRole = input(f"What is the new Role of {USER[0]}, from {USER[1]}?\n>")
            UserCmds.EditUser(ID, newName, newRole)
    elif userIn==3:
        os.system("title Remove User")
        displayUsers()
        ID = input("Which user do you wish to remove? (Give their ID or type * to PERMANENTLY DELETE all users):\n>")
        if ID=="*":
            ID="*"
            confirm = input(f"Are you sure you wish to PERMANENTLY REMOVE all users? (Y/N)").lower()
        else:
            ID=int(ID)
            USER = Run(f"SELECT users.name, users.role FROM users WHERE users.id=={ID}", "fetch")[0]
            confirm = input(f"Are you sure you wish to remove {USER[0]} with the role {USER[1]}, and ID {ID}? (Y/N)").lower()

        if confirm=="y":
            UserCmds.RemoveUser(ID)
        else:
            print(f"Cancelling. {USER[0]} has not been removed. (Recieved N or unknown character)"if ID!="*"else"Cancelling. No users have been removed. (Recieved N or unknown character)")

    else:
        global message
        message = "invalid input"
        
    return 0

# PROJECTS - lines 87 to ### ==============================================================================================================================

def displayProjects():
    cls()
    data = ProjectCmds.ListProjects()
    global message
    if message!="":
        print(message+"\n\n")
        message=False

    print(" ______________________________________________________________________________________________________________________\n|ID____|Name__________________________|Description_____________________________________________________________________|\n|      |                              |                                                                                |")#40_ 
    for PROJ in data:
        ID = PROJ[0]
        NAME = PROJ[1]
        DESC = PROJ[2]
        line = f"|{ID: <6}|{NAME: <30}|{DESC: <80}|".replace(" ","_")
        print(line)
        continue


def projPage(): # -------------------------------------------------------------------------------------------------------------------------------------------
    
    displayProjects() 
    userIn = int(input("\n\n--Projects--\n1. Add Project\n2. Edit Project\n3. Remove Project\n4. Return\n\nPlease select a number:\n>"))
    if userIn==4:
        return 1
    elif userIn==1:
        os.system("title Add Project")
        displayProjects()
        name = input("Name of Project:")
        desc = input("Description of Project:")
        ProjectCmds.AddProject(name, desc)
        displayProjects()
    elif userIn==2:
        os.system("title Edit Projects")
        displayProjects()
        ID = int(input("Which project do you wish to edit? (Give the ID):\n>"))
        PROJ = Run(f"SELECT projects.name, projects.description FROM projects WHERE description.id={ID}", "fetch")[0]
        displayProjects()
        print(PROJ)
        userIn = int(input(f"1. Edit Project Name ({PROJ[0]})\n2. Edit Description ({PROJ[1]})\n3. Edit Both\n\n>"))
        displayProjects()
        if userIn==1:
            newName = input(f"What is the new name for {PROJ[0]}?\n>")
            ProjectCmds.EditProject(ID, newName)
        elif userIn==2:
            newDesc = input(f"What is the new Description of {PROJ[0]}, from {PROJ[1]}?\n>")
            ProjectCmds.EditProject(ID, desc=newDesc)
        elif userIn==3:
            newName = input(f"What is the new name for {PROJ[0]}?\n>")
            newDesc = input(f"What is the new Role of {PROJ[0]}, from {PROJ[1]}?\n>")
            ProjectCmds.EditProject(ID, newName, newDesc)
    elif userIn==3:
        os.system("title Remove Project")
        displayProjects()
        ID = input("Which project do you wish to remove? (Give the ID or type * to PERMANENTLY DELETE all projects):\n>")
        if ID=="*":
            ID="*"
            confirm = input(f"Are you sure you wish to PERMANENTLY REMOVE all projects? (Y/N)").lower()
        else:
            ID=int(ID)
            PROJ = Run(f"SELECT projects.name, projects.description FROM projects WHERE projects.id=={ID}", "fetch")[0]
            confirm = input(f"Are you sure you wish to remove {PROJ[0]} with the description {PROJ[1]}, and ID {ID}? (Y/N)").lower()

        if confirm=="y":
            ProjectCmds.RemoveProject(ID)
        else:
            print(f"Cancelling. {PROJ[0]} has not been removed. (Recieved N or unknown character)"if ID!="*"else"Cancelling. No projects have been removed. (Recieved N or unknown character)")
    
    
    return 0

# ISSUES - lines 158 to ### ==============================================================================================================================

def displayIssues():
    cls()
    data = IssueCmds.ListIssues()
    global message
    if message!="":
        print(message+"\n\n")
        message=False

    print(" ______________________________________________________________________________________________________________________\n|ID____|Name_____________________________|Status______________________________|Priority________________________________|\n|      |                                 |                                    |                                        |")#40_ 
    for ISS in data:
        ID = ISS[0]
        NAME = ISS[1]
        STA = ISS[3]
        PRI = ISS[4]
        line = f"|{ID: <6}|{NAME: <33}|{STA: <36}|{PRI: <40}|".replace(" ","_")
        print(line)
        continue


def IssuesPage(): # -------------------------------------------------------------------------------------------------------------------------------------------
    
    displayIssues() 
    userIn = int(input("\n\n--Issues--\n1. View Issue\n2. Add Issue\n3. Edit Issue\n4. Remove Issue\n5. Return\n\nPlease select a number:\n>"))
    if userIn==5:
        return 1
    elif userIn==1:
        displayIssues()
        ID = int(input("Which Issue do you wish to view in detail? (Give the ID):\n>"))
        ISS = Run(f"SELECT * FROM issues WHERE issues.id={ID}", "fetch")[0]
        global message
        message = (f"ID: {ISS[0]}\nTitle: {ISS[1]}\nDescription: {ISS[2]}\nStatus: {ISS[3]}\nPriority: {ISS[4]}\nTimestamp: {ISS[5]} ({time.ctime(float(ISS[5]))})\nLast Update: {ISS[6]} ({time.ctime(float(ISS[6]))})\nAssigned User: {ISS[7]}")
        

        return 0
    elif userIn==2:
        os.system("title Add Issue")
        displayIssues()
        title = input("Name of Issue:")
        desc = input("Description of Issue:")
        status = input("Status of Issue:")
        priority = input("Priority of Issue:")
        timestamp = time.time()
        lastUpdate = time.time()
        displayUsers()
        assignedUser = input("User assigned to Issue (ID):")
        displayIssues()




        IssueCmds.AddIssue(title, desc, status, priority, timestamp, lastUpdate, assignedUser)
        displayIssues()
    elif userIn==3:
        os.system("title Edit Issues")
        displayIssues()
        ID = int(input("Which Issue do you wish to edit? (Give the ID):\n>"))
        ISS = Run(f"SELECT * FROM issues WHERE issues.id={ID}", "fetch")[0]
        displayIssues()
        print(ISS)
        userIn = int(input(f"1. Edit Issue Name/Desc ({ISS[1]}...)\n2. Edit Issue status/priority ({ISS[3]},{ISS[4]})\n3. Edit All\n\n>"))
        displayIssues()
        print("For any of the selections, leave it blank to skip and keep the current one.")
        if userIn==1:
            newName = input(f"What is the new name for {ISS[1]}?\n>")
            newDesc = input(f"What is the new description for {newName}, from {ISS[2]}?\n>")
            IssueCmds.EditIssue(ID, title=newName, desc=newDesc)
        elif userIn==2:
            newStatus = input(f"What is the new status of {ISS[1]}, from {ISS[3]}?\n>")
            newPriority = input(f"What is the new priority of {ISS[1]} from {ISS[4]}?\n>")
            IssueCmds.EditIssue(ID, status=newStatus, priority=newPriority)
        elif userIn==3:
            newName = input(f"What is the new name for {ISS[1]}?\n>")
            newDesc = input(f"What is the new description for {newName}, from {ISS[2]}?\n>")
            newStatus = input(f"What is the new status of {newName}, from {ISS[3]}?\n>")
            newPriority = input(f"What is the new priority of {newName} from {ISS[4]}?\n>")
            newlastUpdate = time.time()
            displayUsers()
            newUser = input(f"Who is the new assigned user of {newName} from {ISS[5]}?\n>")


            IssueCmds.EditIssue(ID, newName, newDesc, newStatus, newPriority, newlastUpdate, assignedUser=newUser)
    elif userIn==4:
        os.system("title Remove Issue")
        displayIssues()
        ID = input("Which Issue do you wish to remove? (Give the ID or type * to PERMANENTLY DELETE all issues):\n>")
        if ID=="*":
            ID="*"
            confirm = input(f"Are you sure you wish to PERMANENTLY REMOVE all issues? (Y/N)").lower()
        else:
            ID=int(ID)
            ISS = Run(f"SELECT issues.name, issues.description FROM issues WHERE issues.id={ID}", "fetch")[0]
            confirm = input(f"Are you sure you wish to remove {ISS[1]} with the description {ISS[2]}, and ID {ID}? (Y/N)").lower()

        if confirm=="y":
            IssueCmds.RemoveIssue(ID)
        else:
            print(f"Cancelling. {ISS[1]} has not been removed. (Recieved N or unknown character)"if ID!="*"else"Cancelling. No issues have been removed. (Recieved N or unknown character)")
    
    
    return 0













while True:
    try:
        os.system("title Main")
        cls()
        selection = int(input("\n\n--Menu--\n1. Users\n2. Projects\n3. Issues\n4. Exit\n\nPlease select a number:\n>"))
        if selection==1:
            cls()
            a = 0
            while not a:
                os.system("title Users")
                a = userPage()
        elif selection==2:
            cls()
            a = 0
            while not a:
                os.system("title Projects")
                a = projPage()
        elif selection==3:
            cls()
            a = 0
            while not a:
                os.system("title Issues")
                a = IssuesPage()
        elif selection==4:
            exit()
        else:
            print("Invalid Selection")
            continue
    except KeyboardInterrupt:
        print("")