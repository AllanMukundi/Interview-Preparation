from hashmapbase import HashMapBase

"""
An implementation of a Hash Map using linear probing for collision resolution.
"""

class ProbeHashMap(HashMapBase):
    """Hash Map implemented with linear probing."""

    _AVAIL = object()   # sentinel denoting the location of a prior deletion

    def _is_available(self, i):
        """
        Returns 'True' if index i is available
        in the Hash Table and 'False' otherwise.
        """
        return (self._table[i] is None) or (self._table[i] is ProbeHashMap._AVAIL)

    def _find_slot(self, i, k):
        """
        Searches for key k in the Hash Table from index i.

        If a match is found, (True, index) is returned
        If a match is not found, (False, index) is returned
        (where index denotes the first available slot).
        """
        slot = None
        while True:
            if self._is_available(i):
                if slot is None:
                    slot = i
                if (self._table[i] is None):
                    return (False, slot)
            elif (k == self._table[i]._key):
                return (True, i)
            i = (i + 1) % len(self._table)

    def _bucket_getitem(self, i, k):
        """Returns the value associated with key k if it exists."""
        found, slot = self._find_slot(i, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[slot]._value

    def _bucket_setitem(self, i, k ,v):
        """
        Updates the value of key k to be v if the key exists in the Hash Map.
        Inserts key k with a value of v into the Hash Table if it is non-existent.
        """
        found, slot = self._find_slot(i, k)
        if not found:
            self._table[slot] = self._Item(k, v)
            self._n += 1
        else:
            self._table[slot]._value = v
   
    def _bucket_delitem(self, i, k):
        """Deletes key k from the Hash Map if it exists."""
        found, slot = self._find_slot(i, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[slot] = ProbeHashMap._AVAIL

    def __iter__(self):
        """Generates an iterator of the keys in the Hash Map."""
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]._key


# Unit Tests:
if __name__ == '__main__':
    m = ProbeHashMap()
    m['allan'] = 3
    m['ereneo'] = 7
    m['barnes'] = 'test'
    assert(m['allan'] == 3)
    assert(m['ereneo'] == 7)
    assert(len(m) == 3)
    assert(m['barnes'] == 'test')
    m['barnes'] = 'foo'
    assert(m['barnes'] == 'foo')
    assert(len(m) == 2)
    del m['allan']
    assert(m['ereneo'] == 7)
    del m['ereneo']
    assert(len(m) == 0)

