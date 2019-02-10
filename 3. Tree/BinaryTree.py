from Tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Concrete class representing a linked binary tree"""
    class _Node:
        def __init__(self, element, left, right, parent):
            self._element = element
            self._left = left
            self._right = right
            self._parent = parent
        
    class Position(BinaryTree.Position):
        def __init__(self, node, container):
            self._node = node
            self._container = container
        
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node

    def _validate(self, p):
        """Return associate node, if position p is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper positon type")

        if p._container is not self:
            raise ValueError('p does not belong to this container')

        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')

        return p._node

    def _make_position(self, node):
        return self.Position(node, self) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    



