"""
An implementation of a Stack ADT using a Python list (adapter design pattern).
"""

class Empty(Exception):
    """
    Error for attempting to access an
    element from an empty structure.
    """
    pass


class Stack:
    """Stack ADT implementation."""

    def __init__(self):
        """Initializes an empty Stack."""
        self._data = []

    def __len__(self):
        """Returns the number of elements on the Stack."""
        return len(self._data)

    def is_empty(self):
        """Returns 'True' if the Stack is empty and 'False' otherwise."""
        return self._data == []

    def push(self, i):
        """Adds element i to the top of the Stack."""
        self._data.append(i)

    def pop(self):
        """Removes and returns the element on top of the Stack."""
        try:
            return self._data.pop()
        except:
            raise Empty('The Stack is empty.')

    def top(self):
            """Returns the element on top of the Stack but does not remove it."""
            try:
                return self._data[-1]
            except:
                raise Empty('The Stack is empty.')


# Unit Tests:
if __name__ == '__main__':
    s = Stack()
    assert(len(s) == 0)
    assert(s.is_empty() == True)
    s.push(3)
    s.push('test')
    assert(len(s) == 2)
    assert(s.pop() == 'test')
    assert(len(s) == 1)
    assert(s.top() == 3)
    assert(s.is_empty() == False)
    s.push(9)
    s.push(12)
    assert(len(s) == 3)
    assert(s.top() == 12)
    s.pop()
    s.pop()
    s.pop()
    assert(len(s) == 0)
    assert(s.is_empty() == True)

