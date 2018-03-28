'''
    In software engineering, the adapter pattern is a software design pattern (also known as Wrapper, an alternative naming shared with the Decorator pattern) 
    that allows the interface of an existing class to be used as another interface.[1] It is often used to make existing classes work with others without modifying their source code.

    https://en.wikipedia.org/wiki/Adaptor_pattern

    Adaptee
        Adaptor
           Target 

'''

from abc import ABCMeta, abstractmethod

class Adaptee:
    user = None
    number = None

    def recharge(self):
        raise NotImplementedError("To be implemented")


class AdaptorA(Adaptee):
    @abstractmethod
    def use_lightning(self):
        raise NotImplementedError("To be implemented")


class AdaptorB(Adaptee):
    @abstractmethod
    def use_micro_usb(self):
        raise NotImplementedError("To be implemented")


class TargetA(AdaptorA): # IPhone
    def use_lightning(self):
        print('use lightning')

    def recharge(self):
        self.use_lightning()
        


class TargetB(AdaptorB): # Android

    def use_micro_usb(self):
        print('use micro usb')

    def recharge(self):
        self.use_micro_usb()



if __name__ == '__main__':
   target_a = TargetA()
   target_a.recharge()
