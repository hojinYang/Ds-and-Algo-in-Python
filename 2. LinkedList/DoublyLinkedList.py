class _DoublyLinkedList:
    """A base class providing a doubly linked list representation."""
    #--------------Nested Node class---------------------------
    class _Node:
        """Lightweight, non-public class for storing a doubly linked node."""
        __slot__ = '_element', '_prev', '_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    #--------------Doubly linked list implementation------------

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of nodes"""
        return self._size
    
    def is_empty(self):
        """return True if the number of nodes is zero"""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two exisitng node and return new node"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Delete nonsentimental node from the list and return its element"""
        predecessor = node._prev
        successor = node._next

        predecessor._next , successor._prev = successor, predecessor
        self._size -= 1
        ret = node._element
        node._element = node._prev = node._next = None

        return ret
    





