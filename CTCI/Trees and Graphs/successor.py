from binarysearchtree import BinarySearchTree

"""
4.6 - Write an algorithm to find the 'next' node
(i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node
has a link to its parent.
"""

def successor(tree, node):
    if node._right:
        successor = node._right
        while(successor._left):
            successor = successor._left
        return successor
    else:
        if node._parent:
            parent = node._parent
            while (parent):
                if parent._item > node._item:
                    return parent
                parent = parent._parent
    return None

# Unit Tests:
if __name__ == '__main__':
    bst = BinarySearchTree()
    a = bst.add(15)
    b = bst.add(10)
    c = bst.add(20)
    d = bst.add(8)
    e = bst.add(14)
    f = bst.add(30)
    g = bst.add(16)
    h = bst.add(1)
    assert(successor(bst, a) == g)
    assert(successor(bst, b) == e)
    assert(successor(bst, c) == f)
    assert(successor(bst, d) == b)
    assert(successor(bst, e) == a)
    assert(successor(bst, f) == None)
    assert(successor(bst, g) == c)
    assert(successor(bst, h) == d)

