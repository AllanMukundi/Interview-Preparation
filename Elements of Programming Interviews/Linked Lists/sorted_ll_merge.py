from singlylinkedlist import LinkedList

def sorted_ll_merge(l1, l2):
    curnode_l1 = l1._head
    curnode_l2 = l2._head
    new_ll = LinkedList()
    while(True):
        if (curnode_l1 is None and curnode_l2 is None):
            break
        elif (curnode_l1 is None or (curnode_l2 and curnode_l2._item < curnode_l1._item)):
            new_ll.add(curnode_l2._item)
            curnode_l2 = curnode_l2._next
        else:
            new_ll.add(curnode_l1._item)
            curnode_l1 = curnode_l1._next
    return new_ll

# Unit Tests:
if __name__ == '__main__':
    l1 = LinkedList()
    for i in range(0, 101, 20):
        l1.add(i)
    l2 = LinkedList()
    for i in range(-20, 31, 7):
        l2.add(i)
    assert(str(sorted_ll_merge(l1, l2)) == '-20 -> -13 -> -6 -> 0 -> 1 -> 8 -> 15 -> 20 -> 22 -> 29 -> 40 -> 60 -> 80 -> 100')
    l3 = l2
    l4 = LinkedList()
    assert(str(sorted_ll_merge(l3, l4)) == str(l3))
    l5 = LinkedList()
    l5.add(0)
    l6 = LinkedList()
    l6.add(1)
    assert(str(sorted_ll_merge(l5, l6)) == '0 -> 1')
