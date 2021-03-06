class InsufficientBalance(Exception):
    def __init__(self, deficit):
        self.deficit = deficit


class Account:
    def __init__(self, iban, balance):
        self._iban = iban
        self._balance = balance

    @property
    def iban(self):
        return self._iban

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self._balance = self._balance + amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if self._balance < amount:
            raise InsufficientBalance(amount - self._balance)
        self._balance = self._balance - amount
