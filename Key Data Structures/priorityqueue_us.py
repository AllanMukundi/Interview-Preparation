from priorityqueuebase import PriorityQueueBase
from positionallist import PositionalList

"""
An implementation of a Priorty Queue using an unsorted list.

"""

class Empty(Exception):
    """
    Error for attempting to access an
    item from an empty structure.
    """
    pass


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented Priority Queue implementation using an unsorted list."""

    def __init__(self):
        """Initializes an empty Priority Queue."""
        self._data = PositionalList()

    def _find_min(self):
        """
        A utility method which returns the Position
        of the item with the minimum key.
        """
        if self.is_empty():
            raise Empty('The Priority Queue is empty.')
        smallest = self._data.first()
        walk = self._data.after(smallest)
        while walk is not None:
            if (walk.item() < smallest.item()):
                smallest = walk
            walk = self._data.after(walk)
        return smallest

    def __len__(self):
        """Returns the number of items in the Priority Queue."""
        return len(self._data)

    def add(self, key, value):
        """Inserts a key-value pair into the Priority Queue."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Returns but does not remove the key-value pair (k, v)  with the minimum key."""
        min_pos = self._find_min()
        item = min_pos.item()
        return (item._key, item._value)

    def remove_min(self):
        """Removes and returns the key-value pair (k, v) with the minimum key."""
        min_pos = self._find_min()
        item = self._data.delete(min_pos)
        return (item._key, item._value)


# Unit Tests:
if __name__ == '__main__':
    pq = UnsortedPriorityQueue()
    pq.add(5, 'allan')
    pq.add(9, 'barnes')
    pq.add(3, 'ereneo')
    pq.add(7, 'kyle')
    assert(pq.min() == (3, 'ereneo'))
    assert(pq.remove_min() == (3, 'ereneo'))
    assert(pq.remove_min() == (5, 'allan'))
    assert(len(pq) == 2)
    assert(pq.remove_min() == (7, 'kyle'))
    assert(pq.remove_min() == (9, 'barnes'))
    assert(pq.is_empty() == True)

