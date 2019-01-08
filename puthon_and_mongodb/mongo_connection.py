import pymongo

class MongoConnection:

    def connect(self):
        myclient = pymongo.MongoClient("ds041934.mlab.com",41934)
        mydb = myclient["hub-petland"]
        mydb.authenticate("admin","petland1234")
        return mydb
