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


def stack_sort(stack):
    temp_stack = Stack()
    while(not stack.is_empty()):
        temp = stack.pop()
        while(not temp_stack.is_empty() and temp < temp_stack.top()):
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    while(not temp_stack.is_empty()):
        stack.push(temp_stack.pop())


# Output Test:
if __name__ == '__main__':
    s = Stack()
    s.push(8)
    s.push(0)
    s.push(-4)
    s.push(11)
    s.push(19)
    s.push(21)
    s.push(3)
    s.push(14)
    s.push(1)
    s.push(14)
    print(s._data)
    stack_sort(s)
    print(s._data)

