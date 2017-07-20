from singlylinkedlist import LinkedList
from copy import deepcopy

"""
2.6 - Implement a function to check if a linked list is a palindrome or not.
"""

def is_palindrome(llist):
    llist = deepcopy(llist)    # remove this line if you want it done in-place
    even = True if (len(llist) % 2 == 0) else False
    middle = len(llist) // 2
    prevnode = None
    curnode = llist._head
    while(curnode and middle > 0):
        nextnode = curnode._next
        curnode._next = prevnode
        prevnode = curnode
        curnode = nextnode
        middle -= 1
    left = prevnode
    right = curnode if even else curnode._next
    while(left and right):
        if (left.item() != right.item()):
            return False
        left = left._next
        right = right._next
    return True


# Unit Tests:
if __name__ == '__main__':
    llist = LinkedList()
    llist2 = LinkedList()
    llist3 = LinkedList()
    llist4 = LinkedList()
    llist5 = LinkedList()
    llist.add(3)
    llist2.add(3)
    assert(is_palindrome(llist) == True)
    llist.add(3)
    llist2.add(5)
    assert(is_palindrome(llist) == True)
    assert(is_palindrome(llist2) == False)
    llist3.add(3)
    llist3.add(2)
    llist3.add(1)
    llist3.add(1)
    llist3.add(2)
    llist3.add(3)
    assert(is_palindrome(llist3) == True)
    llist4.add(3)
    llist4.add(2)
    llist4.add(1)
    llist4.add(10)
    llist4.add(1)
    llist4.add(2)
    llist4.add(3)
    assert(is_palindrome(llist4) == True)
    llist5.add(3)
    llist5.add(10)
    llist5.add(2)
    llist5.add(1)
    llist5.add(10)
    llist5.add(1)
    llist5.add(2)
    llist5.add(3)
    assert(is_palindrome(llist5) == False)

