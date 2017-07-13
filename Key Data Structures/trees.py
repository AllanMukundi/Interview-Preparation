from linkedqueue import LinkedQueue

"""
An implementation of a Tree abstract base classes for various applications.
"""

class Tree:
    """An abstract base class describing a Tree."""

    class Position:
        """An abstraction representing an item's location."""
        
        def item(self):
            """Returns the item stored at this Position."""
            raise NotImplementedError('Subclass must implement this.')

        def __eq__(self, other):
            """Returns 'True' if other is a Position representing the same location and 'False' otherwise.""" 
            raise NotImplementedError('Subclass must implement this.')

        def __ne__(self, other):
            """Returns 'True' if other does not represent the same location and 'False' otherwise."""
            return not (self == other)

    def root(self):
        """Returns a Position representing the Tree's root (or None if the Tree is empty)."""
        raise NotImplementedError('Subclass must implement this.')

    def parent(self, p):
        """Returns a Position representing Position p's parent (or None if p is the root)."""
        raise NotImplementedError('Subclass must implement this.')

    def num_children(self, p):
        """Returns the number of children belonging to Position p."""
        raise NotImplementedError('Subclass must implement this.')

    def children(self, p):
        """Generates an iteration of Positions representing Position p's children."""
        raise NotImplementedError('Subclass must implement this.')

    def __len__(self):
        """Returns the total number of items in the Tree."""
        raise NotImplementedError('Subclass must implement this.')

    def is_root(self, p):
        """Returns 'True' if Position p is the root of the Tree and 'False' otherwise."""
        return (self.root() == p)

    def is_leaf(self, p):
        """Returns 'True' if Position p does not have any children and 'False' otherwise."""
        return (self.num_children(p) == 0)

    def is_empty(self):
        """Returns 'True' if the Tree is empty and 'False' otherwise."""
        return (self._size == 0)

    def __iter__(self):
        """Generates an iteration of the Tree's items."""
        for p in self.positions():
            yield p.item()

    def positions(self):
        """Generates an iteration of the Tree's positions."""
        return self.preorder()

    def preorder(self):
        """Generates a pre-order iteration of the Positions in the Tree."""
        if not self.is_empty():
            for p in self._preorder(self.root()):
                yield p

    def _preorder(self, p):
        """Generates a pre-order iteration of the Positions in the subtree rooted at p."""
        yield p
        for child in self.children(p):
            for other in self._preorder(child):
                yield other

    def postorder(self):
        """Generates a post-order iteration of the Positions in the Tree."""
        if not self.is_empty():
            for p in self._postorder(self.root()):
                yield p

    def _postorder(self, p):
        """Generates a post-order iteration of the Positions in the subtree rooted at p."""
        for child in self.children(p):
            for other in self._postorder(child):
                yield other
        yield p

    def breadth_first(self):
        """Generates a breadth-first iteration of the Positions in the Tree."""
        if not self.is_empty():
            q = LinkedQueue()
            q.enqueue(self.root())
            while not q.is_empty():
                p = q.dequeue()
                yield p
                for child in self.children(p):
                    q.enqueue(child)


class BinaryTree(Tree):
    """An abstract base class describing a Binary Tree."""

    def left(self, p):
        """
        Returns a Position representing Position p's left child.
        Returns None if p does not have a left child.
        """
        raise NotImplementedError('Subclass must implement this.')

    def right(self, p):
        """
        Returns a Position representing Position p's right child.
        Returns None if p does not have a right child.
        """
        raise NotImplementedError('Subclass must implement this.')

    def sibling(self, p):
        """Returns a Position representing p's sibling (or None if no sibling exists)."""
        parent = self.parent(p)
        if parent is None:
            return None
        elif (p == self.left(parent)):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        """Generates an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generates an in-order iteration of the Positions in a Tree."""
        if not self.is_empty():
            for p in self._inorder(self.root()):
                yield p

    def _inorder(self, p):
        """Generates an in-order iteration of the Positions in the subtree rooted at p."""
        if self.left(p) is not None:
            for other in self._inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._inorder(self.right(p)):
                yield other

    def positions(self):
        """Generates an iteration of the Tree's Positions."""
        return self.inorder()

