from singlylinkedlist import LinkedList

"""
2.2 - Implement an algorithm to find the kth to
last element of a singly linked list.
"""

def kth_to_last(llist, k): 
    num = len(llist) - k
    counter = 0 
    curnode = llist._head
    while curnode:
        if (num == counter):
            return curnode.item()
        curnode = curnode._next
        counter += 1
    raise KeyError('k is out of range.')


# Unit Tests:
if __name__ == '__main__':
    ll = LinkedList()
    ll.add(3)
    ll.add(9)
    ll.add(13)
    ll.add(19)
    ll.delete(3)
    ll.add(-5)
    ll.add(21)
    assert(kth_to_last(ll, 1) == ll._tail.item())
    assert(kth_to_last(ll, 3) == 19)
    assert(kth_to_last(ll, 5) == 9)

