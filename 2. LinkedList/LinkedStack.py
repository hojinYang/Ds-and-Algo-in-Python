class LinkedStack:
    """Stack implementation using linked list"""
    #------------Node implementation-------------
    class _Node:
        def __init__(self, element, next = None):
            self._element = element
            self._next = next
        
    def __init__(self):
        self._size = 0
        self._head = None
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, e):
        newest = self._Node(e, self._head)
        self._head = newest
        self._size += 1 
    
    def pop(self):
        if self.is_empty():
            raise ValueError("Queue is Empty")
        
        node = self._head
        self._head = self._head._next
        ret = node._element
        node._element = node._next = None
        self._size -= 1
        return ret
    
    def top(self):
        if self.is_empty():
            raise ValueError("Queue is Empty")
        
        return self._head._element
    


