"""Matrix module."""


class Matrix:
    """Transforms a string representation of matrix into
    a matrix of integers.
    """

    def __init__(self, matrix_string: str):
        self._matrix = [
            [int(elem) for elem in row.split()] for row in matrix_string.split("\n")
        ]

    def row(self, index: int) -> list[int]:
        """Returns the matrix row at provided index."""
        if index - 1 >= len(self._matrix):
            raise IndexError
        return self._matrix[index - 1]

    def column(self, index: int) -> list[int]:
        """Returns the matrix column at provided index."""
        if index - 1 >= len(self._matrix[0]):
            raise IndexError
        return [row[index - 1] for row in self._matrix]
