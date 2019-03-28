import copy
from abc import ABC, abstractmethod


class Prototype:
    @abstractmethod
    def clone(self):
        raise NotImplementedError("You should implement this!")


class ConcretePrototypeA(Prototype):
    def clone(self):
        return copy.copy(self)


class ConcretePrototypeB(Prototype):
    def clone(self):
        return copy.copy(self)


if __name__ == '__main__':
    concrete_prototype_a_clone = ConcretePrototypeA().clone()
    print(concrete_prototype_a_clone)
