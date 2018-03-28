Gof patterns
---


# ways to implement interfaces with python

import abc


class Animal(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def method_to_implement(self, input):
        return

class Animal:

    def andar(self):
        raise NotImplementedError("Animais precisam implementar andar")


