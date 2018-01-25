from binarysearchtree import BinarySearchTree

def is_balanced(root):
    return _is_balanced(root) != -1

def _is_balanced(node):
    if node is None:
        return 0
    left_height = _is_balanced(node._left)
    right_height = _is_balanced(node._right)
    if (left_height == -1) or (right_height == -1) or (abs(left_height-right_height) > 1):
        return -1
    else:
        return 1 + max(left_height, right_height)

# Unit Tests:
if __name__ == '__main__':
    t1 = BinarySearchTree()
    t1.add(20)
    assert(is_balanced(t1.root()) == True)
    t1.add(30)
    t1.add(40)
    assert(is_balanced(t1.root()) == False)
    t1.add(10)
    assert(is_balanced(t1.root()) == True)
    t1.add(5)
    assert(is_balanced(t1.root()) == True)
    t2 = BinarySearchTree()
    for i in range(0, 10):
        t2.add(i)
    assert(is_balanced(t2.root()) == False)
    t3 = BinarySearchTree()
    t3.add(0)
    assert(is_balanced(t3.root()) == True)
    t3.add(-5)
    t3.add(5)
    t3.add(2.5)
    assert(is_balanced(t3.root()) == True)
    t3.add(7.5)
    t3.add(-2.5)
    t3.add(-7.5)
    assert(is_balanced(t3.root()) == True)
