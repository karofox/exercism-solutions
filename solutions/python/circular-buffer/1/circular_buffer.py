"""Circular Buffer module."""


from typing import Any


class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.
    """

    def __init__(self, message: str):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.
    """

    def __init__(self, message: str):
        self.message = message


class CircularBuffer:
    """A cyclic data structure.

    capacity: the capacity of the buffer.
    """

    def __init__(self, capacity: int):
        self._capacity = capacity + 1 # an empty space added
        self._content = [None for _ in range(self._capacity)]
        self._head = 0  # index of the first value
        self._tail = 0  # index of the first empty space

    def read(self) -> Any:
        """Reads the oldest value from the buffer."""
        if self._is_empty():
            raise BufferEmptyException("Circular buffer is empty")
        data = self._content[self._head]
        self._content[self._head] = None
        self._head = (self._head + 1) % self._capacity
        return data

    def write(self, data: Any) -> None:
        """Writes the data to the buffer."""
        if self._is_full():
            raise BufferFullException("Circular buffer is full")
        self._content[self._tail] = data
        self._tail = (self._tail + 1) % self._capacity

    def overwrite(self, data: Any) -> None:
        """Writes the data to the buffer. In case the buffer is full,
        the oldest value is overwritten."""
        self._content[self._tail] = data
        if self._is_full():
            self._head = (self._head + 1) % self._capacity
        self._tail = (self._tail + 1) % self._capacity

    def clear(self):
        """Clears the contents of the buffer."""
        self._head = 0
        self._tail = 0
        self._content = [None for _ in range(self._capacity)]

    def _is_full(self) -> bool:
        """Returns True if the buffer is full."""
        return (self._tail + 1) % self._capacity == self._head

    def _is_empty(self) -> bool:
        """Returns True if the buffer is empty."""
        return self._head == self._tail
