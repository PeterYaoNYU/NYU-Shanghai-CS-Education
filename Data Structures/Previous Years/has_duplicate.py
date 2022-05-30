def has_duplicate(list1):
    """
    remember to mention your runtime as comment!

    :param l: List -- list of integers
    :return: True if list1 has duplicate, return False otherwise.
    """
    n=len(list1)
    for i in range(n):
        if list1[i] in list1[i+1:]:
            return True
    return False
# the runtime complexity is o(n**2)




# liqiaowei's solution use a hashmap to reduce the runtime complexity
# def has_duplicate(list1):
#     """
#     remember to mention your runtime as comment!

#     :param l: List -- list of integers
#     :return: True if list1 has duplicate, return False otherwise.
#     """
#     check={}
#     for i in list1:
#         if i in check:
#             return True
#         else:
#             check[i]=False
#     return False

# #runtime complexity: O(len(list1))
    
'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(has_duplicate([0,6,2,4,9]))   # False

    print(has_duplicate([0,6,2,4,9,1,2]))   # True

if __name__ == '__main__':
    main()