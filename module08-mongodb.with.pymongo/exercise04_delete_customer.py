from pymongo import MongoClient
from pprint import pprint as pp

from crm.domain import Customer

client = MongoClient("mongodb://localhost:27017")
crm = client.crm
customers = crm.customers

# result = customers.delete_one({"email": "jack@example.com"})
# print(result.deleted_count)

result = customers.delete_many({})
print(result.deleted_count)
