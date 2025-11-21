"""Robot class module"""

from typing import Literal

NORTH = 1j
EAST = 1
SOUTH = -1j
WEST = -1


class Robot:
    """A Robot that can process three commands:

    R - it turns right
    L - it turns left
    A - it advances one step
    """

    def __init__(self, direction: int = NORTH, x_pos: int = 0, y_pos: int = 0):
        self.direction = direction
        self._coord = x_pos + y_pos * 1j

    @property
    def coordinates(self):
        return (int(self._coord.real), int(self._coord.imag))

    def move(self, instructions: str) -> None:
        """Processes a set of instructions."""
        for command in instructions:
            self._process(command)
    
    def _process(self, command: str) -> None:
        """Processes one given command."""
        match command:
            case "R":
                self.direction *= -1j
            case "L":
                self.direction *= 1j
            case "A":
                self._coord += self.direction
            case _:
                raise ValueError(f"Unknown {command=}")
