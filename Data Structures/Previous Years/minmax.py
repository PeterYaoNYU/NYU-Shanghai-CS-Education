from tempfile import TemporaryFile


def minmax(list1):
    """
    find both the minimum and maximum within list1.
    # You can assume list1 size is even.
    required number of comparisons: 3n/2  (This is not big O, you should limit your "<", ">" comparisons)

	:param list1: List -- list of integers
    :return: a tuple of two integers. The first integer is the minimum, the second integer is the maximum.
    """
    
    n=len(list1)
    small=[]
    big=[]
    for i in range(0,n,2):
        if list1[i]<list1[i+1]:
            small.append(list1[i])
            big.append(list1[i+1])
        else:
            small.append(list1[i+1])
            big.append(list1[i])
    min=find_smallest(small)
    max=find_biggest(big)
    
    return (min, max)
    
def find_smallest(small):
    if len(small)==1:
        return small[0]
    even_smaller=[]
    while small:
        temp1=small.pop()
        try:
            temp2=small.pop()
            if temp1<temp2:
                even_smaller.append(temp1)
            else:
                even_smaller.append(temp2)
        except:
            even_smaller.append(temp1)
    return find_smallest(even_smaller)

def find_biggest(big):
    if len(big)==1:
        return big[0]
    even_bigger=[]
    while big:
        temp1=big.pop()
        try:
            temp2=big.pop()
            if temp1>temp2:
                even_bigger.append(temp1)
            else:
                even_bigger.append(temp2)
        except:
            even_bigger.append(temp1)
    return find_biggest(even_bigger)
            
        
        

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(minmax([150, 24, 79, 50, 98, 88, 345, 3]))    # (3, 345)
    print(minmax([678, 227, 764, 37, 956, 982, 118, 212, 177, 597, 519, 968, 866, 121, 771, 343, 561, 100]))  # (37, 982)

if __name__ == '__main__':
    main()