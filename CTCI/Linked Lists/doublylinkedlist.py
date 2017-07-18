class LinkedList:

    class _Node:
        __slots__ = '_item', '_prev', '_next'

        def __init__(self, item, prev=None, next=None):
            self._item = item
            self._prev = prev
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
                items += " <-> "
        return items

    def add(self, item):
        newnode = self._Node(item)
        if len(self) == 0:
            self._head = newnode
        else:
            self._tail._next = newnode
            newnode._prev = self._tail
        self._tail = newnode
        self._size += 1
        return newnode

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
                curnode._next._prev = prevnode
                if len(self) == 1:
                    self._tail = None
                curnode = None
                self._size -= 1
                return val
            else:
                prevnode = curnode
                curnode = curnode._next
        raise KeyError('Node with the specified item does not exist.')

