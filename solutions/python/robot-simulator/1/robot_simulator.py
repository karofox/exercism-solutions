"""Robot class module"""

from typing import Literal

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

Direction = Literal[0, 1, 2, 3]
Command = Literal["R", "L", "A"]


class Robot:
    """A Robot that can process three commands:

    R - it turns right
    L - it turns left
    A - it advances one step
    """

    def __init__(self, direction: Direction = NORTH, x_pos: int = 0, y_pos: int = 0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions: str) -> None:
        """Processes a set of instructions."""
        for command in instructions:
            self._process(command)

    def _process(self, command: Command) -> None:
        """Processes one given command."""
        match command:
            case "R":
                self.direction = (self.direction + 1) % 4
            case "L":
                self.direction = (self.direction - 1) % 4
            case "A":
                self._advance()
            case _:
                raise ValueError(f"Unknown {command=}")

    def _advance(self) -> None:
        """Advances in proper direction."""
        match self.direction:
            case _ if self.direction == NORTH:
                self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
            case _ if self.direction == SOUTH:
                self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
            case _ if self.direction == EAST:
                self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
            case _ if self.direction == WEST:
                self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
