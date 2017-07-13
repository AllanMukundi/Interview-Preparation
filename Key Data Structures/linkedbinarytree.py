from trees import BinaryTree

"""
A linked implementation of a Binary Tree.
"""

class LinkedBinaryTree(BinaryTree):
    """Linked Binary Tree implementation."""

    class _Node:
        """A lightweight, non-public class used for storing a node."""
        __slots__ = '_item', '_parent', '_left', '_right'    # streamline memory usage

        def __init__(self, item, parent=None, left=None, right=None):
            """Initializes a Node."""
            self._item = item
            self._parent = parent
            self._left = left
            self._right = right

    class Position:
        """An abstraction representing an item's location."""

        def __init__(self, container, node):
            """Initializes a Position (should not be called by users)."""
            self._container = container
            self._node = node

        def item(self):
            """Returns the item stored at this Position."""
            return self._node._item

        def __eq__(self, other):
            """Returns 'True' if other is a Position representing the same location and 'False' otherwise.""" 
            return (type(self) is type(other)) and (self._node is other._node)

    # Constructor:

    def __init__(self):
        """Initializes an empty Binary Tree."""
        self._root = None
        self._size = 0 

    # Utility Methods:

    def _validate(self, p):
        """Returns Position p's node."""
        if not isinstance(p, self.Position):
            raise TypeError('p is not a Position.')
        if p._container is not self:
            raise ValueError('p does not belong to this Tree.')
        if p._node._parent is p._node:    # convention for a deprecated node
            raise ValueError('p is invalid.')
        return p._node

    def _make_position(self, node):
        """Returns a Position instance for a given node (or None if no node)."""
        if node is None:
            return None
        return self.Position(self, node)

    # Accessors:

    def __len__(self):
        """Returns the number of items in the Tree."""
        return self._size

    def root(self):
        """Returns the root Position of the Tree (or None if the Tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Returns the Position of p's parent (or None if p is the root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Returns the Position of p's left child (or None if there is no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Returns the Position of p's right child (or None if there is no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Returns the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    # Mutators:

    def _add_root(self, i):
        """Places item i at the root of an empty Tree and returns its Position."""
        if self._root is not None:
            raise ValueError('Root already exists.')
        self._size = 1
        self._root = self._Node(i)
        return self._make_position(self._root)

    def _add_left(self, p, i):
        """
        Creates a new left child for Position p, storing item i.
        Returns the Position of the new node.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child already exists.')
        self._size += 1
        node._left = self._Node(i, node)
        return self._make_position(node._left)

    def _add_right(self, p, i):
        """
        Creates a new right child for Position p, storing item i.
        Returns the Position of the new node.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child already exists.')
        self._size += 1
        node._right = self._Node(i, node)
        return self._make_position(node._right)

    def _replace(self, p, i):
        """Replaces the item at Position p with item i and returns the old item."""
        node = self._validate(p)
        old = node._item
        node._item = i
        return old

    def _delete(self, p):
        """
        Deletes the node at Position p and replaces it with its child, if any.
        Returns the element that was stored at Position p.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children.')
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
        node._parent = node    # deprecate node
        return node._item

    def _attach(self, p, t1, t2):
        """Attaches Trees t1 and t2 as left and right subtrees respectively of Position p (leaf)."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be a leaf.')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match.')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0 
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
            
    def depth(self, p):
        """Returns the number of levels between Position p and the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _calc_height(self, p):
        """Returns the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return  max(self._calc_height(x) for x in self.children(p)) + 1

    def height(self, p=None):
        """
        Returns the height of the subtree rooted at Position p.
        If p is None, returns the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._calc_height(p)

       
# Unit Tests:
if __name__ == '__main__':
    tree = LinkedBinaryTree()
    ltree = LinkedBinaryTree()
    rtree = LinkedBinaryTree()
    tree._add_root(3)
    ltree._add_root(14)
    ltree._add_left(ltree.root(), -7)
    ltree._add_right(ltree.root(), 10)
    rtree._add_root(100)
    rtree._add_left(rtree.root(), 15)
    rtree._add_right(rtree.root(), -14)
    tree._attach(tree.root(), ltree, rtree)
    assert(tree.is_empty() == False)
    assert(tree.height() == 2)
    assert(len(tree) == 7)
    assert(tree.num_children(tree.root()) == 2)
    leaf = tree.left(tree.left(tree.root()))
    assert(tree.is_leaf(leaf) == True)
    assert(tree.is_root(leaf) == False)
    assert(tree.depth(leaf) == 2)
    assert(tree.sibling(leaf).item() == 10)
    assert(tree.num_children(leaf) == 0)
    assert(tree.parent(leaf).item() == 14)
    assert(tree._replace(tree.root(), -3) == 3)
    assert(tree.root().item() == -3)
    tree._add_left(leaf, 5)
    assert(tree._delete(leaf) == -7)
    assert(tree.left(tree.left(tree.root())).item() == 5)

