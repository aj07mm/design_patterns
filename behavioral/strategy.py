'''
    In computer programming, the strategy pattern (also known as the policy pattern) is a behavioral software design pattern that enables selecting an algorithm at runtime. 
    Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.

    Strategy lets the algorithm vary independently from clients that use it.[2] Strategy is one of the patterns included in the influential book Design Patterns by Gamma et al.[3] 
    that popularized the concept of using design patterns to describe how to design flexible and reusable object-oriented software. 
    Deferring the decision about which algorithm to use until runtime allows the calling code to be more flexible and reusable.

    For instance, a class that performs validation on incoming data may use the strategy pattern to select a validation algorithm depending on the type of data, 
    the source of the data, user choice, or other discriminating factors. These factors are not known until run-time and may require radically different validation to be performed. 
    The validation algorithms (strategies), encapsulated separately from the validating object, may be used by other validating objects in different areas of the system (or even different systems) 
    without code duplication.

    Typically the strategy pattern stores a reference to some code in a data structure and retrieves it. 
    This can be achieved by mechanisms such as the native function pointer, the first-class function, 
    classes or class instances in object-oriented programming languages, or accessing the language implementation's internal storage of code via reflection.

    https://en.wikipedia.org/wiki/Strategy_pattern

'''

import abc


class Context:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()


class Strategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms. Context
    uses this interface to call the algorithm defined by a
    ConcreteStrategy.
    """

    @abc.abstractmethod
    def algorithm_interface(self):
        pass


class ConcreteStrategyA(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self):
        print('concrete strategyA')


class ConcreteStrategyB(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self):
        print('concrete strategyB')


if __name__ == "__main__":
    concrete_strategy_a = ConcreteStrategyA()
    context = Context(concrete_strategy_a)
    context.context_interface()
