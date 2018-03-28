'''
    In software engineering, the composite pattern is a partitioning design pattern. 
    The composite pattern describes a group of objects that is treated the same way as a single instance of the same type of object. 
    The intent of a composite is to "compose" objects into tree structures to represent part-whole hierarchies. 
    Implementing the composite pattern lets clients treat individual objects and compositions uniformly.

    https://en.wikipedia.org/wiki/Composite_pattern

    Component
        Leaf Leaf Composite
                Leaf Leaf Leaf Composite Leaf
                            Leaf Leaf Leaf

'''


class Component:
    def get_composite(self):
        raise NotImplementedError("To be implemented")


class Composite(Component):
    leafs = []

    def get_composite(self):
        for leaf in self.leafs:
            print(leaf)

    def add(self, leaf):
        self.leafs.append(leaf)

    def remove(self, leaf):
        self.leafs.remove(leaf)


class Leaf(Component):
    name = None

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

if __name__ == '__main__':
    composite = Composite()
    composite.add(Leaf('leaf no1'))
    composite.add(Leaf('leaf no2'))
    composite.add(Leaf('leaf no3'))
    composite.get_composite()
