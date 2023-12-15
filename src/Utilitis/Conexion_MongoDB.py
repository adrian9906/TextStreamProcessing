import pymongo

class Conection_MongoDb:
    @staticmethod
    def serverInfo(self,MONGO_HOST, LOCAL_PORT):
        MONGO_TIME_OUT = 1000
        MONGO_URI = "mongodb://" + MONGO_HOST + ":" + LOCAL_PORT + "/"

        return MONGO_TIME_OUT, MONGO_URI


