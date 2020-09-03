from pymongo import MongoClient

from crm.domain import Customer

client = MongoClient("mongodb://localhost:27017")
crm = client.crm
customers = crm.customers

""""
jack = Customer("jack bauer", "ankara, turkey", "jack@example.com")
result = customers.insert_one(jack.__dict__)
print(f"inserted _id: {result.inserted_id}")
"""

customers_to_insert = [
    Customer("kate austen", "istanbul, turkey", "kate@example.com"),
    Customer("james sawyer", "antalya, turkey", "james@example.com"),
    Customer("ben linus", "izmir, turkey", "ben@example.com")
]
new_customers = []
for cust in customers_to_insert:
    new_customers.append(cust.__dict__)
result = customers.insert_many(new_customers)
print(f"inserted _id's: {result.inserted_ids}")
