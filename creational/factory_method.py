'''
    In class-based programming, the factory method pattern is a creational pattern that uses factory methods to deal with the problem of creating objects 
    without having to specify the exact class of the object that will be created. 
    This is done by creating objects by calling a factory method—either specified in an interface and implemented by child classes, 
    or implemented in a base class and optionally overridden by derived classes—rather than by calling a constructor.

    https://en.wikipedia.org/wiki/Factory_method_pattern

    Creator
        - factoryMethod()

'''

from abc import ABC, abstractmethod


class MazeGame(ABC):

    def __init__(self):
        self.rooms = []
        self._prepare_rooms()

    def _prepare_rooms(self):
        room1 = self.make_room()
        room2 = self.make_room()

        room1.connect(room2)
        self.rooms.append(room1)
        self.rooms.append(room2)

    def play(self):
        print("Playing using \"{}\"".format(self.rooms[0]))

    @abstractmethod
    def make_room(self):
        raise NotImplementedError("You should implement this!")


class MagicMazeGame(MazeGame):

    def make_room(self):
        return MagicRoom()


class OrdinaryMazeGame(MazeGame):

    def make_room(self):
        return OrdinaryRoom()


class Room(ABC):
    def __init__(self):
        self.connected_rooms = []

    def connect(self, room):
        self.connected_rooms.append(room)


class MagicRoom(Room):
    def __str__(self):
        return "Magic room"


class OrdinaryRoom(Room):
    def __str__(self):
        return "Ordinary room"



if __concrete_prototype_a_clonename__ == '__main__':
    ordinaryGame = OrdinaryMazeGame()
    ordinaryGame.play()

    magicGame = MagicMazeGame()
    magicGame.play()
