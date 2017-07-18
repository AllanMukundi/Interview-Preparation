from singlylinkedlist import LinkedList

"""
2.4 - Write code to partition a linked list around a value x,
such that all nodes less than x comes before all nodes greater
than or equal to x. If x is contained within the list, the
values of x only need to be after the elements less than x.
"""

def partition(llist, val):
    curnode = llist._tail = llist._head
    if not llist.is_empty():
        while (curnode):
            nextnode = curnode._next
            curnode._next = None
            if (curnode.item() < val):
                curnode._next = ll._head
                ll._head = curnode
            else:
                ll._tail._next = curnode
                ll._tail = curnode
            curnode = nextnode
    if llist._tail._next is not None:
        ll._tail._next = None


ll = LinkedList()
ll.add(3)
ll.add(5)
ll.add(8)
ll.add(5)
ll.add(10)
ll.add(2)
ll.add(1)
print(ll)
partition(ll, 5)
print(ll)

