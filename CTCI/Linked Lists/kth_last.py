from singlylinkedlist import LinkedList

"""
2.2 - Implement an algorithm to find the kth to
last element of a singly linked list.
"""

def kth_to_last(llist, k): 
    if not (0 < k and k >= len(llist)): 
        raise KeyError('k is out of range.')
    start = end = llist._head
    walk = k
    while(walk and end is not None):
        end = end._next
        walk -= 1
    while(end):
        start = start._next
        end = end._next
    return start


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
    assert(kth_to_last(ll, 5).item() == 9)

