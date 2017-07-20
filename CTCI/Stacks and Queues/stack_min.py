"""
3.2 - How would you design a stack which, in addition to the regular
stack operations, has a function which returns the minimum element?
All operations should run in O(1) time.
"""

class MinStack:

    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def push(self, i):
        getMin = self.minimum()
        if getMin is None or i < getMin:
            getMin = i
        self._data.append((i, getMin))

    def pop(self):
        if len(self) > 0:
            return self._data.pop()[0]

    def top(self):
        if len(self) > 0:
            return self._data[len(self) - 1][0]

    def minimum(self):
        if len(self) > 0:
            return self._data[len(self) - 1][1]
        else:
            return None


# Unit Tests:
if __name__ == '__main__':
    s = MinStack()
    s.push(0)
    s.push(-3)
    s.push(5)
    assert(s.minimum() == -3)
    assert(len(s) == 3)
    assert(s.pop() == 5)
    assert(len(s) == 2)
    s.pop()
    assert(s.minimum() == 0)
    assert(s.pop() == 0)
    assert(s.is_empty() == True)
    s.push(9)
    s.push(8)
    s.push(14)
    s.push(-4)
    assert(s.top() == -4)
    assert(s.minimum() == -4)
    s.pop()
    assert(s.minimum() == 8)
    s.pop()
    s.pop()
    assert(s.minimum() == 9)
    s.pop()
    assert(s.is_empty() == True)

