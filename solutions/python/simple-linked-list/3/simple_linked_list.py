from __future__ import annotations


class Node:
    def __init__(self, value: int, next: Node = None):
        self._value = value
        self._next = next

    def value(self) -> int:
        return self._value

    def next(self) -> Node:
        return self._next


class LinkedList:
    def __init__(self, values: list[int] | None = None):
        if not values:
            self._head = None
            return
        prev = None
        for val in values:
            node = Node(val, prev)
            prev = node
        self._head = prev

    def __len__(self) -> int:
        elem = self._head
        counter = 0
        while elem is not None:
            counter += 1
            elem = elem.next()
        return counter

    def __iter__(self) -> int:
        elem = self._head
        while elem is not None:
            yield elem.value()
            elem = elem.next()

    def head(self) -> Node:
        if not self._head:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value: int) -> None:
        node = Node(value, self._head)
        self._head = node

    def pop(self) -> int:
        if not self._head:
            raise EmptyListException("The list is empty.")
        node = self._head
        self._head = self._head.next()
        return node.value()

    def reversed(self) -> LinkedList:
        return LinkedList(self)


class EmptyListException(Exception):
    """List is empty."""
