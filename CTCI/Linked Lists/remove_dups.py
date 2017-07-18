from doublylinkedlist import LinkedList
from collections import Counter

"""
2.1 - Write code to remove duplicates from an
unsorted linked list. How would you do it without
using an auxiliary structure?
"""

def remove_dups(llist):
    count = Counter()
    curnode = llist._head
    while(curnode):
        if (count[curnode.item()] != 0):
            if curnode != llist._head:
                curnode._prev._next = curnode._next
            else:
                llist._head = curnode._next
            if curnode._next:
                curnode._next._prev = curnode._prev
            if curnode == llist._tail:
                llist._tail = curnode._prev
            llist._size -= 1
        else:
            count[curnode.item()] += 1
        curnode = curnode._next


def remove_dups_v2(llist):
    if not llist.is_empty():
        start = llist._head
        marker = start.item()
        curnode = start._next
        while(start != llist._tail):
            while(curnode):
                if (curnode.item() == marker):
                    if curnode != llist._head:
                        curnode._prev._next = curnode._next
                    else:
                        llist._head = curnode._next
                    if curnode._next:
                        curnode._next._prev = curnode._prev
                    if curnode == llist._tail:
                        llist._tail = curnode._prev
                    llist._size -= 1
                curnode = curnode._next
            start = start._next
            marker = start.item()
            curnode = start._next


# Output Tests:
if __name__ == '__main__':
    llist = LinkedList()
    llist.add(3)
    llist.add(7)
    llist.add(0)
    llist.add(3)
    llist.add(-1)
    llist.add(2)
    llist.add(3)
    llist.add(0)
    llist.add(3)
    llist.add(14)
    llist.add(3)
    print(llist)
    llist_v2 = llist
    remove_dups(llist)
    remove_dups(llist_v2)
    print(llist)
    print(llist_v2)

