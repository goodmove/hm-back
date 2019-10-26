from pymongo import MongoClient

__db_name = "hackm"
__uri = "mongodb+srv://admin:admin@mflix-tbs6k.mongodb.net/{}?retryWrites=true&w=majority".format(__db_name)

__client = MongoClient(__uri)
DB = __client[__db_name]