from DoublyLinkedList import _DoublyLinkedList

class PositionalList(_DoublyLinkedList):
    """A sequencial container of elements allowing positional access"""
    #-----------------Nested Positon class--------------
    class Position:
        def __init__(self, node, container):
            self._node = node
            self._container = container
        
        def element(self):
            """ return element of the position"""
            return self._node._element
        
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            return not (self == other)

    
    #----------------Utility method--------------------
    def _validate(self, p):
        """ Return position's node, or raise appropriate error if invalid """
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Positon type')
        
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        
        return p._node
    
    def _make_position(self, node):
        """Return node's positoin"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(node, self)
    

    #---------------accessor------------------------------
    def first(self):
        return self._make_position(self._header._next)
    
    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """Generate a forward iteration of the element in the list"""
        p = self.first()
        while p is not None:
            yield p.element()
            p = self.after(p)
    
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position"""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)
    
    def add_after(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)
    

if __name__ == '__main__':
    PL = PositionalList()
    p = PL.add_first(10)
    p = PL.add_after(p, 30)
    p = PL.add_before(p, 20)
    for i in PL:
        print(i)
    


        

