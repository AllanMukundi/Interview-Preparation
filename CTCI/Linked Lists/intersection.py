"""
2.7 - Given two singly linked lists, determine if the two
linked lists intersect. Return the intersecting node.
Note that intersection is determined by reference, not by value.
"""

def intersect(llist1, llist2):
    if (llist1._tail != llist2._tail):
        return False
    longer = llist1 if len(llist1) > len(llist2) else llist2
    shorter = llist1 if len(llist1) < len(llist2) else llist2

    curnode_1 = longer._head
    curnode_2 = shorter._head

    while (len(longer) > len(shorter)):
        curnode_1 = curnode_1._next

    while(curnode_1 and curnode_2):
        if (curnode_1 is curnode_2):
            return curnode_1
        else:
            curnode_1 = curnode_1._next
            curnode_2 = curnode_2._next

