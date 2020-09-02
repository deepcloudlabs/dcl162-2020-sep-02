class InsufficientBalance(Exception):
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit


class Customer:
    def __init__(self, identity, fullname, email):
        self.identity = identity
        self.fullname = fullname
        self.email = email
        self.accounts = {}

    def add_account(self, iban, balance):
        if iban in self.accounts:
            raise ValueError("Iban already exists.")
        acc = Account(iban, balance)
        self.accounts[iban] = acc
        return acc

    def add_account(self, account):
        if account.get_iban() in self.accounts:
            raise ValueError("Iban already exists.")
        self.accounts[account.get_iban()] = account

    def get_account(self, iban):
        return self.accounts[iban]

    def remove_account(self, iban):
        acc = None
        if iban in self.accounts:
            acc = self.accounts[iban]
            del self.accounts[iban]
        return acc

    def get_num_accounts(self):
        len(self.accounts)

    def get_all_accounts(self):
        return self.accounts.values()

    def get_all_ibans(self):
        return self.accounts.keys()

    def __str__(self):
        pass

    def __repr__(self):
        return repr(self.identity)


class Account:  # super/base class
    def __init__(self, iban, balance):  # constructor
        self._iban = iban  # attribute information hiding!
        self._balance = balance  # balance should be positive!
        self.status = None

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
        return f"Account [ iban: {self.iban}, balance: {self.balance}]"

    def __repr__(self):
        return repr(self.iban)


class CheckingAccount(Account):  # sub/derived class
    def __init__(self, iban, balance, overdraft_amount=500):
        super().__init__(iban, balance)
        self.overdraft_amount = overdraft_amount

    def withdraw(self, amount):  # overriding
        print("CheckingAccount::withdraw")
        if amount <= 0:  # validation
            raise ValueError("amount must be positive.")
        if amount > (self.balance + self.overdraft_amount):  # business rule
            raise InsufficientBalance("your balance does not cover your expenses.",
                                      amount - self.balance - self.overdraft_amount)
        self._balance = self._balance - amount

    def __str__(self):  # overriding
        return f"CheckingAccount [ balance: {self.balance}]"


class Stock:
    def __init__(self, symbol, price):
        self._symbol = symbol
        self._price = price

    def __repr__(self):
        return repr(self._symbol)

    @property  # read-only property
    def symbol(self):
        return self._symbol

    @property  # read-write property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("Stock price must be positive.")
        self._price = price

    def __str__(self):
        return f"Stock ({self._symbol}, {self._price})"
