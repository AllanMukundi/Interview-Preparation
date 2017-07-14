from linkedqueue import LinkedQueue

"""
An implementation of a Binary Search Tree.
"""

# Decided to use Nodes as references instead of Positions as the 
# Positions abstraction may not be optimal for an interview setting.

class BinarySearchTree:
    """Binary Search Tree implementation."""

    class _Node:
        """A lightweight, non-public class used for storing a node."""
        __slots__ = '_item', '_parent', '_left', '_right',    # streamline memory usage

        def __init__(self, item, parent=None, left=None, right=None):
            """Initializes a Node."""
            self._item = item
            self._parent = parent
            self._left = left
            self._right = right

    # Constructor:

    def __init__(self):
        """Initializes an empty Binary Search Tree."""
        self._root = None
        self._size = 0

    # Utility Methods

    def _search(self, node, item):
        """
        Searches the subtree rooted at node for the specified item and returns 
        the Node containing it (if it exists) or the last Node searched.
        """
        if (item == node._item):
            return node
        elif (item < node._item):
            if (node._left):
                return self._search(node._left, item)
        elif (item > node._item):
            if (node._right):
                return self._search(node._right, item)
        return node    # unsuccessful search

    def _first(self, node):
        """Returns the Node with the smallest item in the subtree rooted at node."""
        walk = node
        while walk._left is not None:
            walk = walk._left
        return walk

    def _last(self, node):
        """Returns the Node with the largest item in the subtree rooted at node."""
        walk = node
        while walk._right is not None:
            walk = walk._right
        return walk

    def is_empty(self):
        """Returns 'True' if the Tree is empty and 'False' otherwise."""
        return (self._size == 0)

    def is_root(self, node):
        """Returns 'True' if node is the root of the Tree and 'False' otherwise."""
        return (self._root == node)

    def is_leaf(self, node):
        """Returns 'True' if node is a leaf of the Tree and 'False' otherwise."""
        if (node._left or node._right):
            return False
        return True

    def _preorder(self, node):
        """generates a pre-order iteration of the nodes in the subtree rooted at node."""
        yield node
        for child in self.children(node):
            for each in self._preorder(child):
                yield each

    def _postorder(self, node):
        """generates a post-order iteration of the nodes in the subtree rooted at node."""
        for child in self.children(node):
            for each in self._postorder(child):
                yield each
        yield node

    def _inorder(self, node):
        """Generates an in-order iteration of the Nodes in the subtree rooted at node."""
        if (node._left):
            for other in self._inorder(node._left):
                yield other
        yield node
        if (node._right):
            for other in self._inorder(node._right):
                yield other
    
    def _height(self, node):
        """Returns the height of the subtree rooted at node."""
        if self.is_leaf(node):
            return 0
        else:
            return max(self._height(child) for child in self.children(node)) + 1

    def _delete(self, node):
        """
        Deletes node and replaces it with its child, if any.
        """
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node

    # ----------AVL Tree----------

    def _rebalance_add(self, node):
        pass

    def _rebalance_del(self, node):
        pass

    # ----------------------------

    # Accessors:

    def __len__(self):
        """Returns the number of items in the Tree."""
        return self._size

    def root(self):
        """Returns the root Node of the Tree."""
        return self._root if len(self) > 0 else None

    def first(self):
        """Returns the first (smallest) Node in the Tree."""
        return self._first(self.root()) if len(self) > 0 else None

    def last(self):
        """Returns the last (biggest) Node in the Tree."""
        return self._last(self.root()) if len(self) > 0 else None

    def children(self, node):
        """Generates an iteration of node's children."""
        if (node._left):
            yield node._left
        if (node._right):
            yield node._right

    def height(self, node=None):
        """
        Returns the height of the subtree rooted at node.
        If node is None, returns the height of the entire Tree.
        """
        if (node == None):
            node = self.root()
        return self._height(node)

    def depth(self, node):
        """Returns the number of levels between node and the Tree's root."""
        if self.is_root(node):
            return 0
        else:
            return 1 + self.depth(node._parent)

    def breadthfirst(self):
        """Generates a breadth-first iteration of the Nodes in the Tree."""
        if not self.is_empty():
            q = LinkedQueue()
            q.enqueue(self.root())
            while not q.is_empty():
                start = q.dequeue()
                yield start
                for child in self.children(start):
                    q.enqueue(child)
                print('------------------')
    
    def preorder(self):
        """generates a pre-order iteration of the nodes in the tree."""
        if not self.is_empty():
            for node in self._preorder(self.root()):
                yield node

    def postorder(self):
        """generates a post-order iteration of the nodes in the tree."""
        if not self.is_empty():
            for node in self._postorder(self.root()):
                yield node

    def inorder(self):
        """generates an in-order iteration of the nodes in the tree."""
        if not self.is_empty():
            for node in self._inorder(self.root()):
                yield node

    # Mutators:

    def add(self, i):
        """Adds a Node with item i to the Tree."""
        if self.is_empty():
            self._root = self._Node(i)
            leaf = self.root()
        else:
            parent = self._search(self.root(), i)
            leaf = self._Node(i, parent)
            if (i == parent._item):
                return
            elif (i < parent._item):
                parent._left = leaf
            else:
                parent._right = leaf
        self._size += 1
        self._rebalance_add(leaf)

    def delete(self, i):
        """Removes the Node with item i from the Tree."""
        if not self.is_empty():
            curnode = self._search(self.root(), i)
            if (i == curnode._item):
                if (curnode._left and curnode._right):
                    replacement = self._last(curnode._left)
                    curnode._item = replacement._item
                    curnode = replacement
                parent = curnode._parent
                self._delete(curnode)
                self._rebalance_del(parent)
                return
            else:
                raise ValueError('No node with the specified item exists.')
        raise ValueError('No node with the specified item exists.')


# Unit Tests:
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.add(4)
    assert(bst.root()._item == 4)
    bst.add(1)
    bst.add(10)
    assert(len(bst) == 3)
    assert(bst.first()._item == 1)
    assert(bst.last()._item == 10)
    bst.add(0)
    bst.add(15)
    assert(bst.depth(bst.last()) == 2)
    assert(bst.height() == 2)
    bst.delete(10)
    assert(len(bst) == 4)
    bst.delete(4)
    bst.delete(1)
    bst.delete(0)
    assert(bst.root()._item == 15)
    bst.delete(15)
    assert(bst.is_empty() == True)

