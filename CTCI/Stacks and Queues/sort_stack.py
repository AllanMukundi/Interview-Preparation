"""
3.5 - Write a program to sort a stack such that the smallest
items are on the top. You can use an additional temporary
stack, but you may not copy the elements into any other
data structure (such as an array).
"""

class Stack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def push(self, i):
        self._data.append(i)

    def pop(self):
        if not self.is_empty():
           return self._data.pop()
        raise IndexError('Cannot pop an empty Stack.')

    def top(self):
        if not self.is_empty():
            return self._data[len(self) - 1]
        raise IndexError('Cannot check the top of an empty Stack.')


def sort_stack(stack):
    pass
