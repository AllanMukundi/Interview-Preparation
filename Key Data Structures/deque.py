"""
An implementation of a Deque ADT using a Python list (adapter design pattern).
"""

class Empty(Exception):
    """
    Error for attempting to access an
    element from an empty structure.
    """
    pass


class Deque:
    """Deque ADT implementation."""

    INITIAL_CAPACITY = 10

    def __init__(self):
        """Initializes an empty Deque."""
        self._data = [None] * Deque.INITIAL_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Returns the number of elements in the Deque."""
        return self._size

    def is_empty(self):
        """Returns 'True' if the Deque is empty and 'False' otherwise."""
        return self._size == 0

    def add_first(self, i):
        """Adds element i to the front of the Deque."""
        if (self._size == len(self._data)):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = i
        self._size += 1

    def add_last(self, i):
        """Adds element i to the back of the Deque."""
        if (self._size == len(self._data)):
            self._resize(2 * len(self._data))
        index = (self._front + self._size) % len(self._data)
        self._data[index] = i
        self._size += 1

    def delete_first(self):
       """Removes and returns the first element in the Deque."""
       if self.is_empty():
           raise Empty('The Deque is empty.')
       value = self._data[self._front]
       self._data[self._front] = None
       self._front = (self._front + 1) % len(self._data)
       self._size -= 1
       if 0 < self._size < (len(self._data) // 4):
           self._resize(len(self._data) // 2)
       return value

    def delete_last(self):
        """Removes and returns the last element in the Deque."""
        if self.is_empty():
            raise Empty('The Deque is empty.')
        back = (self._front + self._size - 1) % len(self._data)
        value = self._data[back]
        self._data[back] = None
        self._size -= 1
        if 0 < self._size < (len(self._data) // 4):
            self._resize(len(self._data) // 2)
        return value

    def front(self):
        """Returns the element at the front of the Deque but does not remove it."""
        if self.is_empty():
            raise Empty('The Deque is empty.')
        return self._data[self._front]

    def back(self):
        """Returns the element at the back of the Deque but does not remove it."""
        if self.is_empty():
            raise Empty('The Deque is empty.')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def _resize(self, num):
        """Resizes the Deque to use a new list of size num."""
        old = self._data
        self._data = [None] * num
        place = self._front
        for i in range(self._size):
            self._data[i] = old[place]
            place = (place + 1) % len(old)
        self._front = 0


# Unit Tests:
if __name__ == '__main__':
    d = Deque()
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
