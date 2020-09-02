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