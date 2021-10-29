import sqlite3


class DataBase:

    def __init__(self):
        self.connection = sqlite3.connect("DataBase.db")
        self.createTable()

    def createTable(self):
        c = self.connection.cursor()

        sql = """CREATE TABLE IF NOT EXISTS users (
        id_user integer primary key autoincrement ,
        name text,
        email text,
        tel text,
        postal_code text,
        state text,
        city text,
        district text,
        street text,
        number text,
        residence_type text)"""

        c.execute(sql)
        self.connection.commit()
        c.close()
