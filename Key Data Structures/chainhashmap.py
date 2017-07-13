from hashmapbase import HashMapBase
from tablemap_us import UnsortedTableMap

"""
An implementation of a Hash Map using separate chaining for collision resolution.
"""

class ChainHashMap(HashMapBase):
    """Hash Map implemented with separate chaining."""

    def _bucket_getitem(self, i, k):
        """Returns the value associated with key k if it exists."""
        bucket = self._table[i]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, i, k ,v):
        """
        Updates the value of key k to be v if the key exists in the Hash Map.
        Inserts key k with a value of v into the Hash Table if it is non-existent.
        """
        if self._table[i] is None:
            self._table[i] = UnsortedTableMap()
        size = len(self._table[i])
        self._table[i][k] = v
        if len(self._table[i]) > size:
            self._n += 1
   
    def _bucket_delitem(self, i, k):
        """Deletes key k from the Hash Map if it exists."""
        bucket = self._table[i]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        """Generates an iterator of the keys in the Hash Map."""
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


# Unit Tests:
if __name__ == '__main__':
    m = ChainHashMap()
    m['allan'] = 3
    m['ereneo'] = 7
    m['barnes'] = 'test'
    assert(m['allan'] == 3)
    assert(m['ereneo'] == 7)
    assert(len(m) == 3)
    assert(m['barnes'] == 'test')
    m['barnes'] = 'foo'
    assert(m['barnes'] == 'foo')
    del m['barnes']
    assert(len(m) == 2)
    del m['allan']
    assert(m['ereneo'] == 7)
    del m['ereneo']
    assert(len(m) == 0)

