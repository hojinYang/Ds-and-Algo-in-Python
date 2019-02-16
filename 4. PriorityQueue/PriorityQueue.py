class PriorityQueueBase:
    class _item:
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value
        
        def __lt__(self, other):
            return self._key < other._key
        
    def is_empty(self):
        return len(self) == 0


class HeapPriorityQueue(PriorityQueueBase):
    #------------non-public behavior---------------
    def _parent(self, j):
        return j-1 // 2
    def _left(self, j):
        return 2*j + 1
    def _right(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left < len(self._data)
    def _has_right(self, j):
        return self._right < len(self._data)
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _upheap(self, j):
        parent = self._data[j]
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            min_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    min_child = right
            if self._data[min_child] < self._data[j]:
                self._swap(j, min_child)
                self._downheap(min_child)

    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        newest = self._item(key, value)
        self._data.insert(newest)
        self._upheap(len(self._data) - 1)
    
    def min(self):
        if self.is_empty():
            raise ValueError("Empty")
        
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty():
            raise ValueError("Empty")
        
        self._swap(0, len(self._data) -1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
    
    



    


