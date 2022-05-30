'Homework Assignment 6 Trees'
__date__ = 'Apr 9 2022'
__note__ = 'Your answers should start from line 260'



# from typing import List



class Tree:
    class TreeNode:
        def __init__(self, element, parent = None, left = None, right = None):
            self._parent = parent
            self._element = element
            self._left = left
            self._right = right

    #-------------------------- binary tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    #-------------------------- public accessors ---------------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def is_root(self, node):
        """Return True if a given node represents the root of the tree."""
        return self._root == node

    def is_leaf(self, node):
        """Return True if a given node does not have any children."""
        return self.num_children(node) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for node in self.nodes():                        # use same order as nodes()
            yield node._element                               # but yield each element

    def depth(self, node):
        """Return the number of levels separating a given node from the root."""
        if self.is_root(node):
            return 0
        else:
            return 1 + self.depth(self.parent(node))

    def _height1(self):                 # works, but O(n^2) worst-case time
        """Return the height of the tree."""
        return max(self.depth(node) for node in self.nodes() if self.is_leaf(node))

    def _height2(self, node):                  # time is linear in size of subtree
        """Return the height of the subtree rooted at the given node."""
        if self.is_leaf(node):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(node))

    def height(self, node=None):
        """Return the height of the subtree rooted at a given node.

        If node is None, return the height of the entire tree.
        """
        if node is None:
            node = self._root
        return self._height2(node)        # start _height2 recursion

    def nodes(self):
        """Generate an iteration of the tree's nodes."""
        return self.preorder()                            # return entire preorder iteration

    def preorder(self):
        """Generate a preorder iteration of nodes in the tree."""
        if not self.is_empty():
            for node in self._subtree_preorder(self._root):  # start recursion
                yield node

    def _subtree_preorder(self, node):
        """Generate a preorder iteration of nodes in subtree rooted at node."""
        yield node                                           # visit node before its subtrees
        for c in self.children(node):                        # for each child c
            for other in self._subtree_preorder(c):         # do preorder of c's subtree
                yield other                                   # yielding each to our caller

    def postorder(self):
        """Generate a postorder iteration of nodes in the tree."""
        if not self.is_empty():
            for node in self._subtree_postorder(self._root):  # start recursion
                yield node

    def _subtree_postorder(self, node):
        """Generate a postorder iteration of nodes in subtree rooted at node."""
        for c in self.children(node):                        # for each child c
            for other in self._subtree_postorder(c):        # do postorder of c's subtree
                yield other                                   # yielding each to our caller
        yield node                                           # visit node after its subtrees

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
          for node in self._subtree_inorder(self._root):
            yield node

    def _subtree_inorder(self, node):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if node._left is not None:          # if left child exists, traverse its subtree
          for other in self._subtree_inorder(node._left):
            yield other
        yield node                               # visit p between its subtrees
        if node._right is not None:         # if right child exists, traverse its subtree
          for other in self._subtree_inorder(node._right):
            yield other

    def breadthfirst(self):
        """Generate a breadth-first iteration of the nodes of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()             # known nodes not yet yielded
            fringe.enqueue(self._root)        # starting with the root
            while not fringe.is_empty():
                node = fringe.dequeue()             # remove from front of the queue
                yield node                          # report this node
                for c in self.children(node):
                    fringe.enqueue(c)              # add children to back of queue

    def root(self):
        """Return the root of the tree (or None if tree is empty)."""
        return self._root

    def parent(self, node):
        """Return node's parent (or None if node is the root)."""
        return node._parent

    def left(self, node):
        """Return node's left child (or None if no left child)."""
        return node._left

    def right(self, node):
        """Return node's right child (or None if no right child)."""
        return node._right

    def children(self, node):
        """Generate an iteration of nodes representing node's children."""
        if node._left is not None:
            yield node._left
        if node._right is not None:
            yield node._right

    def num_children(self, node):
        """Return the number of children of a given node."""
        count = 0
        if node._left is not None:     # left child exists
            count += 1
        if node._right is not None:    # right child exists
            count += 1
        return count

    def sibling(self, node):
        """Return a node representing given node's sibling (or None if no sibling)."""
        parent = node._parent
        if parent is None:                    # p must be the root
            return None                         # root has no sibling
        else:
            if node == parent._left:
                return parent._right         # possibly None
            else:
                return parent._left         # possibly None

    #-------------------------- nonpublic mutators --------------------------
    def add_root(self, e):
        """Place element e at the root of an empty tree and return the root node.

        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self.TreeNode(e)
        return self._root

    def add_left(self, node, e):
        """Create a new left child for a given node, storing element e in the new node.

        Return the new node.
        Raise ValueError if node already has a left child.
        """
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self.TreeNode(e, node)             # node is its parent
        return node._left

    def add_right(self, node, e):
        """Create a new right child for a given node, storing element e in the new node.

        Return the new node.
        Raise ValueError if node already has a right child.
        """
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self.TreeNode(e, node)            # node is its parent
        return node._right

    def _replace(self, node, e):
        """Replace the element at given node with e, and return the old element."""
        old = node._element
        node._element = e
        return old

    def _delete(self, node):
        """Delete the given node, and replace it with its child, if any.

        Return the element that had been stored at the given node.
        Raise ValueError if node has two children.
        """
        if self.num_children(node) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent     # child's grandparent becomes parent
        if node is self._root:
            self._root = child             # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        return node._element

    def _attach(self, node, t1, t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external node.

        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if node already has a child. (This operation requires a leaf node!)
        """
        if not self.is_leaf(node):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():         # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None             # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():         # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None             # set t2 instance to empty
            t2._size = 0

    #---------------------------------- Problems ---------------------------------

    def has_duplicate(self):
        """
        :self: Tree -- a binary Tree.
        :return: True if self BinaryTree contains duplicate values. False otherwise
        """

        # Task 1
        def duplicate_one_traversal(node: Tree.TreeNode):
            for i in self.preorder():
                if i._element==node._element and id(i)!=id(node):
                    return True
            return False
        for i in self.preorder():
            if duplicate_one_traversal(i):
                return True
        return False         


