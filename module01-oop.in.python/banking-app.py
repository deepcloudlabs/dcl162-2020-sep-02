from banking.domain import Account, InsufficientBalance, CheckingAccount
from banking.stockmarket import Stock

# Ctrl+Alt+L : formatLa

try:
    acc1 = Account("tr1", 1000) # __init__(self, iban, balance) ==> Account(acc1,"tr1", 1000)
    print(str(acc1))
    acc1.withdraw(500) # def withdraw(self, amount) ==> withdraw(acc1, 500)
    print(str(acc1)) # ==> __str__(self)
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
