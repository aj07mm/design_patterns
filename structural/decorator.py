'''
    In object-oriented programming, the decorator pattern is a design pattern that allows behavior to be added to an individual object, either statically or dynamically, 
    without affecting the behavior of other objects from the same class.[1] The decorator pattern is often useful for adhering to the Single Responsibility Principle, 
    as it allows functionality to be divided between classes with unique areas of concern.[2] The decorator pattern is structurally nearly identical to the chain of responsibility pattern, 
    the difference being that in a chain of responsibility, exactly one of the classes handles the request, while for the decorator, all classes handle the request.

    https://en.wikipedia.org/wiki/Decorator_pattern

    Component
        ConcreteComponent Decorator
                            ConcreteDecoratorA ConcreteDecoratorB
'''


class Component:
    def draw(self):
        raise NotImplementedError("To be implemented")

    def resize(self):
        raise NotImplementedError("To be implemented")

class ConcreteComponent(Component):
    def draw(self):
        print("bar")

    def resize(self):
        print("bar")


class Decorator(Component):
    def __init__(self, _component):
        self._component = _component

    def draw(self):
        self._component.draw()

    def resize(self):
        self._component.resize()

class ConcreteDecoratorA(Decorator):

    def draw(self):
        super().draw()
        print('with decoratorA')

    def resize(self):
        super().resize()
        print('with decoratorA')


class ConcreteDecoratorB(Decorator):
    def draw(self):
        super().draw()
        print('with decoratorB')

    def resize(self):
        super().resize()
        print('with decoratorB')


if __name__ == '__main__':
    component = ConcreteComponent() 
    decorator_a = ConcreteDecoratorA(component)
    decorator_a.draw()
