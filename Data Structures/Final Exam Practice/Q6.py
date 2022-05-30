def return_missing(arr, low, high):
    # TODO
    output = []
    d={}
    for ele in arr:
        d[ele]=True
    for i in range(low, high):
        if d.get(i, False)==False:
            output.append(i)
        
        
    return output
    

if __name__ == '__main__':
    #test case1
    arr = [10, 12, 11, 15]
    low = 10
    high = 15
    print(return_missing(arr, low, high)) #Expect: [13, 14]
    
    #test case2   
    arr = [1, 14, 11, 51, 15]
    low = 50
    high = 55
    print(return_missing(arr, low, high)) #Output: [50, 52, 53, 54]
