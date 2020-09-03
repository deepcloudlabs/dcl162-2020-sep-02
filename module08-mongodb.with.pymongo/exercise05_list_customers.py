from pymongo import MongoClient
from pprint import pprint as pp

from crm.domain import Customer

client = MongoClient("mongodb://localhost:27017")
crm = client.crm
customers = crm.customers

#for cust in customers.find({'address': 'antalya, turkey'}):
for cust in customers.find({}).sort("address", -1):
    pp(cust)
