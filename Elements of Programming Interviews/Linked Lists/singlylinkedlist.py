class LinkedList:

    class _Node:
        __slots__ = '_item', '_next'

        def __init__(self, item, next=None):
            self._item = item
            self._next = next

        def item(self):
            return self._item

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return (self._size == 0)

    def __str__(self):
        curnode = self._head
        items = ""
        while (curnode):
            items += str(curnode.item())
            curnode = curnode._next
            if curnode:
                items += " -> "
        return items

    def add(self, item):
        new_node = self._Node(item)
        if len(self) == 0:
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1
        return new_node

    def delete(self, item):
        prevnode = None
        curnode = self._head
        while curnode:
            if curnode.item() == item:
                val = curnode.item()
                if prevnode is None:
                    self._head = curnode._next
                else:
                    prevnode._next = curnode._next
                if len(self) == 1:
                    self._tail = None
                curnode = None
                self._size -= 1
                return val
            else:
                prevnode = curnode
                curnode = curnode._next
        raise KeyError('Node with the specified item does not exist.')

