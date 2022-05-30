class SimpleTree:
    def __init__(self, element, left=None, right=None, parent=None):
        self._element = element
        self._left = left
        self._right = right
        self._parent = parent

    def __str__(self):
        return str(self._element)


#Problem4
"""Displays a simple tree in preorder. Can’t use recursion."""
def return_pre_order(root):
    # TODO
    stack = []
    output = []
    walk=root
    while stack or walk:
        while walk:
            output.append(walk._element)
            stack.append(walk)
            walk=walk._left
        walk=stack.pop()._right
    return output
        
        
    return output
            
if __name__ == '__main__':
    #test case
    tree = SimpleTree(1)
    tree._left = SimpleTree(2)
    tree._right = SimpleTree(3)
    tree._left._left = SimpleTree(4)
    tree._left._right = SimpleTree(5)
    tree._right._right = SimpleTree(8)
    tree._right._right._left = SimpleTree(6)
    tree._right._right._right = SimpleTree(7)
    
    print(return_pre_order(tree)) #Expect: [1, 2, 4, 5, 3, 8, 6, 7]
