import copy
def throw_stones(N, M):
    """
    N: Number of stones (N>=1)
    M: Number of days (M>=1)
    """
    # TODO:
    results = helper(N,M,[],True,[])
    return results

def helper(target, days, path, flag, result=[]):
    if len(path)==days and sum(path)==target:
        result.append(path)
        return result
    elif len(path)==days:
        return result
    if sum(path)+1<=target:
        temp=path[:]
        temp.append(1)
        # print(temp)
        
        helper(target, days, temp, not flag, result)
    if sum(path)+3<=target:
        temp=path.copy()
        temp.append(3)
        # print(temp)
        
        helper(target, days, temp, not flag, result)
    if flag==True:
        if sum(path)+2<=target:
            temp=path.copy()
            temp.append(2)
            # print(temp)
            helper(target, days, temp, not flag, result)
    return result
    # if len(path)==days:
    #     return result
    # if sum(path)+1==target:
    #     temp=path[:]+[1]
    #     result.append(temp)
    # elif sum(path)+1<temp:
    #     temp=path[:]
    #     temp.append(1)
    #     helper(target, days, temp, flag, result)
    # if sum(path)+3==target:
    #     temp=path[:]+[1]
    #     result.append(temp)
    # elif sum(path)+3<temp:
    #     temp=path[:]
    #     temp.append(1)
    #     helper(target, days, temp, flag, result)
    
        
    
    


def main():
    print(throw_stones(N=5,
                       M=3))  # Expect: [(1, 1, 3), (1, 3, 1), (2, 1, 2), (3, 1, 1)] or [[1, 1, 3], [1, 3, 1], [2, 1, 2], [3, 1, 1]]
    print(throw_stones(N=6, M=2))  # Expect: [(3, 3)] or [[3, 3]]


if __name__ == '__main__':
    main()