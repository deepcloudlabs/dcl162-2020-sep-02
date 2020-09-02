from enum import Enum

class InsufficientBalance(Exception):
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit

# Value Class has no identity
class Address:
    def __init__(self,line1, line2, city, country):
        self.line1 = line1

# Entity Class
class Customer:
    def __init__(self, identity, fullname, email,address):
        self._identity = identity
        self._fullname = fullname
        self._email = email
        self._address = address
        self.accounts = {}

    @property
    def identity(self):
        return self._identity

    @property
    def fullname(self):
        return self._fullname

    @property
    def email(self):
        return self._email

    def get_total_balance(self):
        total = 0
        for iban, account in self.accounts.items():
            total = total + account.balance
        return total

    def new_account(self, iban, balance):
        if iban in self.accounts:
            raise ValueError("Iban already exists.")
        acc = Account(iban, balance)
        self.accounts[iban] = acc
        return acc

    def add_account(self, account):
        if account.iban in self.accounts:
            raise ValueError("Iban already exists.")
        self.accounts[account.iban] = account

    def get_account(self, iban):
        return self.accounts[iban]

    def remove_account(self, iban):
        acc = None
        if iban in self.accounts:
            acc = self.accounts[iban]
            del self.accounts[iban]
        return acc

    def get_num_accounts(self):
        return len(self.accounts)

    def get_all_accounts(self):
        return self.accounts.values()

    def get_all_ibans(self):
        return self.accounts.keys()

    def __str__(self):
        return f"Customer [identity: {self.identity}, fullname: {self.fullname}, email: {self.email}]"

    def __repr__(self):
        return repr(self.identity)


class AccountStatus(Enum):
    CLOSED = 100
    ACTIVE = 200
    BLOCKED = 350


class Account:  # super/base class
    def __init__(self, iban, balance):  # constructor
        self._iban = iban  # attribute information hiding!
        self._balance = balance  # balance should be positive!
        self._status = AccountStatus.ACTIVE

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def iban(self):
        return self._iban

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        print("Account::withdraw")
        if amount <= 0:  # validation
            raise ValueError("amount must be positive.")
        if amount > self._balance:  # business rule
            raise InsufficientBalance("your balance does not cover your expenses.", amount - self._balance)
        self._balance = self._balance - amount

    def deposit(self, amount):
        print("Account::deposit")
        if amount <= 0:  # validation
            raise ValueError("amount must be positive.")
        self._balance = self._balance + amount

    def __str__(self):
        return f"Account [ iban: {self.iban}, balance: {self.balance}, status: {self.status}]"

    def __repr__(self):
        return repr(self.iban)


class CheckingAccount(Account):  # sub/derived class
    def __init__(self, iban, balance, overdraft_amount=500):
        super().__init__(iban, balance)
        self.overdraft_amount = overdraft_amount

    def withdraw(self, amount):  # overriding
        print("CheckingAccount::withdraw")
        # if isinstance(amount, float)
        if amount <= 0:  # validation
            raise ValueError("amount must be positive.")
        if amount > (self.balance + self.overdraft_amount):  # business rule
            raise InsufficientBalance("your balance does not cover your expenses.",
                                      amount - self.balance - self.overdraft_amount)
        self._balance = self._balance - amount

    def __str__(self):  # overriding
        return f"CheckingAccount [ iban: {self.iban}, balance: {self.balance}, status: {self.status}, overdraftAmount: {self.overdraft_amount}]"
