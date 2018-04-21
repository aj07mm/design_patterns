'''
    In computer programming, flyweight is a software design pattern. 
    A flyweight is an object that minimizes memory usage by sharing as much data as possible with other similar objects; 
    it is a way to use objects in large numbers when a simple repeated representation would use an unacceptable amount of memory. 
    Often some parts of the object state can be shared, and it is common practice to hold them in external data structures and pass them to the objects temporarily when they are used.

    A classic example usage of the flyweight pattern is the data structures for graphical representation of characters in a word processor. 
    It might be desirable to have, for each character in a document, a glyph object containing its font outline, font metrics, and other formatting data, 
    but this would amount to hundreds or thousands of bytes for each character. 
    Instead, for every character there might be a reference to a flyweight glyph object shared by every instance of the same character in the document; 
    only the position of each character (in the document and/or the page) would need to be stored internally.

    https://en.wikipedia.org/wiki/Flyweight_pattern

'''


# Instances of CheeseBrand will be the Flyweights
class CheeseBrand(object):
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost
        self._immutable = True   # Disables future attributions

    def __setattr__(self, name, value):
        if getattr(self, '_immutable', False):  # Allow initial attribution
            raise RuntimeError('This object is immutable')
        else:
            super(CheeseBrand, self).__setattr__(name, value)
    

class CheeseShop(object):
    menu = {}  # Shared container to access the Flyweights
    
    def __init__(self):
        self.orders = {}  # per-instance container with private attributes

    def stock_cheese(self, brand, cost):
        cheese = CheeseBrand(brand, cost)
        self.menu[brand] = cheese   # Shared Flyweight

    def sell_cheese(self, brand, units):
        self.orders.setdefault(brand, 0)
        self.orders[brand] += units   # Instance attribute

    def total_units_sold(self):
        return sum(self.orders.values())
    
    def total_income(self):
        income = 0
        for brand, units in self.orders.items():
            income += self.menu[brand].cost * units
        return income



if __name__ == '__main__':
    shop1 = CheeseShop()
    shop2 = CheeseShop()

    shop1.stock_cheese('white', 1.25)
    shop1.stock_cheese('blue', 3.75)
    # Now every CheeseShop have 'white' and 'blue' on the inventory
    # The SAME 'white' and 'blue' CheeseBrand

    shop1.sell_cheese('blue', 3)    # Both can sell
    shop2.sell_cheese('blue', 8)    # But the units sold are stored per-instance
