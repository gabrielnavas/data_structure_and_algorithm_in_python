class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percent=10):
        return self.price - (self.price * (percent/100))

    # Getter
    @property
    def price(self):
        return self._price
    
    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = value.replace('R$', '')
            value = value.replace('$', '')
            value = float(value)
        self._price = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value