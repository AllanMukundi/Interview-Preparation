"""
An implementation of a Queue ADT using a Singly Linked List.
""" 

class Empty(Exception):
    """
    Error for attempting to access an
    item from an empty structure.
    """
    pass


class LinkedQueue:
    """Singly Linked List Queue implementation."""

    class _Node:
        """A lightweight, non-public class used as a Linked List node."""
        __slots__ = '_item', '_next'    # streamline memory usage

        def __init__(self, item, next=None):
            """Initializes a Node."""
            self._item = item
            self._next = next

    def __init__(self):
        """Initializes an empty Queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Returns the number of items in the Queue."""
        return self._size

    def is_empty(self):
        """Returns 'True' if the Queue is empty and 'False' otherwise."""
        return self._size == 0

    def enqueue(self, i):
        """Adds item i to the end of the Queue."""
        new_node = self._Node(i)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Removes and returns the first item in the Queue."""
        if self.is_empty():
            raise Empty('The Queue is empty.')
        value = self._head._item
        self._head = self._head._next
        if self.is_empty():
            self._tail = None
        self._size -= 1
        return value

    def front(self):
        """Returns the item at the front of the Queue but does not remove it."""
        if self.is_empty():
            raise Empty('The Queue is empty.')
        return self._head._item

# Unit Tests:
if __name__ == '__main__':
    q = LinkedQueue()
    assert(len(q) == 0)
    assert(q.is_empty() == True)
    q.enqueue('test')
    assert(q.front() == 'test')
    assert(len(q) == 1)
    assert(q.is_empty() == False)
    assert(q.dequeue() == 'test')
    assert(q.is_empty() == True)
    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(-3)
    q.enqueue(9)
    q.enqueue('test')
    assert(len(q) == 5)
    assert(q.front() == 5)
    q.dequeue()
    q.dequeue()
    assert(q.dequeue() == -3)
    q.dequeue()
    assert(q.dequeue() == 'test')
    assert(q.is_empty() == True)

