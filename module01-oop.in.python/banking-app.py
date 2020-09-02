from banking.domain import Account, InsufficientBalance, CheckingAccount, Customer
from banking.stockmarket import Stock

# Ctrl+Alt+L : formatLa

try:
    acc1 = Account("tr1", 1000)  # __init__(self, iban, balance) ==> Account(acc1,"tr1", 1000)
    print(str(acc1))
    acc1.withdraw(500)  # def withdraw(self, amount) ==> withdraw(acc1, 500)
    print(str(acc1))  # ==> __str__(self)
    acc1.deposit(750)
    print(acc1)
    acc1.withdraw(1000000)
except ValueError as err:
    print(err)
except InsufficientBalance as err:
    print(err)

try:
    acc2 = CheckingAccount("tr2", 1000, 500)
    acc2.withdraw(1500)
    print(acc2)
except ValueError as err:
    print(err)
except InsufficientBalance as err:
    print(err)

# Alt + Enter
orcl = Stock("orcl", 111.34)
print(orcl)
orcl.price = 109.76  # setter method
print(orcl)

customers = [Customer("1", "Jack Bauer", "jack@example.com"),
             Customer("2", "Kate Austen", "kate@example.com")]
for customer in customers:
    print(customer)
jack = customers[0]
jack.add_account(Account("1", 1000))
jack.add_account(CheckingAccount("2", 2000, 500))
kate = customers[1]
kate.add_account(Account("3", 4000))
kate.add_account(CheckingAccount("4", 4000, 2500))
print(jack.get_num_accounts())
for customer in customers:
    print(f"{customer.fullname}: {customer.get_total_balance()}")