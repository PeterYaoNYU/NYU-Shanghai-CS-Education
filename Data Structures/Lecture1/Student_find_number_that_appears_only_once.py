def find(lissy):
    # TODo
    # d={}
    # for i in lissy:
    #     if i in d.keys():
    #         d[i]+=1
    #     else:
    #         d[i]=1
    # for item in d.keys():
    #     if d[item]==1:
    #         return item
    c=[]
    for i in lissy:
        if i in c:
            continue
        occur=lissy.count(i)
        if occur==1:
            return i
        c.append(i)
        # use bitwise operator to solve this problem
        
    
    
        
        

def main():
    l1 = [7,1,5,3,6,4,7,1,5,6,4]
    l2 = [7,6,4,3,2,1,1,2,3,4,5,6,7]
    print(find(l1)) # expect: 3
    print(find(l2)) # expect: 5

if __name__ == '__main__':
    main()

