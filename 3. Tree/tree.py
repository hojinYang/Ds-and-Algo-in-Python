class Tree:
    """Abstract base class representing a tree structure"""

    #-----------nested Position Class--------------#
    class Position:
        """An abstraction represnting the location of a single element."""

        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            """Return true if other Position represents the same location"""
            raise NotImplementedError('must be implemented by subclass')
        
        def __ne__(self, other):
            """Return ture if other does not represent the same location"""
            return (self == other)
        
    #-----------abstract methods that concrete subclass must support---------#
    def root(self):
        """Return Position representing the trees root"""
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        """Return Positon representing p's parent"""
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        """Return the number of children that Position P has"""
        raise NotImplementedError('must be implemented by subclass')

    def childern(self, p):
        """Generate an iteratoin of Positions representing p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any child"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Positon p from the root"""
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def height_1(self, p):
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height_1(c) for c in self.childern(p))

    def height(self, p=None):
        """Return the height of the subtree roorted at Position p."""
        if p == None:
            p = self.root()
        
        return self.height_1(p)

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # -------------- additional abstraction methods-----------------
    def left(self, p):
        """Return a Position representing p's left child."""
        raise NotImplementedError('must be implemented by subclass')
    
    def right(self, p):
        """Return a Position representing p's right child."""
        raise NotImplementedError('must be implemented by subclass')
    
    #--------------- concrete methods implemented in this class ----
    def sibling(self, p):
        """Return a Positon representing p's sibling(or None if no sibling)"""
        parent = self.parent(p)
        if parent == None:
            return None
        else:
            if p == self.left(parent):
                return self.right(p)
            else:
                return self.left(p)
    
    def children(self, p):
        """Generate an iteration of Position representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.left(p) is not None:
            yield self.right(p)

            
        

        
        




     


        
