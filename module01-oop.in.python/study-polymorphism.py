from banking.domain import Account, CheckingAccount

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
        total = total + acc.get_balance()  # polymorphic call
    return total


print(f"Total Balance: {get_total_balance(accounts)}.")
