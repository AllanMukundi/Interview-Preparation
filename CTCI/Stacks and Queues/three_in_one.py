"""
3.1 - Describe how you could use a single
array to implement three stacks.
"""

class MultiStack:

    def __init__(self, capacity):
        self._num_stacks = 3
        self._stack_capacity = capacity
        self._data = [None] * (self._num_stacks * self._stack_capacity)
        self._sizes = [0] * self._num_stacks

    def _validate(self, stacknum):
        if not (0 <= stacknum < self._num_stacks):
            raise IndexError('The given stack number is out of range.')

    def __len__(self):
        return sum(self._sizes)

    def stack_len(self, stacknum):
        self._validate(stacknum)
        return self._sizes[stacknum]

    def is_empty(self):
        return len(self) == 0

    def stack_empty(self, stacknum):
        self._validate(stacknum)
        return self._sizes[stacknum] == 0

    def push(self, i, stacknum):
        self._validate(stacknum)
        if (self._sizes[stacknum] == self._stack_capacity):
            raise IndexError('Cannot push onto a full Stack.')
        index = self._set_top(stacknum)
        self._data[index] = i
        self._sizes[stacknum] += 1

    def pop(self, stacknum):
        self._validate(stacknum)
        if (self._sizes[stacknum] == 0):
            raise IndexError('Cannot pop an empty Stack.')
        index = self._get_top(stacknum)
        val = self._data[index]
        self._data[index] = None
        self._sizes[stacknum] -= 1
        return val

    def top(self, stacknum):
        self._validate(stacknum)
        if (self._sizes[stacknum] == 0):
            raise IndexError('Cannot pop an empty Stack.')
        index = self._get_top(stacknum)
        return self._data[index]

    def _set_top(self, stacknum):
        return (stacknum * self._stack_capacity) + self._sizes[stacknum] 

    def _get_top(self, stacknum):
        return (stacknum * self._stack_capacity) + self._sizes[stacknum] - 1


# Unit Tests:
if __name__ == '__main__':
    stacks = MultiStack(3)
    assert(stacks.is_empty() == True)
    stacks.push(3, 0)
    stacks.push(0, 1)
    stacks.push(-4, 2)
    assert(len(stacks) == 3)
    assert(stacks.top(1) == 0)
    assert(stacks.top(2) == -4)
    assert(stacks.top(0) == 3)
    stacks.push(9, 0)
    stacks.push(19, 0)
    stacks.push(-15, 1)
    stacks.push('test', 1)
    stacks.push('foo', 2)
    stacks.push('bar', 2)
    assert(len(stacks) == 9)
    assert(stacks.pop(0) == 19)
    assert(stacks.pop(1) == 'test')
    assert(stacks.pop(2) == 'bar')
    assert(stacks.pop(0) == 9)
    assert(stacks.pop(1) == -15)
    assert(stacks.pop(2) == 'foo')
    assert(stacks.pop(0) == 3)
    assert(stacks.pop(1) == 0)
    assert(stacks.pop(2) == -4)
    assert(stacks.is_empty() == True)

