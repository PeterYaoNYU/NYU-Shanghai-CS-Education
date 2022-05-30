'''
Note:
To get autograded on gradescope, you program can't print anything.
'''

# from re import I


# from sklearn.svm import l1_min_c


def merge_generator(I1, I2, I3):
    """
    takes three iterable objects and merges them alternately
    required runtime: O(len(I1) + len(I2) + len(I3)).
    required space complexity: O(1)

    :param I1: Iterable -- the first iterable object.
    :param I2: Iterable -- the second iterable object.
    :param I3: Iterable -- the third iterable object.

    :return: an iterator
    """      
    # count=0
    # while count<(len(I1)):
    #     yield I1[count]
    #     yield I2[count]
    #     yield I3[count]
    #     count+=1
    count=0
    i1=iter(I1)
    i2=iter(I2)
    i3=iter(I3)
    m=max(len(I1),len(I2),len(I3))
    while count<m:
        try:
            yield next(i1)
        except:
            pass
        try:
            yield next(i2)
        except:
            pass
        try:
            yield next(i3)
        except:
            pass
        count+=1
        
    
        
    
    



def main():
    for i in merge_generator(range(3), range(95,98), range(-3,0) ):
        print(i, end=", ")
        # Expect: print 0, 95, -3, 1, 96, -2, 2, 97, -1 in the order

    print()
    L = [ i for i in merge_generator( range(1), range(95,98) , range(-2,0) )]
    print(L)  # Expect: [0, 95, -2, 96, -1, 97]

    all = merge_generator( range(4), range(95,96), range(-2,0) )
    print(next(all))  # Expect: 0
    print(next(all))  # Expect: 95
    print(next(all))  # Expect: -2
    print(next(all))  # Expect: 1
    print(next(all))  # Expect: -1
    print(next(all))  # Expect: 2
    print(next(all))  # Expect: 3
    print(next(all))  # Expect: StopIteration Error

if __name__ == '__main__':
    main()