# Task 2
def is_isomorphic(tree1:Tree, tree2: Tree):
    """
    :param tree1: Tree -- a binary tree
    :param tree2: Tree -- another binary tree

    :return: True if tree1 and tree2 are isomorphic. False otherwise.
    """
    def isomorphic_recur(node1:Tree.TreeNode, node2:Tree.TreeNode):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1._element!=node2._element:
            return False
        return (isomorphic_recur(node1._left, node2._right) and isomorphic_recur(node1._right, node2._left)) or \
            (isomorphic_recur(node1._left, node2._left) and isomorphic_recur(node1._right, node2._right))
    return isomorphic_recur(tree1._root, tree2._root)



# Task 3
def build_expression_tree(infix: str):
    """
    :param infix: String -- infix string contains spaces between each operand/operator.

    :return: a class Tree object. This tree should be the Expression Tree for the given infix string.
    """
    # TODO, modify the code below, this is just place holder code.
    infix_storage=infix.split()
    infix_storage.reverse()
    operand=[]
    operator=[]
    while infix_storage:
        temp=infix_storage.pop()
        if temp not in "+-*/":
            new=Tree()
            new._root=Tree.TreeNode(int(temp))
            new._size=1
            operand.append(new)
        else:
        # temp=infix_storage.pop()
            new_op=Tree()
            new_op._size=1
            new_op._root=Tree.TreeNode(temp)
            if temp=='*' or temp=='/':
                right_child=int(infix_storage.pop())
                new=Tree()
                new._root=Tree.TreeNode(right_child)
                new._size=1
                new_op._attach(new_op._root, operand.pop(), new)
                operand.append(new_op)
            else:
                operator.append(new_op)
    while operator:
        left_child=operand.pop(0)
        right_child=operand.pop(0)
        op=operator.pop(0)
        op._attach(op._root, left_child, right_child)
        operand.insert(0, op)
    return operand.pop()
        
        
            

            
        
        # operand.append(int(infix_storage.pop()))
        # temp=infix_storage.pop()
        # if temp=='*' or temp=='/':
        #     right_child=int(infix_storage.pop())
        #     new_tree=Tree()
        #     new_tree._root=temp
        #     new_tree._root._left=operand.pop()
        #     new_tree._root._rig
            
    return Tree()


