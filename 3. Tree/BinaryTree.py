from Tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Concrete class representing a linked binary tree"""
    class _Node:
        def __init__(self, element, parent = None, left  = None, right = None):
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
    
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        count = 0
        node = self._validate(p)
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1    
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('root exists')
        self._root = self._Node(e)
        self._size += 1
        return self._make_position(self._root)
    
    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('right child exists')
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)
    
    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('left child exists')
        node._left = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left)

    def _delete(self, p):
        num_child = self.num_children(p)
        if num_child is 2:
            raise ValueError('two children exists') 

        node = self._validate(p)  
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
        self._size = -1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")
        self._size = self._size + len(t1) + len(t2)

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
            







    



