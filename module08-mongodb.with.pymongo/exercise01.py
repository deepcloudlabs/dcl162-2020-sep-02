from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
for dbname in client.list_database_names():
    print(dbname)