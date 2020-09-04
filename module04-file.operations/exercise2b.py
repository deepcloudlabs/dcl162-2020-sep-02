import pickle

with open('accounts.pkl', mode="rb") as accounts:
    bank_accounts = pickle.load(accounts)
    print(bank_accounts)