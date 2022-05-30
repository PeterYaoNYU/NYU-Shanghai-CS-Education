'Homework Assignment 5 Linked Lists'
__date__ = 'Apr 1 2022'
__note__ = 'Your answers should start from line 50'


class Empty(Exception):
    pass


# Question 1 SinglyLinkedList
class SinglyLinkedList:
    """ A singly linked list with single end"""
    class _Node:
        def __init__(self, element, next=None):
            self._element = element
            self._next = next  # should be linked to a Node

    def __init__(self):
        """Create an empty LinkedList."""
        self._head = None  # reference to the head node
        self._size = 0  # number of elements in the list

    def __len__(self):
        """Return the number of elements in the LinkedList."""
        return self._size

    def is_empty(self):
        """Return True if the LinkedList is empty."""
        return self._size == 0

    def insert_from_head(self,e):
        new_node = self._Node(e,self._head)
        if self.is_empty():
            self._tail = new_node
        self._head = new_node
        self._size += 1
        return new_node

    def delete_from_head(self):
        if self.is_empty():
            raise Empty('Singly Linked List is empty')
        answer = self.get_head()._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    # Question 1 __getitem__()
    def __getitem__(self, k):
        # TODO:
        count=0
        cur=self._head
        while count<k:
            cur=cur._next
            count+=1
        return cur._element
    
        

    # Question 2: Reverse a Singly Linked List
    def list_reverse(self):
        # TODO:
        prev=self._head
        cur=self._head._next
        future=cur._next
        while cur:
            cur._next=prev
            prev=cur
            cur=future
            if future and future._next:
                future=future._next
            else:
                future=None
        self._head._next=None
        self._head=prev
        
        

    # Question 3: Search node pairs
    def search_node_pair(self, target):
        # TODO:
        # return None, None
        if self._head._element==target:
            return None, self._head
        def helper(target, prev, cur):
            if not cur:
                return None, None
            if cur._element==target:
                return prev, cur
            return helper(target, prev._next, cur._next)
        return helper(target, self._head, self._head._next)

    def __str__(self):
        ret = []
        next_node = self._head
        while next_node:
            ret.append(str(next_node._element))
            next_node = next_node._next
        return str(ret)


# Question 4: favorite items
class FavSinglyLinkedList:
    def __init__(self):
        self._data = SinglyLinkedList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self,e):
        # TODO:
        cur=self._data._head
        if not cur:
            self._data._head=self._data._Node([e,1],None)
            self._data._size+=1
            return
        if cur._element[0]==e:
            cur._element[1]+=1
            return 
        if self._data._size>1:
            prev=cur
            cur=cur._next
            while cur:
                if cur._element[0]==e:
                    prev._next=cur._next
                    cur._next=self._data._head
                    self._data._head=cur
                    cur._element[1]+=1
                    return 
                else:
                    cur=cur._next
                    prev=prev._next  
            if not cur:
                prev._next=self._data._Node([e,1], None)  
                self._data._size+=1
                     
        else:
            self._data._head._next=self._data._Node([e,1], None)
            self._data._size+=1
            
                

    # Question 5: top-k favorite items
    def topk(self,k):
        # TODO
        # we have to bear in mind the possibility of having numerous websites that have the 
        # same amount of visits 
        visited=[]
        last_max=float("inf")
        temp=-float("inf")
        to_be_ret=None
        for _ in range (k):
            cur=self._data._head
            while cur:
                if cur._element[1]==last_max and (cur not in visited):
                    # visited.append(cur)
                    to_be_ret=cur
                    temp=last_max
                    # yield cur._element
                    # break
                    break
                elif cur._element[1]>temp and cur._element[1]<last_max:
                    temp=cur._element[1]
                    to_be_ret=cur
                cur=cur._next
            yield to_be_ret._element
            last_max=to_be_ret._element[1]
            visited.append(to_be_ret)
            temp=-float("inf")                    
            
        

    def __str__(self):
        return str(self._data)


