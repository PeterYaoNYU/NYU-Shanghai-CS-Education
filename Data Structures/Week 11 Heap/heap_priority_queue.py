from queue import Empty

class PriorityQueueBase:
  """Abstract base class for a priority queue."""
  """You should not modify this class."""

  #------------------------------ nested _Item class ------------------------------
  class _Item:
    """Lightweight composite to store priority queue items."""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __lt__(self, other):
      return self._key < other._key    # compare items based on their keys

    def __repr__(self):
      return '({0},{1})'.format(self._key, self._value)

  #------------------------------ public behaviors ------------------------------
  def is_empty(self):                  # concrete method assuming abstract len
    """Return True if the priority queue is empty."""
    return len(self) == 0

  def __len__(self):
    """Return the number of items in the priority queue."""
    raise NotImplementedError('must be implemented by subclass')

class HeapPriorityQueue(PriorityQueueBase): # base class defines _Item
  """A min-oriented array-based priority queue implemented with a binary heap."""
  """There are TODO in this class for your work"""

  def __init__(self):
    """Create a new empty Priority Queue."""
    self._data = []

  def __len__(self):
    """Return the number of items in the priority queue."""
    return len(self._data)

  #------------------------------ nonpublic behaviors ------------------------------
  def _parent(self, j):
    # TODO: return the parent index
    # 1-2 line of code
    return (j-1)//2

  def _left(self, j):
    # TODO: return the left child index
    # 1-2 line of code
    return 2*j+1
  
  def _right(self, j):
    # TODO: return the right child index
    # 1-2 line of code
    return 2*j+2

  def _has_left(self, j):
    # TODO: check if node j has a left child. Return boolean value
    # 1-2 line of code
    return 2*j+1<len(self)
  
  def _has_right(self, j):
    # TODO: check if node j has a right child. Return boolean value
    # 1-2 line of code
    return 2*j+2<len(self)
    
  
  def _swap(self, i, j):
    """Swap the elements at indices i and j of array."""
    # 1-2 line of code
    self._data[i], self._data[j]=self._data[j],self._data[i]

  def _upheap(self, j):
    parent = self._parent(j)
    # TODO: Use recursion. ~ 3 lines of code
    # Think about when the recursion will terminate. And how to perform recursion:
    # If j is already root, then exit recursion. So what is the root index?
    # If heap-order property is not maintained bwteen j and parent(j), need to swap self._data[parent(j)] and self._data[j]
    if j==0:
      return
    if self._data[parent]<self._data[j]:
      return
    self._swap(parent, j)
    self._upheap(parent)
    
  
  def _downheap(self, j):
    if self._has_left(j):
      left = self._left(j)
      small_child = left               # although right may be smaller
      if self._has_right(j):
        right = self._right(j)
        if self._data[right] < self._data[left]:
          small_child = right
      if self._data[small_child] < self._data[j]:
        self._swap(j, small_child)
        self._downheap(small_child)    # recur at position of small child

  #------------------------------ public behaviors ------------------------------
  def add(self, key, value):
    """Add a key-value pair to the priority queue."""
    self._data.append(self._Item(key, value))
    self._upheap(len(self._data) - 1)            # upheap newly added position
  
  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    item = self._data[0]
    return (item._key, item._value)

  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    self._swap(0, len(self._data) - 1)           # put minimum item at the end
    item = self._data.pop()                      # and remove it from the list;
    self._downheap(0)                            # then fix new root
    return (item._key, item._value)

if __name__ == '__main__':
    heap = HeapPriorityQueue()
    for i in range(10, -1, -1):
        key = i
        value = i
        heap.add(key, value)
    print(heap._data)

    for i in range(10):
        print("Removing from heap:", heap.remove_min()[0])
