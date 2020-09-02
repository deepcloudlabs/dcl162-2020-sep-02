class InsufficientBalance(Exception):
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit


class Account:  # super/base class
    def __init__(self, iban, balance):  # constructor
        self.__iban = iban  # attribute information hiding!
        self.balance = balance  # balance should be positive!
        self.status = None

    def withdraw(self, amount):
        print("Account::withdraw")
        if amount <= 0:  # validation
            raise ValueError("amount must be positive.")
        if amount > self.balance:  # business rule
            raise InsufficientBalance("your balance does not cover your expenses.", amount - self.balance)
        self.balance = self.balance - amount

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        print("Account::deposit")
        if amount <= 0:  # validation
            raise ValueError("amount must be positive.")
        self.balance = self.balance + amount

    def __str__(self):
        return f"Account [ iban: {self.__iban}, balance: {self.balance}]"

    def __repr__(self):
        return repr(self.__iban)


class CheckingAccount(Account): # sub/derived class
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
        self.balance = self.balance - amount

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
