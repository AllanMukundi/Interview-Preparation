from collections.abc import MutableMapping

"""
An implementation of an abstract base class for Maps.
"""

class MapBase(MutableMapping):
    """An abstract base class for a Map."""

    class _Item:
        """A lightweight, non-public composite used to store Map items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            """Initializes an item."""
            self._key = k
            self._value = v

        def __eq__(self, other):
            """Returns 'True' if self and other have the same key and 'False' otherwise."""
            return (self._key == other._key)

        def __ne__(self, other):
            """Returns 'True' if self and other have different keys and 'False' otherwise."""
            return not (self == other)

        def __lt__(self, other):
            """
            Returns 'True' if the first Item's key (self)
            is less than other's and 'False' otherwise.
            """
            return (self._key < other._key)

