"""
An implementation of a Queue ADT using a Python list (adapter design pattern).
"""

class Empty(Exception):
    """
    Error for attempting to access an
    element from an empty structure.
    """
    pass


class Queue:
    """Queue ADT implementation."""

    INITIAL_CAPACITY = 10 

    def __init__(self):
        """Initializes an empty Queue."""
        self._data = [None] * Queue.INITIAL_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Returns the number of elements in the Queue."""
        return self._size

    def is_empty(self):
        """Returns 'True' if the Queue is empty and 'False' otherwise."""
        return self._size == 0

    def enqueue(self, i):
        """Adds element i to the end of the Queue."""
        if (self._size == len(self._data)):
            self._resize(2 * len(self._data))
        index = (self._front + self._size) % len(self._data)
        self._data[index] = i
        self._size += 1

    def dequeue(self):
        """Removes and returns the first element in the Queue."""
        if self.is_empty():
            raise Empty('The Queue is empty.')
        value = self._data[self._front]
        self._data[self._front] = None    # for garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < (len(self._data) // 4):
            self._resize(len(self._data) // 2)
        return value

    def front(self):
        """Returns the element at the front of the Queue but does not remove it."""
        if self.is_empty():
            raise Empty('The Queue is empty.')
        return self._data[self._front]
    
    def _resize(self, num): 
        """Resizes the Queue to use a new list of size num."""
        old = self._data
        self._data = [None] * num
        place = self._front
        for i in range(self._size):
            self._data[i] = old[place]
            place = (place + 1) % len(old)
        self._front = 0


# Unit Tests:
if __name__ == '__main__':
    q = Queue()
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

