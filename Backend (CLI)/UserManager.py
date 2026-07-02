from DatabaseManager import run



def ListUsers():
    data = (run("SELECT * FROM users","fetch"))
    
    return data

def AddUser(name, role):
    return (run(f"INSERT INTO users (name, role) VALUES ('{name}','{role}')","change"))
    

def EditUser(id, name="", role=""):
    run(f"UPDATE users SET {("name = '"+name+("' ,"if role!=""else"'"))if name!="" else ""}{("role = '"+role+"'")if role!="" else ""} WHERE users.id={id}", "change")

def RemoveUser(id):
    run(f"DELETE FROM users {("WHERE users.id={id}")if id!="*"else""}", "change")