# Tasl 4
def zero_one_update(one_zero_tree:Tree):
    """
    :param one_zero_tree: a class Tree object. This tree has been initialized such that
                          leaves have 0/1 and internal nodes have None
    Update the elements in all the nodes.
    :return: None or the one_zero_tree
    """
    def recur_zero_one(node:Tree.TreeNode):
        left_flag=False
        right_flag=False
        if not node:
            return 
        if node._element!=None:
            return
        if not node._left:
            left_flag=True
        elif node._left._element==None:
            recur_zero_one(node._left)
            
        if not node._right:
            right_flag=True
        elif node._right._element==None:
            recur_zero_one(node._right)
            
        if left_flag:
            node._element=node._right._element
            return
        if right_flag:
            node._element=node._left._element
            return
        if one_zero_tree.depth(node)%2==0:
            node._element=max(node._left._element, node._right._element)
            return
        else:
            node._element=min(node._left._element, node._right._element)
        return 
    recur_zero_one(one_zero_tree._root)
  


# For pretty printing
def pretty_print(tree):
    # ----------------------- Need to enter height to work -----------------
    levels = tree.height() + 1  
    print_internal([tree._root], 1, levels)

def print_internal(this_level_nodes, current_level, max_level):
    if (len(this_level_nodes) == 0 or all_elements_are_None(this_level_nodes)):
        return  # Base case of recursion: out of nodes, or only None left

    floor = max_level - current_level;
    endgeLines = 2 ** max(floor - 1, 0);
    firstSpaces = 2 ** floor - 1;
    betweenSpaces = 2 ** (floor + 1) - 1;
    print_spaces(firstSpaces)
    next_level_nodes = []
    for node in this_level_nodes:
        if (node is not None):
            print(node._element, end = "")
            next_level_nodes.append(node._left)
            next_level_nodes.append(node._right)
        else:
            next_level_nodes.append(None)
            next_level_nodes.append(None)
            print_spaces(1)

        print_spaces(betweenSpaces)
    print()
    for i in range(1, endgeLines + 1):
        for j in range(0, len(this_level_nodes)):
            print_spaces(firstSpaces - i)
            if (this_level_nodes[j] == None):
                    print_spaces(endgeLines + endgeLines + i + 1);
                    continue
            if (this_level_nodes[j]._left != None):
                    print("/", end = "")
            else:
                    print_spaces(1)
            print_spaces(i + i - 1)
            if (this_level_nodes[j]._right != None):
                    print("\\", end = "")
            else:
                    print_spaces(1)
            print_spaces(endgeLines + endgeLines - i)
        print()

    print_internal(next_level_nodes, current_level + 1, max_level)

def all_elements_are_None(list_of_nodes):
    for each in list_of_nodes:
        if each is not None:
            return False
    return True

def print_spaces(number):
    for i in range(number):
        print(" ", end = "")


