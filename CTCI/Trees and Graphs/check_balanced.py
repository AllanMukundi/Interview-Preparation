from binarysearchtree import BinarySearchTree
from AVLTree import AVLTree
from random import randrange

"""
4.4 - Implement a function to check if a binary tree is balanced.
For the purposes of this question, a balanced tree is defined to
be a tree such that the heights of the left and right subtrees
never differ by more than one.
"""

def _balanced(node):
    if node is None:
        return 0
    left = _balanced(node._left)
    right = _balanced(node._right)
    if (left == -1) or (right == -1) or abs(left - right) > 1:
        return -1
    return 1 + max(left, right)

def is_balanced(root):
    if root is None:
        return True
    return (_balanced(root) != -1)

# Unit Tests:
if __name__ == '__main__':
    avl1 = AVLTree()
    avl2 = AVLTree()
    avl3 = AVLTree()
    bst1 = BinarySearchTree()
    bst2 = BinarySearchTree()
    bst3 = BinarySearchTree()
    for i in range(100):
        avl1.add(randrange(1, 1000))
    for i in range(100):
        avl2.add(randrange(1, 1000))
    for i in range(100):
        avl3.add(randrange(1, 1000))
    for i in range(0, 1000, 5):
        bst1.add(i)
    for i in range(1000, -1, -5):
        bst2.add(i)
    bst3.add(25)
    assert(is_balanced(bst3.root()) == True)
    bst3.add(10)
    bst3.add(30)
    assert(is_balanced(bst3.root()) == True)
    bst3.add(5)
    bst3.add(15)
    bst3.add(28)
    bst3.add(35)
    assert(is_balanced(avl1.root()) == True)
    assert(is_balanced(avl2.root()) == True)
    assert(is_balanced(avl3.root()) == True)
    assert(is_balanced(bst1.root()) == False)
    assert(is_balanced(bst2.root()) == False)
    assert(is_balanced(bst3.root()) == True)

