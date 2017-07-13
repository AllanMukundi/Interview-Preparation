from random import randrange
from mapbase import MapBase

"""
An implementation of an abstract base class for a Map using a Hash Table.
"""

class HashMapBase(MapBase):
    """An abstract base class for a Map using a Hash Table."""

    def __init__(self, cap=11, p=179426363):
        """Initializes an empty Hash Table Map."""
        self._table = [None] * cap
        self._n = 0
        self._prime = p
        self._scale = randrange(1, p)
        self._shift = randrange(0, p)

    def _hash_function(self, k):
        """Returns a hash value for the immutable value k."""
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        """Returns the number of items in the Hash Table."""
        return self._n

    def __getitem__(self, k):
        """Returns the value associated with key k if it exists."""
        slot = self._hash_function(k)
        return self._bucket_getitem(slot, k)

    def __setitem__(self, k, v):
        """
        Updates the value of key k to be v if the key exists in the Hash Table.
        Inserts key k with a value of v into the Hash Table if it is non-existent.
        """
        slot = self._hash_function(k)
        self._bucket_setitem(slot, k, v)
        if (self._n > (len(self._table) // 2)):
            self._resize(2 * len(self._table) - 1)    # 2x - 1 is often prime
    
    def __delitem__(self, k):
        """Deletes key k from the Hash Table if it exists."""
        slot = self._hash_function(k)
        self._bucket_delitem(slot, k)
        self._n -= 1

    def _resize(self, num):
       """Resizes the table to use a new list of size num."""
       old = list(self.items())
       self._table = [None] * num
       self._n = 0    # to be computed during insertions
       for (k, v) in old:
           self[k] = v

