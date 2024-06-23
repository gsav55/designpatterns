"""
map.py - Base map implementation from Chapter 3 Creational Patterns
"""


class MapSite:
    def Enter(self):
        raise NotImplementedError


class Room(MapSite):
    def __init__(self, roomNumber: int) -> None:
        self.roomNumber: int = roomNumber

    def Enter(self):
        print(f"Entered room {self.roomNumber}")

    def SetSide(self, Direction, MapSite: MapSite):
        raise NotImplementedError

    def GetSide(self):
        raise NotImplementedError


class Wall(MapSite):
    def Enter(self):
        print("You hurt your nose bumping into the wall!")


class Door(MapSite):
    def __init__(self, room1, room2, isOpen: bool = False) -> None:
        self._room1: int = room1
        self._room2: int = room2
        self.isOpen: bool = isOpen

    def Enter(self):
        if self.isOpen:
            raise NotImplementedError
        else:
            print("You hurt your nose bumping into the closed door!")
