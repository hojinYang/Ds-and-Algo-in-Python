class LinkedQueue:
    """Queue implementation using linked list"""
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return ValueError("Queue is empty")
        
        node = self._head
        self._head = self._head._next
        ret = node._element
        node._next = node._element = None
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return ret

    def first(self):
        if self.is_empty():
            return ValueError("Queue is empty")
        
        return self._head._element
    



    