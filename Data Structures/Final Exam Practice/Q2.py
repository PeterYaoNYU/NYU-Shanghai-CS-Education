class DoubleLinkedList:
    """A base class providing a doubly linked list representation."""

#-------------------------- nested _Node class --------------------------
# nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next' # streamline memory

        def __init__(self, element, prev, next): # initialize node's fields
            self._element = element # user's element
            self._prev = prev # previous node reference
            self._next = next # next node reference

#-------------------------- list constructor --------------------------

    def __init__(self):
        """Create an empty list."""
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0 # number of elements

#-------------------------- public accessors --------------------------

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def add_first(self, e):
        """Add an element to the front of list."""
        self._insert_between(e, self._head, self._head._next)
    
    def __str__(self):
        result = ['head <--> ']
        curNode = self._head._next
        while (curNode._next is not None):
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("tail")
        return "".join(result)
    
    #Problem2
    def switch_first(self, l2):
        """Switch first node of self, with first node of l2."""
        temp1=self._head._next
        temp2=l2._head._next
        self._head._next=self._head._next._next
        self._head._next._prev=self._head
        temp1._prev=temp1._next=None
        
        l2._head._next=l2._head._next._next
        l2._head._next._prev=l2._head
        temp2._next=temp2._prev=None
        
        old_next=self._head._next
        old_next._prev=temp2
        temp2._next=old_next
        self._head._next=temp2
        temp2._prev=self._head
        
        old_next=l2._head._next
        old_next._prev=temp1
        temp1._next=old_next
        l2._head._next=temp1
        temp1._prev=l2._head
        


#test case
def main():
    l1 = DoubleLinkedList()
    for i in range(8):
        l1.add_first(i)
    print(l1) #head <--> 7 <--> 6 <--> 5 <--> 4 <--> 3 <--> 2 <--> 1 <--> 0 <--> tail
    l2 = DoubleLinkedList() 
    for i in range(8):
        l2.add_first(7-i)
    print(l2) #head <--> 0 <--> 1 <--> 2 <--> 3 <--> 4 <--> 5 <--> 6 <--> 7 <--> tail
    l1.switch_first(l2)
    print(l1) #head <--> 0 <--> 6 <--> 5 <--> 4 <--> 3 <--> 2 <--> 1 <--> 0 <--> tail
    print(l2) #head <--> 7 <--> 1 <--> 2 <--> 3 <--> 4 <--> 5 <--> 6 <--> 7 <--> tail

if __name__ == '__main__':
    main()

