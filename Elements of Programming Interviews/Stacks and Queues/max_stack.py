class MaxStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def max(self):
        if self.is_empty():
            raise IndexError('Cannot get the max value of an empty Stack.')
        return self._data[-1][1]

    def pop(self):
        if self.is_empty():
            raise IndexError('Cannot pop an empty Stack.')
        return self._data.pop()[0]

    def push(self, i): 
        new_max = i if len(self) == 0 or i > self.max() else self.max()
        self._data.append((i, new_max))

# Unit Tests:
if __name__ == '__main__':
    ms = MaxStack()
    assert(ms.is_empty() == True)
    ms.push(3)
    assert(ms.is_empty() == False)
    assert(ms.max() == 3)
    ms.push(5)
    ms.pop()
    assert(ms.max() == 3)
    ms.push(0)
    assert(ms.max() == 3)
    ms.push(-5)
    assert(len(ms) == 3)
    ms.push(15)
    assert(ms.max() == 15)
    ms.push(4)
    assert(ms.max() == 15)
    ms.pop()
    assert(ms.pop() == 15)
    assert(ms.max() == 3)
    ms.pop()
    ms.pop()
    ms.pop()
    assert(ms.is_empty() == True)
