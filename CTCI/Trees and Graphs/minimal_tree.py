from binarysearchtree import BinarySearchTree

"""
4.2 - Given a sorted (increasing order) array with unique
integer elements, write an algorithm to create a binary
search tree with minimal height.
"""

def constructBST(nums):
    if not nums:
        return
    middle = len(nums) // 2
    new_node = BinarySearchTree._Node(nums[middle])
    new_node._left = constructBST(nums[:middle])
    new_node._right = constructBST(nums[middle+1:])
    return new_node


# Unit Tests:

def children(node):
    if node._left:
        yield node._left
    if node._right:
        yield node._right

def height(node):
    if not (node._left or node._right):
        return 0
    else:
        return 1 + max(height(child) for child in children(node))

if __name__ == '__main__':
    nums = [i for i in range(0, 100)]
    t1 = BinarySearchTree()
    t2 = BinarySearchTree()
    t1._root = constructBST(nums)
    for i in range(0, 100):
        t2.add(i)
    assert(height(t1._root) < height(t2._root))

