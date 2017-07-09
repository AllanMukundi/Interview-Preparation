"""
An implementation of a Stack ADT using a Singly Linked List.
""" 

class Empty(Exception):
    """
    Error for attempting to access an
    element from an empty structure.
    """
    pass


class LinkedStack:
    """Singly Linked List implementation."""

    class _Node:
        """A lightweight, nonpublic class used as a Linked List node."""
        __slots__ = '_item', '_next'    # streamline memory usage

        def __init__(self, item, next):
            self._item = item
            self._next = next

    def __init__(self):
        """Initializes an empty Stack."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Returns the number of item in the Stack."""
        return self._size

    def is_empty(self):
        """Returns 'True' if the Stack is empty and 'False' otherwise."""
        return self._size == 0

    def push(self, i):
        """Adds item i on top of the Stack."""
        self._head = self._Node(i, self._head)
        self._size += 1

    def pop(self):
        """Removes and returns the item on top of the Stack."""
        if self.is_empty():
            raise Empty('The Stack is empty.')
        value = self._head._item
        self._head = self._head._next
        self._size -= 1
        return value

    def top(self):
        """Returns the item on top of the Stack but does not remove it."""
        if self.is_empty():
            raise Empty('The Stack is empty.')
        return self._head._item


# Unit Tests:
if __name__ == '__main__':
    s = LinkedStack()
    assert(len(s) == 0)
    assert(s.is_empty() == True)
    s.push(3)
    s.push('test')
    assert(len(s) == 2)
    assert(s.pop() == 'test')
    assert(len(s) == 1)
    assert(s.top() == 3)
    assert(s.is_empty() == False)
    s.push(9)
    s.push(12)
    assert(len(s) == 3)
    assert(s.top() == 12)
    s.pop()
    s.pop()
    s.pop()
    assert(len(s) == 0)
    assert(s.is_empty() == True)
