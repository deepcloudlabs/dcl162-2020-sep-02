import json

with open("accounts.json", "r") as json_file:
    bank_accounts = json.load(json_file)
    print(bank_accounts)
