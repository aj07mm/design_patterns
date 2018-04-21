'''
    The Builder design pattern is a creational design pattern, designed to provide a flexible design solution to various object creation problems in Object-Oriented software. 
    The intent of the Builder design pattern is to separate the construction of a complex object from its representation.[1] It is one of the GoF design patterns[2].

    The Builder design pattern solves problems like:[3]

    How can a class (the same construction process) create different representations of a complex object?
    How can a class that includes creating a complex object be simplified?

    https://en.wikipedia.org/wiki/Builder_pattern

    AbstractBuilder
        ConcreteBuilder
            - build()

'''

from __future__ import print_function
from abc import ABCMeta, abstractmethod


class Car(object):
    def __init__(self, wheels=4, seats=4, color="Black"):
        self.wheels = wheels
        self.seats = seats
        self.color = color

    def __str__(self):
        return "This is a {0} car with {1} wheels and {2} seats.".format(
            self.color, self.wheels, self.seats
        )


class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_wheels(self, value):
        pass

    @abstractmethod
    def set_seats(self, value):
        pass

    @abstractmethod
    def set_color(self, value):
        pass

    @abstractmethod
    def get_result(self):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_wheels(self, value):
        self.car.wheels = value

    def set_seats(self, value):
        self.car.seats = value

    def set_color(self, value):
        self.car.color = value

    def get_result(self):
        return self.car


class CarBuilderDirector(object):
    @staticmethod
    def construct():
        builder = CarBuilder()
        builder.set_wheels(8)
        builder.set_seats(4)
        builder.set_color("Red")
        return builder.get_result()


if __name__ == '__main__':
    car = CarBuilderDirector.construct()
    print(car)
