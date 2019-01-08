import mysql.connector

class Database:


    def __init__(self):
        self.connection = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='webapptest', use_pure=False)
        self.curser = self.connection.cursor()


    def selectAll(self):
        data = []
        self.curser.execute("select * from testTable")
        rows = self.curser.fetchall()

        for r in rows:
            data.append(r[0])

        return data