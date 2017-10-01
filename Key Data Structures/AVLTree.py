from binarysearchtree import BinarySearchTree

"""
An implementation of a self-balancing tree (AVL).
"""

class AVLTree(BinarySearchTree):
    """AVL self-balancing Binary Search Tree implementation."""

    class _Node(BinarySearchTree._Node):
        """A lightweight, non-public class used for storing a node."""
        __slots__ = '_height'    # streamline memory usage

        def __init__(self, item, parent=None, left=None, right=None):
            """Initializes a Node."""
            super().__init__(item, parent, left, right)
            self._height = 0

        # Accessors:

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0

    # Utility Methods:

    def _relink(self, parent, child, is_left):
        """Relinks parent node with child node."""
        if (is_left):
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, node):
        """Rotates node above its parent."""
        parent = node._parent
        grandparent = parent._parent
        if grandparent is None:
            self._root = node
            node._parent = None
        else:
            self._relink(grandparent, node, parent == grandparent._left)
        if (node == parent._left):
            self._relink(parent, node._right, True)
            self._relink(node, parent, False)
        else:
            self._relink(parent, node._left, False)
            self._relink(node, parent, True)
        

    def _restructure(self, node):
        """Performs a trinode restructure of the given node with its parent/grandparent."""
        parent = node._parent
        grandparent = parent._parent
        if (node == parent._left) == (parent == grandparent._left):
            self._rotate(parent)
            return parent
        else:
            self._rotate(node)
            self._rotate(node)
            return node

    def _compute_height(self, node):
        """Recomputes the height of the given node."""
        node._height = 1 + max(node.left_height(), node.right_height())

    def _isbalanced(self, node):
        """Returns 'True' if the subtree rooted at node is balanced and 'False' otherwise."""
        return abs(node.left_height() - node.right_height()) <= 1

    def _tall_child(self, node, left=False):
        """Returns node's tallest child with the parameter 'left' being the tiebreaker."""
        if (node.left_height() + (1 if left else 0) > node.right_height()):
            return node._left
        else:
            return node._right

    def _tall_grandchild(self, node):
        """Retrieves node's tallest grandchild."""
        child = self._tall_child(node)    # node Y
        side = (child == node._left)
        return self._tall_child(child, side)    # node X

    def _rebalance(self, node):
        """Rebalances the AVL Tree."""
        while node is not None:
            old = node._height
            if not self._isbalanced(node):
                node = self._restructure(self._tall_grandchild(node))
                self._compute_height(node._left)
                self._compute_height(node._right)
            self._compute_height(node)
            if (node._height == old):
                node = None    # no need to keep rebalancing
            else:
                node = node._parent

    def _rebalance_add(self, node):
        """Rebalances the Tree upon adding a new node."""
        self._rebalance(node)

    def _rebalance_del(self, node):
        """Rebalances the Tree upon deleting a node."""
        self._rebalance(node)


# Unit Tests:
if __name__ == '__main__':
    avl = AVLTree()
    avl.add(4)
    avl.add(3)
    avl.add(2)
    avl.add(1)
    assert(avl.root()._item == 3)
    avl.add(19)
    avl.add(10)
    assert(len(avl) == 6)
    assert(avl.first()._item == 1)
    avl.add(0)
    avl.add(15)
    assert(avl.depth(avl.last()) == 2)
    assert(avl.height() == 3)
    avl.delete(10)
    assert(len(avl) == 7)
    avl.delete(4)
    avl.delete(1)
    avl.delete(0)
    assert(avl.root()._item == 3)
    avl.delete(15)
    avl.delete(3)
    avl.delete(2)
    avl.delete(19)
    assert(avl.is_empty() == True)

