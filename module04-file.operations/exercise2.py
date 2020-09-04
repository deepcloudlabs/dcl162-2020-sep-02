with open('accounts.txt', mode="r") as accounts:
    for record in accounts:
        iban, fullname, balance = record.split(',')
        print(f"{iban}{fullname}{balance}")