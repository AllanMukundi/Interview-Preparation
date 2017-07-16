from doublylinkedbase import _DoublyLinkedBase

"""
An implementation of a Deque ADT using a Doubly Linked List.
"""

class Empty(Exception):
    """
    Error for attempting to access an
    item from an empty structure.
    """
    pass


class LinkedDeque(_DoublyLinkedBase):
    """Doubly Linked List Deque implementation."""

    def add_first(self, i):
        """Adds item i to the front of the Deque."""
        self._insert_between(i, self._header, self._header._next)

    def add_last(self, i):
        """Adds item i to the back of the Deque."""
        self._insert_between(i, self._trailer._prev, self._trailer)

    def delete_first(self):
       """Removes and returns the first item in the Deque."""
       if self.is_empty():
           raise Empty('The Deque is empty.')
       return self._delete_node(self._header._next)

    def delete_last(self):
        """Removes and returns the last item in the Deque."""
        if self.is_empty():
            raise Empty('The Deque is empty.')
        return self._delete_node(self._trailer._prev)

    def front(self):
        """Returns the item at the front of the Deque but does not remove it."""
        if self.is_empty():
            raise Empty('The Deque is empty.')
        return self._header._next._item

    def back(self):
        """Returns the item at the back of the Deque but does not remove it."""
        if self.is_empty():
            raise Empty('The Deque is empty')
        return self._trailer._prev._item


# Unit Tests:
if __name__ == '__main__':
    d = LinkedDeque()
    assert(d.is_empty() == True)
    assert(len(d) == 0)
    d.add_last(5)
    d.add_first(3)
    d.add_first(7)
    assert(d.front() == 7)
    assert(d.back() == 5)
    d.add_last('test')
    assert(d.delete_last() == 'test')
    assert(d.delete_first() == 7)
    assert(d.is_empty() == False)
    assert(len(d) == 2)
    assert(d.delete_last() == 5)
    assert(d.delete_last() == 3)
    assert(d.is_empty() == True)

