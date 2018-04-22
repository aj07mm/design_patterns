'''

    A proxy, in its most general form, is a class functioning as an interface to something else. 
    The proxy could interface to anything: a network connection, a large object in memory, a file, or some other resource that is expensive or impossible to duplicate. 
    In short, a proxy is a wrapper or agent object that is being called by the client to access the real serving object behind the scenes. 
    Use of the proxy can simply be forwarding to the real object, or can provide additional logic. In the proxy, extra functionality can be provided, 
    for example caching when operations on the real object are resource intensive, or checking preconditions before operations on the real object are invoked. 
    For the client, usage of a proxy object is similar to using the real object, because both implement the same interface.

    https://en.wikipedia.org/wiki/Proxy_pattern

'''

from abc import ABCMeta, abstractmethod


NOT_IMPLEMENTED = "You should implement this."


class AbstractCar:
    __metaclass__ = ABCMeta

    @abstractmethod
    def drive(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Car(AbstractCar):
    def drive(self):
        print("Car has been driven!")


class Driver:
    def __init__(self, age):
        self.age = age


class ProxyCar(AbstractCar):
    def __init__(self, driver):
        self.car = Car()
        self.driver = driver

    def drive(self):
        if self.driver.age <= 16:
            print("Sorry, the driver is too young to drive.")
        else:
            self.car.drive()


driver = Driver(16)
car = ProxyCar(driver)
car.drive()

driver = Driver(25)
car = ProxyCar(driver)
car.drive()
