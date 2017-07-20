"""
3.3 - Imagine a (literal) stack of plates. If the stack gets too
high, it might topple. Therefore, in real life, we would likely
start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOfStacks which mimics this.

--

SetOfStacks should be composed of several stacks and should create
a new stack once the previous one exceeds capacity. Operations
should mimic those of a single stack.

--

Implement a function popAt(index) which performs a pop operation on
a specific sub-stack.
"""

class SetOfStacks:

    class _Stack:

        def __init__(self):
            self._data = []

        def __len__(self):
            return len(self._data)

        def is_empty(self):
            return len(self) == 0

        def push(self, i):
            self._data.append(i)

        def pop(self):
            if self.is_empty():
                raise IndexError('Cannot pop an empty Stack.')
            return self._data.pop()

        def top(self):
            if self.is_empty():
                raise IndexError('Cannot check the top of an empty Stack.')
            return self._data[len(self) - 1]

    CAPACITY = 4 

    def __init__(self):
        self._stacks = [self._Stack()]
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        return len(self) == 0

    def push(self, i):
        stack_num = len(self) // SetOfStacks.CAPACITY
        self._stacks[stack_num].push(i)
        stack_len = len(self._stacks[stack_num])
        if (stack_len) >= SetOfStacks.CAPACITY:
            self._stacks.append(self._Stack())
        self._length += 1

    def pop(self):
        stack_num = (len(self) - 1) // SetOfStacks.CAPACITY
        val = self._stacks[stack_num].pop()
        self._length -= 1
        return val

    def top(self):
        stack_num = (len(self) - 1) // SetOfStacks.CAPACITY
        return self._stacks[stack_num].top()

    def popAt(self, index):
        if index < len(self._stacks):
            val = self._stacks[index].pop()
            if self._stacks[index].is_empty():
                self._stacks.pop(index)    # O(n) but this is more efficient than rolling over elements
            self._length -= 1
            return val
        raise IndexError('Index is out of range.')


if __name__ == '__main__':
    s = SetOfStacks()
    for i in 'abcdefghijklmnopqrstuvwxyz0123456789':
        s.push(i)
    assert(len(s) == 36)
    assert(s._stacks[-1].is_empty() == True)
    s.popAt(-2)
    assert(s.popAt(-2)== '8')
    assert(s.popAt(3) == 'p')
    s.popAt(3)
    s.popAt(3)
    s.popAt(3)
    assert(s.popAt(3) == 't')
    assert(len(s) ==  29)

