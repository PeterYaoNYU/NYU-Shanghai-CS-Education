from cmath import inf


def largest_ten(list1):
    """
    find the largest ten elements in list1. Assume list size greater than 10.
    required runtime: O(len(list1))

    :param list1: List -- list of integers
    
    :return: List -- largest ten elements in list list1, as a new size 10 list. (Order doesn't matter.)
    """
    res=[]
    for times in range(10):
        highest=list1[0]
        for i in list1:
            if i >highest:
                highest=i
        list1.remove(highest)
        res.append(highest)
    return res
    
    
    
def main():
    print(largest_ten([9,8,6,4,22,68,96,212,52,12,6,8,99]))
    b=sorted([9,8,6,4,22,68,96,212,52,12,6,8,99])
    b.reverse()
    print(b[:10])

    print(largest_ten([42,10,90,75,79,98,11,90,92,11,21,8,47,72,25,94,99,54,69,60]))
    a=[42,10,90,75,79,98,11,90,92,11,21,8,47,72,25,94,99,54,69,60]
    a=sorted(a)
    a.reverse()
    
    print(a[:10])

if __name__ == '__main__':
    main()