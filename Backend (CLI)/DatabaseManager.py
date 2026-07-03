import sqlite3


DB = sqlite3.connect('DATABASE.db')





def Run(SQL, type):
    Cursor = DB.cursor()

    print("Executing: "+SQL)

    if type=="fetch":
        Cursor.execute(SQL)
        data = Cursor.fetchall()
    elif type=="change":
        data = Cursor.execute(SQL)
    DB.commit()
    return data

class UserCmds:
    def ListUsers(Filter="", OrderBy=""):
        data = (Run(f"SELECT * FROM users{(f" WHERE name LIKE '%{Filter}%' ")if Filter!=""else""}{f" ORDER BY {OrderBy}"if OrderBy!=""else""}","fetch"))
        return data
    def AddUser(name, role):
        return (Run(f"INSERT INTO users (name, role) VALUES ('{name}','{role}')","change"))
    def EditUser(id, name="", role=""):
        Run(f"UPDATE users SET {("name = '"+name+("' ,"if role!=""else"'"))if name!="" else ""}{("role = '"+role+"'")if role!="" else ""} WHERE users.id={id}", "change")
    def RemoveUser(id):
        Run(f"DELETE FROM users {(f"WHERE users.id={id}")if id!="*"else""}", "change")


class ProjectCmds:
    def ListProjects(Filter="", OrderBy=""):
        data = (Run(f"SELECT * FROM projects{(f" WHERE name LIKE '%{Filter}%' ")if Filter!=""else""}{f" ORDER BY {OrderBy}"if OrderBy!=""else""}","fetch"))
        return data
    def AddProject(name, desc):
        return (Run(f"INSERT INTO projects (name, description) VALUES ('{name}','{desc}')","change"))
    def EditProject(id, name="", desc=""):
        Run(f"UPDATE projects SET {("name = '"+name+("' ,"if desc!=""else"'"))if name!="" else ""}{("role = '"+desc+"'")if desc!="" else ""} WHERE projects.id={id}", "change")
    def RemoveProject(id):
        Run(f"DELETE FROM projects {(f"WHERE projects.id={id}")if id!="*"else""}", "change")

class IssueCmds:
    def ListIssues(Filter="", OrderBy=""):
        data = (Run(f"SELECT * FROM issues{(f" WHERE name LIKE '%{Filter}%' ")if Filter!=""else""}{f" ORDER BY {OrderBy}"if OrderBy!=""else""}","fetch"))
        return data
    def AddIssue(title, desc, status, priority, timestamp, lastUpdate, assignedUser):
        return (Run(f"INSERT INTO issues (title, description, status, priority, timestamp, lastUpdate, assignedUser) VALUES ('{title}','{desc}','{status}','{priority}','{timestamp}','{lastUpdate}','{assignedUser}')","change"))
    def EditIssue(id, title="", desc="", status="", priority="", timestamp="", lastUpdate="", assignedUser=""):
        Run(f"UPDATE issues SET {(f"title = '{title}'"+(", " if desc!="" or status!="" or priority!="" or timestamp!="" or lastUpdate!="" or assignedUser!="" else "")) if title!="" else ""}{(f"description = '{desc}'"+(", " if status!="" or priority!="" or timestamp!="" or lastUpdate!="" or assignedUser!="" else "")) if desc!="" else ""}{(f"status = '{status}'"+(", " if priority!="" or timestamp!="" or lastUpdate!="" or assignedUser!="" else "")) if status!="" else ""}{(f"priority = '{priority}'"+(", " if timestamp!="" or lastUpdate!="" or assignedUser!="" else "")) if priority!="" else ""}{(f"timestamp = '{timestamp}'"+(", " if lastUpdate!="" or assignedUser!="" else "")) if timestamp!="" else ""}{(f"lastUpdate = '{lastUpdate}'"+(", " if assignedUser!="" else "")) if lastUpdate!="" else ""}{(f"assignedUser = '{assignedUser}'") if assignedUser!="" else ""} WHERE issues.id={id}", "change")
    def RemoveIssue(id):
        Run(f"DELETE FROM issues {(f"WHERE issues.id={id}")if id!="*"else""}", "change")












