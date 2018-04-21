'''
    The abstract factory pattern provides a way to encapsulate a group of individual factories that have a common theme without specifying their concrete classes.[1] 
    In normal usage, the client software creates a concrete implementation of the abstract factory and then uses the generic interface of the factory to create the concrete objects that are part of the theme.
    The client doesn't know (or care) which concrete objects it gets from each of these internal factories, since it uses only the generic interfaces of their products.[1] 
    This pattern separates the details of implementation of a set of objects from their general usage and relies on object composition, 
    as object creation is implemented in methods exposed in the factory interface.[2]

    https://en.wikipedia.org/wiki/Abstract_factory_pattern

    AbstractFactory
        ConcreteFactory
            - createSomething()

'''

from abc import ABCMeta, abstractmethod


class GUIFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_button(self):
        raise NotImplementedError("To be implemented")

class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()


class Button:
    __metaclass__ = ABCMeta

    @abstractmethod
    def paint(self):
        pass

class LinuxButton(Button):
    def paint(self):
        return "Render a button in a Linux style"

class WindowsButton(Button):
    def paint(self):
        return "Render a button in a Windows style"


class MacOSButton(Button):
    def paint(self):
        return "Render a button in a MacOS style"



if __name__ == '__main__':
    factory = LinuxFactory()
    button = factory.create_button()
    print(button.paint())
