from mapbase import MapBase

"""An implementation of a Map using an unsorted list."""

class UnsortedTableMap(MapBase):
    """Map implementation using an unsorted list."""

    def __init__(self):
        """Initializes an empty Map."""
        self._table = []

    def __getitem__(self, k):
        """Returns the value associated with key k if it exists."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assigns value v to key k, overwriting the existing value if present."""
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Removes the item associated with key k."""
        for i in range(len(self._table)):
            if k == self._table[i]._key:
                self._table.pop(i)
                return
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        """Returns the number of items in the Map."""
        return len(self._table)

    def __iter__(self):
        """Generates an iteration of the Map's keys."""
        for item in self._table:
            yield item._key


# Unit Tests:
if __name__ == '__main__':
    m = UnsortedTableMap()
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

