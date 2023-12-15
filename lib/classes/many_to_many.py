class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        elif hasattr(self, "name"):
            raise Exception("Name can't be changed")
        elif not len(name) >= 3:
            raise Exception("Name must be at least 3 characters")
        else:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list(
            set([order.customer for order in Order.all if order.coffee == self])
        )

    def num_orders(self):
        return len([order.coffee for order in Order.all if order.coffee == self])

    def average_price(self):
        order_prices = [order.price for order in Order.all if order.coffee == self]
        if order_prices:
            return sum(order_prices) / len(order_prices)
        else:
            return "0"


class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            return Exception("Name must be a string")
        elif not 1 <= len(name) <= 15:
            return Exception("Name must be between 1 and 15 characters")
        else:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(
            set([order.coffee for order in Order.all if order.customer == self])
        )

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            return Exception("Price must be a float (ie. 1.0, 2.0, etc.)")
        elif hasattr(self, "price"):
            return Exception("Price cannot be changed")
        elif not 1.0 <= price <= 10.0:
            return Exception("Price must be between 1.0 and 10.0")
        else:
            self._price = price
