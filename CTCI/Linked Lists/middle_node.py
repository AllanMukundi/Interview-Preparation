from singlylinkedlist import LinkedList

"""
2.3 - Implement an algorithm to delete a node in the middle
(any node except the first or last node) of a singly linked
list, given only access to that node.
"""

def delete_middle(llist, node):
    curnode = node
    nextnode = curnode._next
    curnode._item = nextnode._item
    curnode._next = nextnode._next


# Output Tests:
if __name__ == '__main__':
    ll = LinkedList()
    ll.add(3)
    ll.add(13)
    ll.add(21)
    ll.add(17)
    ll.delete(3)
    middle = ll.add(0)
    ll.add(-5)
    print(ll)
    delete_middle(ll, middle)
    print(ll)

