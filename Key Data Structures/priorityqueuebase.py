"""
An implementation of an abstract base class for a Priority Queue.
"""

class PriorityQueueBase:
    """An abstract base class describing a Priority Queue."""

    class _Item:
        """A lightweight, non-public composite used to store Priority Queue items."""
        __slots__ = '_key', '_value'    # streamline memory usage

        def __init__(self, k, v):
            """Initializes an Item."""
            self._key = k
            self._value = v

        def pair(self):
            return (self._key, self._value)

        def __lt__(self, other):
            """
            Returns 'True' if the first Item's key (self)
            is less than other's and 'False' otherwise.
            """
            return self._key < other._key

    def is_empty(self):
        """Returns 'True' if the Priority Queue is empty and 'False' otherwise."""
        return len(self) == 0


