from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
crm = client.crm
customers = crm.customers
customers.drop()