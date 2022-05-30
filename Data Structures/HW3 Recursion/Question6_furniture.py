from cmath import cos


def purchase_combination(Y_cost, X, Z):
    """
    Y_cost: a list of costs of each appliance brand. e.g. Y_cost = [[1, 5], [2, 4, 3, 6]]. All costs are > 0
    The number of brands for appliance type 0 is 2, which corresponds to cost [1, 5] from Y_cost[0].
    The number of brands for appliance type 1 is 4, which corresponds to cost [2, 4, 3, 6] from Y_cost[1].
    X: Total money you have
    Z: Minimum spending, and Z < X
    Return: A list of tuples containing the index of each appliance selected.
    """
    # TODO
    result=helper(Y_cost, X, Z, 0,0,[],0,[])
    return result

def helper(cost, upper, lower, brand_pointer, type_pointer, path,spent,result=[]):
    # print(cost, upper, lower, brand_pointer, type_pointer, path,spent,result)
    if type_pointer==len(cost) and lower<=spent and spent<=upper:
        result.append(tuple(path))
        return
    if len(path)==len(cost):
        return
    if brand_pointer==len(cost[type_pointer]):
        return
    # print(type(spent))
    # helper(cost, upper, lower, brand_pointer+1, type_pointer, path, result, spent)
    if spent+cost[type_pointer][brand_pointer]<=upper:
        temp=path[:]
        temp.append(brand_pointer)
        # print(temp)
        temp2=spent
        temp2+=cost[type_pointer][brand_pointer]
        # print(temp2)
        helper(cost, upper, lower, 0, type_pointer+1, temp, temp2, result)
    helper(cost, upper, lower, brand_pointer+1, type_pointer, path, spent, result)
    return result
    
    
    # if brand_pointer==len(cost[type_pointer]):
    #     return
    # if brand_pointer<len(cost[type_pointer]):
    #     if spent+cost[type_pointer][brand_pointer]<upper:
    #         temp=path[:]
    #         temp.append(brand_pointer)
    #         spent=spent+cost[type_pointer][brand_pointer]
    #         helper(cost, upper, lower, 0, temp, type_pointer, result, spent)
            
        
        


def main():
    Y_cost = [[1,5], [2,4,3,6]]
    X = 12
    Z = 9
    print(purchase_combination(Y_cost, X, Z)) # Expect: results = [(1,1), (1,3)]


if __name__ == "__main__":
    main()