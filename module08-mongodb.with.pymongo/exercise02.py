from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.world
for collection_name in db.list_collection_names():
    print(collection_name)
