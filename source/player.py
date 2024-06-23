"""
player.py - Base player class from Chapter 3 Creational Patterns
"""


class Player:
    def __init__(self) -> None:
        self.currentRoom: int
        self.health: int
