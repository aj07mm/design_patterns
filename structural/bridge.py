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


from abc import ABCMeta, abstractmethod


NOT_IMPLEMENTED = "You should implement this."


class DrawingAPI:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_circle(self, x, y, radius):
        raise NotImplementedError(NOT_IMPLEMENTED)


class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return "API1.circle at {0}:{1} - radius: {2}".format(x, y, radius)


class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return "API2.circle at {0}:{1} - radius: {2}".format(x, y, radius)


class Shape:
    __metaclass__ = ABCMeta

    drawing_api = None

    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def resize_by_percentage(self, percent):
        raise NotImplementedError(NOT_IMPLEMENTED)


class CircleShape(Shape):
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        super(CircleShape, self).__init__(drawing_api)

    def draw(self):
        return self.drawing_api.draw_circle(
            self.x, self.y, self.radius
        )

    def resize_by_percentage(self, percent):
        self.radius *= (1 + percent/100)


if __name__ == '__main__':
    shapes = [
        CircleShape(1.0, 2.0, 3.0, DrawingAPI1()),
        CircleShape(5.0, 7.0, 11.0, DrawingAPI2())
    ]

    for shape in shapes:
        shape.resize_by_percentage(2.5)
        print(shape.draw())
