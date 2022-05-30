# from sklearn.linear_model import lasso_path


# from turtle import pos 


# from turtle import pos


def knapsack_driver(capacity, weights):
    '''
    @capacity: positive integer. the value we are summing up to.
    @weights:  list of positive integers.

    ### Friendly tip: This function can't solve the problem, 
    ### you need more parameters to pass information between recursive functions.
    ### So, define another function!! Return the result from your new function!!

    @return: List of all combinations that can add up to capacity.
    '''
    res=knapsack(capacity, weights, 0, res=[], path=[])
    res2=knapsack2(capacity, weights, 0, path=[], res=[])
    # return len(res2)==len(res)
    return sorted(res)==sorted(res2)


    
    
def knapsack(capacity, weights, position, res=[], path=[]):
    n=len(weights)
    # path.append(weights[position])
    if sum(weights[position:])<capacity-sum(path) or sum(path)>capacity:
        return
    # elif sum(weights[position:])==capacity:
    #     res.append(path)
    #     return
    for i in range(position,n):
        temp=path[:]
        temp.append(weights[i])
        if sum(temp)==capacity:
            res.append(temp)
            continue
        knapsack(capacity, weights, i+1, res, temp)
    return res

def knapsack2(capacity,weights,position=0,path=[],res=[]):
    # knapsack(capacity-weights[position],weights, position+=1, path=pat
    if capacity==0:
        res.append(path)
        return
    if position==len(weights):
        return
    temp=path+[weights[position]]
    next_position=position+1
    knapsack2(capacity, weights, next_position, path, res )
    capacity=capacity-weights[position]
    knapsack2(capacity, weights, next_position,temp, res)
    return res

        
    
        
    
    



    # n=len(weights)
    # res=[]
    # if capacity==0:
    #     return [[]]
    
    # if len(weights)==0:
    #     return None
    # for i in range(n):
    #     if weights[i]<=capacity:
    #         last_ret=knapsack_driver(capacity-weights[i],weights[i+1:])
    #         if not last_ret:
    #             for j in last_ret:
    #                 j.append(weights[i])
    #             res.append(last_ret)
    # return res
        
            
            
            
    

def main():   
    casts = [1, 2, 8, 4, 9, 1, 4, 5]
    # order does not matter, inner values order doesn't matter either.
    # [[9, 5], [9, 1, 4], [4, 1, 4, 5], [4, 9, 1], [8, 1, 5], [2, 8, 4], 
    #[2, 8, 4], [1, 9, 4], [1, 4, 4, 5], [1, 4, 9], [1, 8, 5], [1, 8, 1, 4],
    #[1, 8, 4, 1]]
    print(knapsack_driver(14, casts))  

if __name__ == '__main__':
    main()