
def pascal(k):
    """
    :param k: Int -- Level k of pascal triangle

    :return: List[Int] -- a list of pascal values at level k
    """
    if k==0:
        return [1]
    last_ret=pascal(k-1)
    new=new_pascal(last_ret,0,[])
    new=[1]+new+[1]
    return new
    
def new_pascal(s, position, result=[]):
    if position==len(s)-1:
        return result
    result.append(s[position]+s[position+1])
    return new_pascal(s, position+1, result)

    


def main():
    print(pascal(4))    # [1, 3, 3, 1]
    print(pascal(0))    # [1]
    print(pascal(5))    # [1, 5, 10, 10, 5, 1]


if __name__ == '__main__':
    main()







