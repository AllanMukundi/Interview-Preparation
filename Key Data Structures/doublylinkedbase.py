"""
An implementation of a Doubly Linked List base class.
"""

class _DoublyLinkedBase:
    """A base class providing a Doubly Linked List representation."""

    class _Node:
        "A lightweight, non-public class used as a Linked List node."""
        __slots__ = '_item', '_next', '_prev'    # streamline memory usage

        def __init__(self, i, prev=None, next=None):
            self._item = i
            self._prev = prev
            self._next = next

    def __init__(self):
        """Initializes an empty list."""
        self._header = self._Node(None)
        self._trailer = self._Node(None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Returns the number of items in the list."""
        return self._size

    def is_empty(self):
        """Returns 'True' if the list is empty and 'False' otherwise."""
        return self._size == 0

    def _insert_between(self, i, prev_node, next_node):
        """Inserts item i between two nodes and returns its new node."""
        if (prev_node._next is not next_node) or (prev_node is not next_node._prev):
            raise ValueError('Nodes are not adjacent.')
        new_node = self._Node(i, prev_node, next_node)
        prev_node._next = new_node
        next_node._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """Deletes non-sentinel node from the list and returns its item."""
        prev_node = node._prev
        next_node = node._next
        prev_node._next = next_node
        next_node._prev = prev_node
        self._size -= 1
        item = node._item
        node._prev = node._next = node._item = None
        return item

