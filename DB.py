import sqlite3
from sqlite3 import Error


class DataBase:

    def __init__(self):
        self.connection()

    def connection(self):
        connection = None
        try:
            connection = sqlite3.connect("DataBase.db")
        except Error as ex:
            print(ex)
        return connection

    def dql(self, query):
        connection = self.connection()
        cursor = connection.cursor()
        cursor.execute(query)
        select = cursor.fetchall()
        connection.close()
        return select

    def dml(self, query):
        try:
            connection = self.connection()
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            connection.close()
        except Error as ex:
            return ex
