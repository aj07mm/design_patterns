import unittest
from unittest.mock import patch


class Singleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.setInstance()

    def setInstance(self):
        Singleton.__instance = self
        self.foo()

    def foo(self):
        pass


class SingletonTestCase(unittest.TestCase):
    @patch.object(Singleton, 'foo')
    def test_one_instance_only(self, mock_foo):
        try:
            Singleton()
            Singleton()
        except:
            pass
        self.assertEqual(mock_foo.call_count, 1)


if __name__ == "__main__":
    unittest.main()
