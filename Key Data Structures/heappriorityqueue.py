from priorityqueuebase import PriorityQueueBase

"""
An implementation of a Priority Queue using a min-heap.
"""

class Empty(Exception):
    """
    Error for attempting to access an
    item from an empty structure.
    """
    pass


class HeapPriorityQueue(PriorityQueueBase):
    """A Priority Queue implemented with a min-heap."""

    class _Item(PriorityQueueBase._Item):
        """A lightweight, non-public composite used to store Priority Queue items."""
        __slots__ = '_index'    # streamline memory usage 

        def __init__(self, k, v, index):
            """Initializes an Item."""
            super().__init__(k, v)
            self._index = index

    # Utility methods:

    def _parent(self, i):
        """Yields the index of element i's parent node."""
        return (i - 1) // 2

    def _left(self, i):
        """Yields the index of element i's left node."""
        return (2 * i) + 1

    def _right(self, i):
        """Yields the index of element i's right node."""
        return (2 * i) + 2

    def _has_left(self, i):
        """Returns 'True' if element i has a left child or 'False' otherwise."""
        return self._left(i) < len(self._data)

    def _has_right(self, i):
        """Returns 'True' if element i has a right child or 'False' otherwise."""
        return self._right(i) < len(self._data)

    def _swap(self, i, j):
        """Swaps the elements at indices i and j."""
        self._data[i], self._data[j] = self._data[j], self._data[i]
        self._data[i]._index, self._data[j]._index = i, j

    def _bubble(self, i):
        if (i > 0) and (self._data[i] < self._data[self._parent(i)]):
            self._upheap(i)
        else:
            self._downheap(i)

    def _upheap(self, i):
        """Moves element i to its appropriate position in the heap."""
        parent = self._parent(i)
        if i > 0 and self._data[i] < self._data[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def _downheap(self, i):
        """Moves element i to its appropriate position in the heap."""
        if self._has_left(i):
            left = self._left(i)
            smallest = left
            if self._has_right(i):
                right = self._right(i)
                if self._data[right] < self._data[left]:
                    smallest = right
            if self._data[smallest] < self._data[i]:
                self._swap(i, smallest)
                self._downheap(smallest)

    # Public methods:
    
    def __init__(self):
        """Initializes an empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Returns the number of items in the Priority Queue."""
        return len(self._data)

    def add(self, key, value):
        """Adds a key-value pair to the Priority Queue."""
        pair = self._Item(key, value, len(self))
        self._data.append(pair)
        self._upheap(len(self._data) - 1)
        return pair

    def min(self):
        """Returns but does not remove the key-value pair (k, v) with the minimum key."""
        if self.is_empty():
            raise Empty('The Priority Queue is empty.')
        item = self._data[0]
        return item.pair()

    def remove_min(self):
        """Removes and returns the key-value pair (k, v) with the minimum key."""
        if self.is_empty():
            raise Empty('The Priority Queue is empty.')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item.pair()

    def update(self, item, key, value):
        """Updates the key and value for the specified Item."""
        i = item._index
        item._key = key
        item._value = value
        self._bubble(i)

    def remove(self, item):
        """Removes and returns the key-value pair (k, v) identified by the specified Item."""
        i = item._index
        if (i == len(self) - 1):
            self._data.pop()
        else:
            self._swap(i, len(self) - 1)
            self._data.pop()
            self._bubble(i)
        return (item._key, item._value)


# Unit Tests:
if __name__ == '__main__':
    pq = HeapPriorityQueue()
    pq.add(5, 'allan')
    pq.add(9, 'barnes')
    pq.add(3, 'ereneo')
    pq.add(7, 'kyle')
    last = pq._data[len(pq) - 1]
    assert(last.pair() == (9, 'barnes'))
    assert(pq._has_right(pq._parent(last._index)) == False)
    assert(pq._has_left(pq._parent(last._index)) == True)
    assert(pq.min() == (3, 'ereneo'))
    assert(pq.remove(pq._data[pq._parent(last._index)]) == (7, 'kyle'))
    last = pq._data[len(pq) - 1]
    assert(last.pair() == (5, 'allan'))
    pq.update(pq._data[last._index], 0, 'omega')
    assert(pq.remove_min() == (0, 'omega'))
    assert(pq.remove_min() == (3, 'ereneo'))
    assert(len(pq) == 1)
    assert(pq.remove_min() == (9, 'barnes'))
    assert(pq.is_empty() == True)
    
