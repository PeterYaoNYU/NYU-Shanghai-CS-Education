
import timeit
import random

def timeFunction(f,n,repeat=1):
	return timeit.timeit(f.__name__+'('+str(n)+')',setup="from __main__ import "+f.__name__,number=repeat)/repeat

def insertion_sort(data_list):
    # 1. Split data into two parts: sorted & unsorted
    #    X | X X X X X X X
    #    sorted | unsorted
    # 2. While size of unsorted part is greater than zero锛?    #   a. let the target element be the first element in the unsorted part
    #   b. find targets insertion point in the sorted part
    #   c. make place at insertion point by shifting all larger elements
    #   d. insert the target in its final, sorted position

    # Coding: Please sort the values in-place, i.e. no new data_list is created and final sorted values are in data_list
    s=[0 for i in range(len(data_list))]
    s[0]=data_list[0]
    # n=len(data_list)
    # for i in range(1,n):
    #     key=data_list[i]
    #     for j in range(len(s)):
    #         if key<s[j]:
    #             s.insert(j,key)
    #             break
    #         elif j==i-1:
    #             s.append(key)

    # return s
    while data_list:
        key=data_list.pop(0)
        i=len(s)-1
        while s[i]>key and i>=0:
            s[i+1]=s[i]
            i-=1
        s[i]=key
    return s

        
            
        

    # for i in range(1,n):
    #     s=[data_list[0]]
    #     key=data_list[i]
    #     while i-1>=0 and s[i-1]>key:
    #         s[i]=s[i-1]
    #         i-=1
    #     s[i-1]=key
    # return s

            
                
            

def python_sort(data_list):
    # Use list.sort()
    # Python built in sort uses Tim-sort
    data_list.sort()
    return data_list

if __name__ == '__main__':
    # test=[1,5,2,3,7,4]
    # print(insertion_sort(test))
    data1 = []
    data2 = []
    for i in range(10000):
        value = random.randint(0,1000)
        data1.append(value)
        data2.append(value)
    print("Insertion sort 10000 elements:",
          '{:.6f}'.format(timeFunction(insertion_sort, data1)), "seconds")
    print("Built in sort 10000 elements:",
          '{:.6f}'.format(timeFunction(python_sort, data2)), "seconds")
          
    
