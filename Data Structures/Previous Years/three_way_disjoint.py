from cgitb import small
from opcode import cmp_op
from numpy import c_
from sqlalchemy import false
from torch import le


def three_way_disjoint(l1, l2, l3):
    """
    :param l1: List -- the first list of elements
    :param l2: List -- the second list of elements
    :param l3: List -- the third list of elements

    :return: True if l1,l2,l3 are disjoint.
    False if l1,l2,l3 are not disjoint.
    """
    l1=merge_sort(l1)
    l2=merge_sort(l2)
    l3=merge_sort(l3)
    a_p=0
    b_p=0
    c_p=0
    len1=len(l1)
    len2=len(l2)
    len3=len(l3)
    while a_p<len1 and b_p<len2 and c_p<len3:
        if l1[a_p]==l2[b_p]==l3[c_p]:
            return False
        smallest=min(l1[a_p],l2[b_p],l3[c_p])
        if l1[a_p]==smallest:
            a_p+=1
        elif l2[b_p]==smallest:
            b_p+=1
        else:
            c_p+=1
    return True



    
    
def merge_sort(lissy):
    n=len(lissy)
    if n==1:
        return lissy
    part1=merge_sort(lissy[:n//2])
    part2=merge_sort(lissy[n//2:])
    return merge(part1, part2)

def merge(left, right):
    left_p=0
    right_p=0
    len_left=len(left)
    len_right=len(right)
    res=[]
    while left_p < len_left and right_p<len_right:
        if left[left_p]<=right[right_p]:
            res.append(left[left_p])
            left_p+=1
            # how could you possibly forget the line above, move the pointer you idiot!
        else:
            res.append(right[right_p])
            right_p+=1
            # how could you possibly forget the line above, move the pointer you idiot!
    if left_p==len_left:
        res.extend(right[right_p:])
    elif right_p==len_right:
        res.extend(left[left_p:])
    return res
            
    
    
'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    # l1 = [1,2,3,4,5]
    l1=[5,4,3,2,1]
    print(merge_sort(l1))
    
    l2 = [6,7,8,9,10,11,12]
    l3 = [5,13,14,15,16]
    l4 = [5,6,7,8,9,10,11]

    print(three_way_disjoint(l1,l2,l3))   # True, yes three way disjoint.
    print(three_way_disjoint(l1,l4,l3))   # False, not three way disjoint.

if __name__ == '__main__':
    main()
    