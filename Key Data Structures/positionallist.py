from doublylinkedbase import _DoublyLinkedBase

"""
An implementation of a Positional ADT using a Doubly Linked List.
"""

class PositionalList(_DoublyLinkedBase):
    """A container of items allowing positional access."""

    class Position:
        """An abstraction representing an item's location."""

        def __init__(self, container, node):
            """Initializes a Position (should not be called by users)."""
            self._container = container
            self._node = node

        def item(self):
            """Returns the item stored at this Position."""
            return self._node._item

        def __eq__(self, other):
            """Returns 'True' if other is a Position representing the same location and 'False' otherwise.."""
            return (type(self) is type(other)) and (self._node is other._node)

        def __ne__(self, other):
            """Returns 'True' if other does not represent the same location and 'False' otherwise."""
            return not(self == other)

    # Utility Methods:

    def _validate(self, p):
        """Returns Position p's node."""
        if not isinstance(p, self.Position):
            raise TypeError('p is not a Position.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._next is None:
            raise ValueError('p is invalid.')
        return p._node

    def _make_position(self, node):
        """Returns a Position instance for a given node (None if sentinel)."""
        if (node is self._header) or (node is self._trailer):
            return None
        else:
            return self.Position(self, node)

    # Accessors:

    def first(self):
        """Returns the first Position in the container (or None if the list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Returns the last Position in the container (or None if the list is empty)."""
        return self._make_position(self._trailer._prev)

    def after(self, p):
        """Returns the Position after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def before(self, p):
        """Returns the Position before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def __iter__(self):
        """Generates a forward iteration of the list's items."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.item()
            cursor = self.after(cursor)

    # Mutators:

    def _insert_between(self, i, prev_node, next_node):
        """Inserts item i between two nodes and returns its Position."""
        node = super()._insert_between(i, prev_node, next_node)
        return self._make_position(node)

    def add_first(self, i):
        """Adds item i at the front of the list and returns its Position."""
        return self._insert_between(i, self._header, self._header._next)

    def add_last(self, i):
        """Adds item i at the back of the list and returns its Position."""
        return self._insert_between(i, self._trailer._prev, self._trailer)

    def add_after(self, p, i):
        """Adds item i into the container after Position p and returns its Position."""
        original = self._validate(p)
        return self._insert_between(i, original, original._next)

    def add_before(self, p, i):
        """Adds element i into the container before Position p and returns its Position."""
        original = self._validate(p)
        return self._insert_between(i, original._prev, original)

    def delete(self, p):
        """Removes and returns the item at Position p."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, i):
        """
        Replaces the item at Position P with i 
        and returns the item formerly at Position p.
        """
        original = self._validate(p)
        value = original._item
        original._item = i
        return value


def insertion_sort(plist):
    """Sorts a PositionalList of comparable elements in increasing order."""
    if len(plist) > 1:
        marker = plist.first()
        while (marker != plist.last()):
            pivot = plist.after(marker)
            value = pivot.item()
            if (value > marker.item()):
                marker = pivot
            else:
                walk = marker
                while (walk != plist.first()) and (plist.before(walk).item() > value):
                    walk = plist.before(walk)
                plist.delete(pivot)
                plist.add_before(walk, value)


def insertion_sort_v2(plist):    # I find this method to be more intuitive
    """Sorts a PositionalList of comparable elements in increasing order."""
    if len(plist) > 1:
        mark = plist.after(plist.first())
        while mark != plist.after(plist.last()):
            val = mark.item()
            walk = mark
            while walk != plist.first() and plist.before(walk).item() > val:
                plist.replace(walk, plist.before(walk).item())
                walk = plist.before(walk)
            plist.replace(walk, val)
            mark = plist.after(mark)


# Unit Tests:
if __name__ == '__main__':
    l = PositionalList()
    assert(l.is_empty() == True)
    l.add_first(3)
    assert(len(l) == 1)
    assert(l.first().item() == 3)
    assert(l.after(l.first()) == None)
    assert(l.before(l.first()) == None)
    l.add_last(5)
    l.add_last('test')
    assert(len(l) == 3)
    test_last = l.last()
    assert(test_last.item() == 'test')
    assert(l.before(test_last).item() == 5)
    assert(l.after(test_last) == None)
    l.replace(test_last, 10)
    assert(test_last.item() == 10)
    assert(l.delete(test_last) == 10)
    assert(len(l) == 2)
    assert(test_last._node._item == None)
    l.add_before(l.last(), 999)
    assert(l.after(l.first()).item() == 999)
    l._insert_between(8, l.after(l.first())._node, l.last()._node)
    assert(len(l) == 4)
    assert(l.before(l.last()).item() == 8)
    l.add_after(l.last(), 'test')
    assert(l.last().item() == 'test')
    l.delete(l.last())
    l.delete(l.last())
    l.delete(l.last())
    l.delete(l.last())
    l.delete(l.last())
    assert(l.is_empty() == True)

