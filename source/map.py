"""
map.py - Base map implementation from Chapter 3 Creational Patterns
"""


class MapSite:
    def Enter(self):
        raise NotImplementedError


class Room(MapSite):
    def __init__(self, roomNumber: int) -> None:
        self.roomNumber: int = roomNumber
        self._sides: dict = {"North": None, "South": None, "East": None, "West": None}

    def Enter(self):
        print(f"Entered room {self.roomNumber}")
        return self

    def SetSide(self, direction, feature: MapSite):
        """North, South, East, West and wall or door"""
        self._sides[direction] = feature
        return self._sides[direction]

    def GetSide(self, direction):
        return self._sides[direction]


class Wall(MapSite):
    def Enter(self):
        print("You hurt your nose bumping into the wall!")
        return self


class Door(MapSite):
    def __init__(self, room1: Room, room2: Room, isOpen: bool = False) -> None:
        self._room1: Room = room1
        self._room2: Room = room2
        self.isOpen: bool = isOpen

    def Enter(self):
        if self.isOpen:
            return self
        else:
            print("You hurt your nose bumping into the closed door!")
            return self


class Maze:
    def __init__(self) -> None:
        self._rooms: dict

    def AddRoom(self, room: Room):
        self._rooms[room.roomNumber] = room
        return room

    def GetRoom(self, roomNumber: int):
        return self._rooms.get(roomNumber)


class MazeGame:
    def CreateMaze(self):
        aMaze = Maze()
        r1 = Room(1)
        r2 = Room(2)
        theDoor = Door(r1, r2)

        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)

        r1.SetSide("North", Wall())
        r1.SetSide("East", theDoor)
        r1.SetSide("South", Wall())
        r1.SetSide("West", Wall())

        r2.SetSide("North", Wall())
        r2.SetSide("East", Wall())
        r2.SetSide("South", Wall())
        r2.SetSide("West", theDoor)

        return aMaze
