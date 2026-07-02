import sqlite3


DB = sqlite3.connect('DATABASE.db')





def run(SQL, type):
    Cursor = DB.cursor()

    print("Executing: "+SQL)

    if type=="fetch":
        Cursor.execute(SQL)
        data = Cursor.fetchall()
    elif type=="change":
        data = Cursor.execute(SQL)
    DB.commit()
    return data
