from binarysearchtree import BinarySearchTree

"""
4.5 - Implement a function to check if a binary
tree is a binary search tree.
"""

def is_bst(root):
    bound = (float('-inf'), float('inf'))
    return validate(root, bound)

def validate(node, bound):
    if node is None:
        return True
    elif (node._item < bound[0] or bound[1] < node._item):
        return False
    return validate(node._left, (bound[0], node._item)) and validate(node._right, (node._item, bound[1]))


# Unit Tests:
if __name__ == '__main__':
    bst = BinarySearchTree()
    assert(is_bst(bst.root()) == True)
    bst.add(15)
    assert(is_bst(bst.root()) == True)
    bst.add(10)
    bst.add(20)
    bst.add(8)
    bst.add(14)
    bst.add(30)
    assert(is_bst(bst.root()) == True)
    bst._root._item = 11
    assert(is_bst(bst.root()) == False)

