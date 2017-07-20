"""
3.4 - Implement a Queue using two Stacks. 
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
        else:
            raise IndexError('Cannot pop an empty Stack!')

    def top(self):
        if not self.is_empty():
            return self._data[len(self) - 1]
        else:
            raise IndexError('Cannot check the top of an empty Stack!')

class Queue:

    def __init__(self):
        self._in = Stack()
        self._out = Stack()

    def __len__(self):
        return len(self._in) + len(self._out)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, i):
        self._in.push(i)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Cannot dequeue an empty Queue.')
        if self._out.is_empty():
            while(not self._in.is_empty()):
                self._out.push(self._in.pop())
        return self._out.pop()

    def front(self):
        if self.is_empty():
            raise IndexError('Cannot dequeue an empty Queue.')
        if self._out.is_empty():
            while(not self._in.is_empty()):
                self._out.push(self._in.pop())
        return self._out._data[len(self._out) - 1]


# Unit Tests:
if __name__ == '__main__':
    q = Queue()
    assert(len(q) == 0)
    assert(q.is_empty() == True)
    q.enqueue('test')
    assert(q.front() == 'test')
    assert(len(q) == 1)
    assert(q.is_empty() == False)
    assert(q.dequeue() == 'test')
    assert(q.is_empty() == True)
    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(-3)
    q.enqueue(9)
    q.enqueue('test')
    assert(len(q) == 5)
    assert(q.front() == 5)
    q.dequeue()
    q.dequeue()
    assert(q.dequeue() == -3)
    q.dequeue()
    assert(q.dequeue() == 'test')
    assert(q.is_empty() == True)

