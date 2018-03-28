'''
    The bridge pattern is a design pattern used in software engineering that is meant to 
    "decouple an abstraction from its implementation so that the two can vary independently", introduced by the Gang of Four.[1] 
    The bridge uses encapsulation, aggregation, and can use inheritance to separate responsibilities into different classes.
    When a class varies often, the features of object-oriented programming become very useful because changes to a program's code can be made easily with minimal prior knowledge about the program. 
    The bridge pattern is useful when both the class and what it does vary often. 
    The class itself can be thought of as the abstraction and what the class can do as the implementation. The bridge pattern can also be thought of as two layers of abstraction.

    The bridge pattern is often confused with the adapter pattern. In fact, the bridge pattern is often implemented using the object adapter pattern, e.g. in the Java code below.

    https://en.wikipedia.org/wiki/Bridge_pattern

                Abstraction
    RefinedAbstraction   Implementor
                            ConcreteImplementorA ConcreteImplementorB

'''


class Abstraction:
    _implementation = None

    def draw_circle(self):
        raise NotImplementedError("To be implemented")


class RefinedAbstraction(Abstraction):

    def __init__(self, _implementation):
        self._implementation = _implementation

    def draw_circle(self):
        self._implementation.draw_square()


class Implementor:

    def draw_square(self):
        raise NotImplementedError("To be implemented")


class ConcreteImplementorA(Implementor):

    def draw_square(self):
        print('draw squareA')


class ConcreteImplementorB(Implementor):

    def draw_square(self):
        print('draw squareB')


if __name__ == '__main__':
    implementation = ConcreteImplementorA()
    refined_abstraction = RefinedAbstraction(implementation)
    refined_abstraction.draw_circle()
