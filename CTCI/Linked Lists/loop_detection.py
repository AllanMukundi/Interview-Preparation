from singlylinkedlist import LinkedList

"""
2.8 - Given a circular linked list, implement an algorithm
that returns the node at the beginning of the loop.
"""

def is_loop(llist):
    slow = fast = llist._head
    while(slow._next and fast._next._next):
        slow = slow._next
        fast = fast._next._next
        if (fast == slow):
            break
    slow = llist._head
    while(slow._next and fast._next):
        slow = slow._next
        fast = fast._next
        if (fast == slow):
            return fast
    return None
        

# Unit Tests:
if __name__ == '__main__':
    llist = LinkedList()
    llist.add(3)
    llist.add(8)
    repeat = llist.add(3)
    llist.add(4)
    llist.add(11)
    llist.add(0)
    llist._tail._next = repeat
    print(is_loop(llist).item())

