"""
An implementation of a tree abstract base classes for various applications.
"""

class Tree:
    """An abstract base class describing a tree."""

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
        """Returns a Position representing the tree's root (or None if the tree is empty)."""
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
        return (len(self) == 0)


class BinaryTree(Tree):
    """An abstract base class describing a binary tree."""

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

