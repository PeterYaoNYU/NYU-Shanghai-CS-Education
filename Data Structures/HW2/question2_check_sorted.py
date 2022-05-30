'''
Note:
To get autograded on gradescope, you program can't print anything.
'''

# from sqlalchemy import false


# from sqlalchemy import falsex


def is_sorted(T, S):
    """
    tests if T is a sorting of S. No sorting function is allowed
    required runtime: O(nlogn) in the worst case

    :param T: List -- list of integers
    :param S: List -- list of integers, the original list
    
    :return: True/False
    """
    # a new idea: use binary search to generate a sorted list
    def binarySearch(key, t):
        n=len(t)
        if n==1:
            return t[0]==key
        elif n==0:
            return False
        mid=t[n//2]
        if mid==key:
            return True
        elif mid<key:
            return binarySearch(key,t[n//2+1:])
        else:
            return binarySearch(key, t[:n//2])
        
    def reverse_binary_search(key, t):
        n=len(t)
        if n==1:
            return t[0]==key
        elif n==0:
            return False
        mid=t[n//2]
        if mid ==key:
            return True
        elif mid<key:
            return reverse_binary_search(key, t[:n//2])
        else:
            return reverse_binary_search(key, t[n//2+1:])
        
    try:    
        if T[0]<T[1]:
            for i in S:
                if not binarySearch(i, T):
                    return False
            return True
        else:
            for i in S:
                if not reverse_binary_search(i, T):
                    return False
            return True
    except IndexError:
        return True

    
        
        

def main():
    print(is_sorted([1, 2, 3, 4, 5], [2, 4, 3, 1, 5]))  # Expected: True
    print((is_sorted([1, 2, 3, 5, 9], [2, 4, 3, 1, 5])))  # Expected: False
    print(is_sorted([1, 2, 3, 5, 4], [2, 4, 3, 1, 5]))  # Expect: False
    print(is_sorted([5, 4, 3, 2, 1], [2, 4, 3, 1, 5]))  # Expect: True

if __name__ == '__main__':
    main()
    
