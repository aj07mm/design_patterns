
'''
    In object-oriented design, the chain-of-responsibility pattern is a design pattern consisting of a source of command objects and a series of processing objects.[1] 
    Each processing object contains logic that defines the types of command objects that it can handle; the rest are passed to the next processing object in the chain. 
    A mechanism also exists for adding new processing objects to the end of this chain. 
    Thus, the chain of responsibility is an object oriented version of the if ... else if ... else if ....... else ... endif idiom, 
    with the benefit that the condition–action blocks can be dynamically rearranged and reconfigured at runtime.

    In a variation of the standard chain-of-responsibility model, some handlers may act as dispatchers, capable of sending commands out in a variety of directions, forming a tree of responsibility. 
    In some cases, this can occur recursively, with processing objects calling higher-up processing objects with commands that attempt to solve some smaller part of the problem; 
    in this case recursion continues until the command is processed, or the entire tree has been explored. An XML interpreter might work in this manner.

    This pattern promotes the idea of loose coupling.

    The chain-of-responsibility pattern is structurally nearly identical to the decorator pattern, the difference being that for the decorator, 
    all classes handle the request, while for the chain of responsibility, exactly one of the classes in the chain handles the request.

    https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern

    AbstractFactory
        ConcreteFactory
            - createSomething()

'''

from abc import ABCMeta, abstractmethod
from enum import Enum


class LogLevel(Enum):
    """
    Log Levels Enum.
    """
    NONE = 0
    INFO = 1
    DEBUG = 2
    WARNING = 3
    ERROR = 4
    FUNCTIONAL_MESSAGE = 5
    FUNCTIONAL_ERROR = 6
    ALL = 7


class Logger:
    """
    Abstract handler in chain of responsibility pattern.
    """
    __metaclass__ = ABCMeta

    next = None

    def __init__(self, levels):
        """
        Initialize new logger

        Args:
            levels (list[str]): List of log levels.
        """
        self.log_levels = []

        for level in levels:
            self.log_levels.append(level)

    def set_next(self, next_logger):
        """
        Set next responsible logger in the chain.

        Args:
            next_logger (Logger): Next responsible logger.

        Returns:
            Logger: Next responsible logger.
        """
        self.next = next_logger
        return self.next

    def message(self, msg, severity):
        """
        Message writer handler.

        Args:
            msg (str): Message string.
            severity (LogLevel): Severity of message as log level enum.
        """
        if LogLevel.ALL in self.log_levels or severity in self.log_levels:
            self.write_message(msg)

        if self.next is not None:
            self.next.message(msg, severity)

    @abstractmethod
    def write_message(self, msg):
        """
        Abstract method to write a message.

        Args:
            msg (str): Message string.

        Raises:
            NotImplementedError
        """
        raise NotImplementedError("You should implement this method.")


class ConsoleLogger(Logger):
    def write_message(self, msg):
        """
        Overrides parent's abstract method to write to console.

        Args:
            msg (str): Message string.
        """
        print("Writing to console:", msg)


class EmailLogger(Logger):
    """
    Overrides parent's abstract method to send an email.

    Args:
        msg (str): Message string.
    """
    def write_message(self, msg):
        print("Sending via email:", msg)


class FileLogger(Logger):
    """
    Overrides parent's abstract method to write a file.

    Args:
        msg (str): Message string.
    """
    def write_message(self, msg):
        print("Writing to log file:", msg)

class DatabaseLogger(Logger):
    """
    Overrides parent's abstract method to write a file.

    Args:
        msg (str): Message string.
    """
    def write_message(self, msg):
        print("Writing to database:", msg)

def main():
    """
    Building the chain of responsibility.
    """
    logger = ConsoleLogger([LogLevel.ALL])
    logger1 = logger.set_next(
        EmailLogger([LogLevel.FUNCTIONAL_MESSAGE, LogLevel.FUNCTIONAL_ERROR])
    )
    # As we don't need to use file logger instance anywhere later
    # We will not set any value for it.
    logger2 = logger1.set_next(
        FileLogger([LogLevel.WARNING, LogLevel.ERROR])
    )
    logger3 = logger2.set_next(
        DatabaseLogger([LogLevel.WARNING, LogLevel.ERROR])
    )

    # ConsoleLogger will handle this part of code since the message
    # has a log level of all
    logger.message("Entering function ProcessOrder().", LogLevel.DEBUG)
    logger.message("Order record retrieved.", LogLevel.INFO)

    # ConsoleLogger and FileLogger will handle this part since file logger
    # implements WARNING and ERROR
    logger.message(
        "Customer Address details missing in Branch DataBase.",
        LogLevel.WARNING
    )
    logger.message(
        "Customer Address details missing in Organization DataBase.",
        LogLevel.ERROR
    )

    # ConsoleLogger and EmailLogger will handle this part as they implement
    # functional error
    logger.message(
        "Unable to Process Order ORD1 Dated D1 for customer C1.",
        LogLevel.FUNCTIONAL_ERROR
    )
    logger.message("OrderDispatched.", LogLevel.FUNCTIONAL_MESSAGE)


if __name__ == "__main__":
    main()