# Question 6: Shuffle
class DoublyLinkedList:
    class _Node:
        __slots__ = '_element', '_prev','_next'

        def __init__(self, element, prev, next):
            self._element=element
            self._prev = prev
            self._next = next  # should be linked to a Node

        def get_succ(self):
            return self._next

        def get_pred(self):
            return self._prev

        def get_value(self):
            return self._element

    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, self._head, None) # these two are not equal
        self._head._next = self._tail
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def get_first(self):
        return self._head._next

    def get_last(self):
        return self._tail._prev

    def add_first(self, e):
        new_node = self._Node(e, self._head, self.get_first())
        self.get_first()._prev = new_node
        self._head._next = new_node
        self._size += 1
        return new_node

    def add_last(self, e):
        new_node = self._Node(e, self.get_last(), self._tail)
        self.get_last()._next = new_node
        self._tail._prev = new_node
        self._size += 1
        return new_node

    def __str__(self):
        ret = ["head="]
        next_node = self.get_first()
        while next_node._next:
            ret.append(str(next_node._element)+"=")
            next_node = next_node._next
        ret.append("tail")
        return ''.join(ret)

    # Question 6: Shuffle
    def shuffle(self):
        # TODO
        half=self._size/2
        # print(half)
        cur=self._head
        for i in range(int(half)):
            cur=cur._next
        mid=cur
        cur=self._head._next
        future=cur._next
        while cur!=mid:
            inserting=self._tail._prev
            self._tail._prev=inserting._prev
            inserting._prev._next=self._tail
            inserting._prev=cur
            inserting._next=future

            cur._next=inserting
            future._prev=inserting
            cur=future
            future=cur._next
        return self
        # cur._next._prev=self._Node(None, None, cur._next)
        # newhead=cur._next._prev
        # newtail=self._Node(None, cur, None)
        # cur._next=newtail
        
            


def main():
    print("----------------Testing __getitem__------------------")
    l1 = SinglyLinkedList()
    l1.insert_from_head('good')
    l1.insert_from_head('nice')
    l1.insert_from_head('haha')
    l1.insert_from_head('hi')

    print(l1)
    print("index 0 of l1:", l1[0])
    print("index 1 of l1:", l1[1])
    print("index 2 of l1:", l1[2])
    print("index 3 of l1:", l1[3])

    print("----------------Testing list reverse------------------")
    l1 = SinglyLinkedList()
    for i in range(10):
        l1.insert_from_head(i)
    print(l1)  # 9-->8-->7-->6-->5-->4-->3-->2-->1-->0-->None
    l1.list_reverse()
    print(l1, "Expected: 0-->1-->2-->3-->4-->5-->6-->7-->8-->9-->None")

    print("----------------Testing search node pairs------------------")
    l1 = SinglyLinkedList()
    for i in range(10):
        l1.insert_from_head(i)
    print(l1)  # 9-->8-->7-->6-->5-->4-->3-->2-->1-->0-->None
    a, b = l1.search_node_pair(1)
    print(a._element, b._element, "Expect: 2,1")
    a, b = l1.search_node_pair(9)
    print(a, b._element, "Expect: None,9")
    a, b = l1.search_node_pair(10)
    print(a, b, "Expect: None,None")

    print("----------------Testing FavSinglyLinkedList------------------")
    d = FavSinglyLinkedList()
    for i in range(10):
        d.access('www.a')
        if i % 2 == 0:
            d.access('www.b')
        if i % 3 == 0:
            d.access('www.c')
        if i % 5 == 0:
            d.access('www.d')
    # for i in range(10):
    #     d.access('www.shanghai sb')
    #     d.access('feangndjab')
    print(d)    # Expect ["['www.c', 4]", "['www.a', 10]", "['www.b', 5]", "['www.d', 2]"]
    for each in d.topk(3):
        print(each)
        # Expect ['www.a', 10]
        #             ['www.b', 5]
        #             ['www.c', 4]
        #  in this order

    print("----------------Testing shuffle------------------")
    new_lissy = DoublyLinkedList()
    for i in range(1, 5):
        new_lissy.add_first(i)
        new_lissy.add_last(-i)
    new_lissy.shuffle()
    print(new_lissy, "Expect: head=4=-4=3=-3=2=-2=1=-1=tail")


if __name__ == '__main__':
    main()