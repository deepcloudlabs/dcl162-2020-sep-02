from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
client.drop_database("crm")