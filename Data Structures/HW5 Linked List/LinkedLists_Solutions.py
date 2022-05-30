'Homework Assignment 5 Linked Lists'
__date__ = 'Apr 1 2022'
__note__ = 'Your answer should start from line 50'


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
        if k < 0:
            k += self._size
        if not -1 < k < self._size:
            raise IndexError("Either empty list, or poor index")
        target = self._head
        for i in range(k):
            target = target._next
        return target._element

    # Question 2: Reverse a Singly Linked List
    def list_reverse(self):
        # TODO:
        if (self._head is None):
            return self
        else:
            prev, curr = None, self._head
            while curr:
                next = curr._next
                curr._next = prev
                prev, curr = curr, next
            self._head = prev
            return self

    # Question 3: Search node pairs
    def search_node_pair(self, target, walk = None):
        # TODO:
        if not walk:
            walk = self._head
            if not walk:
                raise Empty("SLL is empty")
            if walk._element == target:
                return None, walk  # before node, actual node
        if not walk._next:
            return None, None
        if walk._next._element == target:
            return walk, walk._next
        return self.search_node_pair(target, walk._next)

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

    def del_and_reconnect(self, before):
        target = before._next
        before._next = target._next
        self._data._size -= 1
        return target._element

    def access(self,e):
        if self.is_empty():
            self._data.insert_from_head([e,1])
            return self
        walk = self._data._head
        if walk._element[0] == e:
            walk._element[1] += 1
            return self
        while walk._next:
            if walk._next._element[0] == e:
                walk._next._element[1] += 1
                return self._data.insert_from_head(self.del_and_reconnect(walk))
            walk = walk._next
        new_node = self._data._Node([e,1], None)
        walk._next = new_node
        self._data._size += 1
        return

    # Question 5: top-k favorite items
    def topk(self,k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        premax = None
        for j in range(k):
            curmax = self._data._head
            if premax != None:
                while curmax._element[1] > premax[1] or curmax._element == premax:
                    curmax = curmax._next
            walk = curmax._next
            while walk:
                if walk._element[1] >= curmax._element[1]:
                    if not premax or (walk._element[1] <= premax[1] and not walk._element == premax):
                        curmax = walk
                walk = walk._next
            yield curmax._element
            premax = curmax._element

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
        target, base, succ = self.get_last(), self.get_first(),self.get_first()._next
        for _ in range(len(self)//2-1):
            next_target = target._prev
            self.remove_and_insert(target, base, succ)
            target, base, succ = next_target, succ, succ._next
        return self

    def remove_and_insert(self, target, pred, succ):
        target._prev._next = target._next
        target._next._prev = target._prev
        # print(self)
        target._prev, target._next = pred, succ
        pred._next = target
        succ._prev = target
        # print(self)
        return self


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

    print("----------------Testing list_reverse------------------")
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
    for i in range(10):
        d.access('www.fuck.com')
    print(d)
    d.access("www.new")
    print(d)
    for each in d.topk(3):
        print(each)

    print("----------------Testing shuffle------------------")
    new_lissy = DoublyLinkedList()
    for i in range(1, 5):
        new_lissy.add_first(i)
        new_lissy.add_last(-i)
    print(new_lissy)
    new_lissy.shuffle()
    print(new_lissy, "Expect: head=4=-4=3=-3=2=-2=1=-1=tail")


if __name__ == '__main__':
    main()