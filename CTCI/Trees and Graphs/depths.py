from random import randrange
from queue import Queue
from singlylinkedlist import LinkedList
from binarysearchtree import BinarySearchTree

"""
4.3 - Given a binary tree, design an algorithm
which creates a linked list of all the nodes
at each depth (if you have a tree with depth D,
you will have D linked lists).
"""

def children(node):
    if node._left:
        yield node._left
    if node._right:
        yield node._right

def depths(root):
    result = []
    depth = old = 0
    queue = Queue()
    queue.enqueue((root, depth))
    llist = LinkedList()
    while not queue.is_empty():
        node, depth = queue.dequeue()
        if (depth == old):
            llist.add(node)
        else:
            result.append(llist)
            llist = LinkedList()
            llist.add(node)
            old = depth
        for child in children(node):
            queue.enqueue((child, depth+1))
    return result+[llist] if llist is not result[-1] else result


# Output Tests:
if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in range(100):
        bst.add(randrange(0, 1000))
    for each in depths(bst.root()):
        print(each)
        
