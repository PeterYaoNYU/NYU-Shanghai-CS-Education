class Node:
  def __init__(self, element, next = None):   # initialize node's fields
    self._element = element               # reference to user's element
    self._next = next                     # reference to next node

class Single_Linked_List:
  #------------------------------- Single Linked List methods -------------------------------
  def __init__(self):
    """Create an empty LinkedList."""
    self._head = None                       # reference to the head node
    self._size = 0                          # number of elements in the list

  def __len__(self):
    """Return the number of elements in the LinkedList."""
    return self._size

  def is_empty(self):
    """Return True if the LinkedList is empty."""
    return self._size == 0

  def insertAtFirst(self, e):
    """Add element e to the start of the LinkedList."""
    # TODO
    self._size+=1
    new_head=Node(e)
    new_head._next=self._head
    self._head=new_head
    
    
  def deleteFirst(self):
    """Remove and return the first element from the LinkedList.
    Raise Empty exception if the Linked list is empty.
    Return: the value of the first node
    """
    if self.is_empty():
      raise Exception('LinkedList is empty')
    # TODO
    temp=self._head
    self._head=self._head._next
    self._size-=1
    return temp._element


  def unOrderedSearch(self, target):
    # Search for the target element in the Linked List
    # Return: True if found else False
    currNode = self._head
    while currNode is not None and currNode._element != target:
      # traverse to the next node
      currNode = currNode._next
    return currNode is not None

  def __str__(self):
    # Return the string of contents of the Linked List
    result = ""
    currNode = self._head
    while currNode is not None:
      result += str(currNode._element) + " "
      currNode = currNode._next
    return result[:-1]

if __name__ == "__main__":
  linkedlist1 = Single_Linked_List()
  linkedlist1.insertAtFirst(5)
  linkedlist1.insertAtFirst(10)
  linkedlist1.insertAtFirst(22)
  linkedlist1.insertAtFirst(35)

  print(linkedlist1)                       # Expect: 35 22 10 5
  print(linkedlist1.deleteFirst())         # Expect: 35
  print(linkedlist1.deleteFirst())         # Expect: 22
  print(linkedlist1)                       # Expect: 10 5
  print(linkedlist1.unOrderedSearch(20))   # Expect: False
  print(linkedlist1)                       # Expect: 10 5
