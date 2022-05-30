'''
Note:
To get autograded on gradescope, you program can't print anything.
'''

# from ctypes import pointer
# from matplotlib.pyplot import pink


def find_sum_m(A,B,m):
    """
    :param A: List -- list of n integers
    :param B: List -- list of n integers
    required runtime: O(n) in the worst case
    required space complexity: O(1)

    :return: a list of all pairs of (a,b)
    """
    n=len(B)
    res=[]
    a_pointer=0
    b_pointer=n-1
    while a_pointer<n:
        try:
            if A[a_pointer]==A[a_pointer-1]:
                a_pointer+=1
                continue
        except:
            pass
        while b_pointer>=0 and A[a_pointer]+B[b_pointer]>m:
            b_pointer-=1
        if A[a_pointer]+B[b_pointer]==m:
            res.append(tuple([A[a_pointer],B[b_pointer]]))
        # elif A[a_pointer]+B[b_pointer]<m:
        #     if b_pointer<n-1:
        #         b_pointer+=1
        a_pointer+=1
    return res
        
        
        
        

def main():
    A = [-1, 4, 5, 6, 8, 10, 12]
    B = [0, 1, 2, 4, 9, 10, 20]
    print(find_sum_m(A, B, 14))  # Expect: [(4, 10), (5, 9), (10, 4), (12, 2)]

    A = [-1, 4, 5, 6, 8]
    B = [0, 1, 2, 4, 10]
    print(find_sum_m (A, B, 100))  # Expect: []

    A = [1, 2, 2, 3, 5]
    B = [1, 98, 98, 99, 99]
    print(find_sum_m(A, B, 100))  # Expect: [(1, 99), (2, 98)]


if __name__ == '__main__':
    main()