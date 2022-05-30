def merge(I1, I2):  
    """
    takes two iterable objects and merges them alternately
    required runtime: O(len(I1) + len(I2)).

    :param I1: Iterable -- the first iterable object. Can be a string, tuple, etc
    :param I2: Iterable -- the second iterable object. Can be a string, tuple, etc

    :return: List -- alternately merged I1, I2 elements in a list.
    """
    i1=iter(I1)
    i2=iter(I2)
    l=max(len(I1),len(I2))
    res=[]
    for i in range(l):
        try:
            res.append(next(i1))
        except:
            pass
        try:
            res.append(next(i2))
        except:
            pass
    return res
        
    
    
    
def main():
    print([i for i in merge("what",range(100,105))])
    print([i for i in merge(range(5),range(100,101))])
    print([i for i in merge(range(1),range(100,105))])

if __name__ == '__main__':
    main()