from banking.domain import Account, CheckingAccount, Customer

# heterogeneous list
accounts = []
accounts.append(Account("tr1", 1000))
accounts.append(CheckingAccount("tr2", 2000, 500))
accounts.append(Account("tr3", 3000))
accounts.append(CheckingAccount("tr4", 4000, 2500))
for acc in accounts:
    acc.withdraw(500)  # polymorphic call
    acc.deposit(250)  # polymorphic call
    print(str(acc))


def account_cost(accounts):  # generic
    for acc in accounts:
        if isinstance(acc, (CheckingAccount, Account)):
            acc.withdraw(50)  # polymorphic method


def get_total_balance(accounts):  # generic
    total = 0
    for acc in accounts:
        total = total + acc.balance  # polymorphic call
    return total


def get_customers_total_balance(customers):  # generic
    total = 0
    for customer in customers:
        for account in customer.get_all_accounts():
            total = total + account.balance  # polymorphic call
    return total

customers = [Customer("1", "Jack Bauer", "jack@example.com",None),
             Customer("2", "Kate Austen", "kate@example.com",None)]
for customer in customers:
    print(customer)
jack = customers[0]
jack.add_account(Account("1", 1000))
jack.add_account(CheckingAccount("2", 2000, 500))
kate = customers[1]
kate.add_account(Account("3", 4000))
kate.add_account(CheckingAccount("4", 4000, 2500))

print(f"Total Customer Balance: {get_customers_total_balance(customers)}.")
