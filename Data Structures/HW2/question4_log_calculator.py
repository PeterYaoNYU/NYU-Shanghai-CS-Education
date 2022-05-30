'''
Note:
To get autograded on gradescope, you program can't print anything.
'''




# from typing import final


def LG1(m,n):
    """
    using the first method, calculate k = lg_m n

    The only arithmetical operations you may use are + and *.
    remember to mention your runtime in terms of k as comment!

    :param m: positive integer, the base
    :param n: positive integer

    :return: k, the greatest integer such that m^k ≤ n
    """
    k=0
    left=1
    right=m
    while True:
        if left<=n and right>n:
            return k
        k+=1
        left*=m
        right*=m
        # my analysis:
        # O(k) in the worst case
        
        


def LG2(m,n):
    """
     using the second method, calculate k = lg_m n
     The only arithmetical operations you may use are + and *.

     :param m: positive integer, the base
     :param n: positive integer
     required runtime complexity: O(logk) in the worst case
     required memory complexity: O(logk)

     :return: k, the greatest integer such that m^k ≤ n
     """
    
    l1, his, his2=find_l1(m,n)
    res=[len(his)-1]
    cur=his.pop()
    while his:
        temp=his.pop()
        if temp*cur<=n and temp*temp*cur>n:
            res.append(len(his))
            cur=cur*temp
    # print(res)
    final=0
    for i in res:
        final+=his2[i]
    return final
    # for i in range(len(res)):
    #     a=1
    #     while res[i]:
    #         a=a*2
    #         res[i]-=1
    #     final+=a
    
    
    # l1, now=find_l1(m,n)
    # res=[l1]
    # current=now
    # while now>2:
    #     temp=m
    #     count=0
    #     while True:
    #         if temp*temp==now:
    #             break
    #         temp*=temp
    #         count+=1
    #     if temp*current<=n and temp*temp*current>n:
    #         res.append(count)
    #         current=current*temp
    #     now=temp
    #     # previous process is bounded by l1, which is log(k)
    # # return res
    # final=0
    # for i in range(len(res)):
    #     a=1
    #     while res[i]:
    #         a=a*2
    #         res[i]-=1
    #     final+=a
    #     # again, the time that we do the multiplication is bounded by log(k)
    # return final
    
def find_l1(m,n):
    l1=0
    now=m
    # addition=m
    his=[m]
    his2=[1]
    final_cur=1
    while True:
        if now<n and now*now>n:
            # print(his)
            # print(his2)
            return l1, his, his2
        now=now*now
        final_cur*=2
        his2.append(final_cur)
        his.append(now)
        l1+=1
#  the process to get l1 is log(k)
           
    # res=[]
    # l1=LG1(m*m, n)
    # left=1
    # temp=0
    # while temp<l1:
    #     left=left*m*m
    #     temp+=1
    # print(left)
    # # print(l1)
    # res.append(l1)
    # while l1>=1:
    #     l1-=1
    #     temp=0
    #     right=left
    #     while temp<l1:
    #         right=right*m*m
    #         temp+=1
    #     if right<=n:
    #         res.append(l1)
    # print(res)

def main():
    print(LG1(3,345))  # Expect: 5
    print(LG1(3,3_000_000_000))  # Expect: 19

    print(LG2(2, 1000))  # Expect: 9
    print(LG2(2, 3_000_000_000))  # Expect: 31

if __name__ == '__main__':
    main()