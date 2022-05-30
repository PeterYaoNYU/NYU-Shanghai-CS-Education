"""
Assignment 1 question 1 Block-wise Palindromes

note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
"""
import copy


def block_palindrome(n):
    """
    :param n: a positive integer
    :return: True if n is a block-wise palindrome in blocks size of 2
             False otherwise.
    """
    # To do
    # s=[]
    original=n
    new=0
    while n!=0:
        rema=n & 3
        n=n>>2
        new=new<<2
        new=new|rema
    # print(new)
    # print(n)
    # print(original)
    return new==original
    # temp=copy.deepcopy(s)
    # temp.reverse()
    # return temp==s
    # def get_four_repr(n):
        
            
    #     res=[]
    #     while n:
    #         m=n%4
    #         n=n//4
    #         res.insert(0,m)
    #     return res
    # four_repr=get_four_repr(n)
    # m=len(four_repr)
    # n=m//2
    # for i in range(n):
    #     if four_repr[i]^four_repr[m-i-1]!=0:
    #         return False
    # return True
        
    
        


def main():
    print(block_palindrome(215)) # Expect: True
    print(block_palindrome(38))  # Expect: True
    print(block_palindrome(153)) # Expect: False
    print(block_palindrome(105)) # Expect: True


# if __name__ == '__main__':
#     main()
