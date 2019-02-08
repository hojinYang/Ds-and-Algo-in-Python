from DoublyLinkedList import _DoublyLinkedList

class LinkedDequeue(_DoublyLinkedList):
    """Dequeue implementation based on doubly linked list"""
    def first(self):
        """Return the element of the first node"""
        if self.is_empty():
            pass
        return self._header._next._element

    def last(self):
        """Return the element of the last node"""
        if self.is_empty():
            pass
        return self._trailer._prev._element
    
    def first_enqueue(self, e):
        """Add element e after header"""
        newest = self._Node(e, self._header, self._header._next)
        self._header._next = newest
        newest._next._prev = newest

    def last_enqueue(self, e):
        """Add element e after trailer"""
        newest = self._Node(e, self._trailer, self._trailer._prev)
        self._trailer._prev = newest
        
     

