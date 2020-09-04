import json

bank_accounts = {
    'accounts': [
        {'i': 'TR1', 'f': 'jack shephard', 'b': 100000},
        {'i': 'TR2', 'f': 'kate austen', 'b': 200000},
        {'i': 'TR3', 'f': 'ben linus', 'b': 300000}
    ]
}

country = {
    "name": "turkey",
    "cities": [{"id": 1000, "name": "ankara"}],
    "capital": 1000
}

with open("accounts.json", "r") as json_file:
    print(json.dumps(json.load(json_file), indent=4))
    #json.dump(bank_accounts,json_file)
