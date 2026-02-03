class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return (self.__price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, new_prod):
        name, description, price, quantity = new_prod.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print('Цена не должна быть нулевая или отрицательная')