def main():
    ###################### Generate sample tree 1 #######################
    print("T1")
    T1 = Tree()
    a = T1.add_root("A")
    b = T1.add_left(a,"B")
    c = T1.add_left(b,"C")
    d = T1.add_right(b,"D")
    T1.add_left(c,"E")
    T1.add_right(c,"F")
    T1.add_left(d,"G")
    x1 = T1.add_right(a,"1")
    T1.add_left(x1,"2")
    x3 = T1.add_right(x1,"3")
    T1.add_left(x3,"4")
    x5 = T1.add_right(x3,"5")
    x6 = T1.add_left(x5,"6")
    pretty_print(T1)    #If you want to visualize sample tree, uncomment this

    ###################### Generate sample tree 2 #######################
    print("T")
    T = Tree()
    eight = T.add_root(8)
    three = T.add_left(eight, 3)
    zero = T.add_right(eight,0)
    one = T.add_left(three,1)
    six = T.add_right(three,6)
    four = T.add_left(six,4)
    five = T.add_right(six,5)
    seven = T.add_right(zero,7)
    two = T.add_left(seven,2)
    nine = T.add_left(zero, 9)
    pretty_print(T)  #If you want to visualize this sample tree, uncomment this

    ###################### Generate sample tree 3 #######################
    print("tree1")
    tree1 = Tree()
    eight = tree1.add_root(8)
    one = tree1.add_left(eight, 1)
    four = tree1.add_right(eight, 4)
    three = tree1.add_left(one, 3)
    two = tree1.add_right(one, 2)
    seven = tree1.add_right(four, 7)
    five = tree1.add_right(two, 5)
    six = tree1.add_left(seven, 6)
    pretty_print(tree1)

    ###################### Generate sample tree 4 #######################
    print("tree2")
    tree2 = Tree()
    eight = tree2.add_root(8)
    one = tree2.add_left(eight, 1)
    four = tree2.add_right(eight, 4)
    three = tree2.add_left(one, 3)
    two = tree2.add_right(one, 2)
    seven = tree2.add_right(four, 7)
    three_2 = tree2.add_right(two, 3)
    six = tree2.add_left(seven, 6)
    pretty_print(tree2)

    ###################### Generate sample tree 5 #######################
    print("tree3")
    tree3 = Tree()
    eight = tree3.add_root(8)
    one = tree3.add_left(eight, 1)
    four = tree3.add_right(eight, 4)
    two = tree3.add_right(one, 2)
    seven = tree3.add_right(four, 7)
    three = tree3.add_left(two, 3)
    five = tree3.add_right(two, 5)
    six = tree3.add_left(seven, 6)
    pretty_print(tree3)

    ###################### Generate sample tree 6 #######################
    print("tree4")
    tree4 = Tree()
    eight = tree4.add_root(8)
    four = tree4.add_left(eight, 4)
    one = tree4.add_right(eight, 1)
    seven = tree4.add_left(four, 7)
    two = tree4.add_right(one, 2)
    three = tree4.add_left(two, 3)
    five = tree4.add_right(two, 5)
    six = tree4.add_right(seven, 6)
    pretty_print(tree4)

    ###################### Generate sample tree 7 #######################
    print("g")
    g = Tree()
    g_root = g.add_root(None)
    gl1 = g.add_left(g_root, None)
    gr1 = g.add_right(g_root, None)
    gr2 = g.add_right(gr1, 0)
    gl2 = g.add_left(gl1, None)
    glr = g.add_right(gl1, 1)
    gl3 = g.add_left(gl2, 0)
    gl2r= g.add_right(gl2, None)
    gl2rl = g.add_left(gl2r, 1)
    gl2r2 = g.add_right(gl2r, 0)
    pretty_print(g)

    ###################### Generate sample tree 8 #######################
    print("gg")
    gg = Tree()
    gg_root = gg.add_root(0)
    ggl1 = gg.add_left(gg_root, 0)
    ggr1 = gg.add_right(gg_root, 0)
    ggr2 = gg.add_right(ggr1, 0)
    ggl2 = gg.add_left(ggl1, 0)
    gglr = gg.add_right(ggl1, 1)
    ggl3 = gg.add_left(ggl2, 0)
    ggl2r = gg.add_right(ggl2, 0)
    ggl2rl = gg.add_left(ggl2r, 1)
    ggl2r2 = gg.add_right(ggl2r, 0)
    # pretty_print(gg)


    print("#-------------------------- Problem 1 has_duplicate tests... --------------------------")
    print(T1.has_duplicate(), "    Expected result is False")
    print(T.has_duplicate(), "    Expected result is False")
    print(tree1.has_duplicate(), "    Expected result is False")
    print(tree2.has_duplicate(), "    Expected result is True")


    print("#-------------------------- Problem 2 is_isomorphic tests... --------------------------")
    print(is_isomorphic(tree3, tree4), "     Expected result is True")
    print(is_isomorphic(tree1, tree4), "     Expected result is False")


    print("#-------------------------- Problem 3 build_expression_tree tests... --------------------------")
    exp1 = build_expression_tree("1 * 2 + 3 / 4")
    exp2 = build_expression_tree("7 + 6 - 3 * 5")
    print("exp tree 1 Expected:")
    print("   +    ")
    print("  / \   ")
    print(" /   \  ")
    print(" *   /  ")
    print("/ \ / \ ")
    print("1 2 3 4 ")
    print("exp tree 2 Expected:")
    print("   -    ")
    print("  / \   ")
    print(" /   \  ")
    print(" +   *  ")
    print("/ \ / \ ")
    print("7 6 3 5 ")

    print("Your exp tree 1:")
    pretty_print(exp1)

    print("Your exp tree 2:")
    pretty_print(exp2)

    print("#-------------------------- Problem 4 one zero trees... --------------------------")
    zero_one_update(g)
    pretty_print(g)
    print("updated tree g Expected:")
    pretty_print(gg)



if __name__ == '__main__':
    main()

