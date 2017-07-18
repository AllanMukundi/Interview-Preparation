from singlylinkedlist import LinkedList

"""
2.5 - You have two numbers represented by a linked list, where 
each node contains a single digit. The digits are stored in 
reverse order, such that the ones digit is at the head of the
list. Write a function that adds the two numbers and returns
the sum in reverse as a linked list.
"""

def sum_lists(llist1, llist2):
    str1 = str2 = ""
    curnode = llist1._head
    while (curnode):
        str1 += str(curnode.item())
        curnode = curnode._next
    curnode = llist2._head
    while (curnode):
        str2 += str(curnode.item())
        curnode = curnode._next
    str1 = str1[::-1]
    str2 = str2[::-1]
    total = list(str(int(str1) + int(str2)))
    totallist = LinkedList()
    for i in range(len(total)-1, -1, -1):
        totallist.add(total[i])
    return totallist


# Output Test:
num1 = LinkedList()
num1.add(7)
num1.add(1)
num1.add(6)
num2 = LinkedList()
num2.add(0)
num2.add(9)
num2.add(2)
print(sum_lists(num1, num2))

