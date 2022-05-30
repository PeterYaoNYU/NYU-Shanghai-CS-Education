import random
def insertion_sort(l):
    for i in range(1, len(l)):
        j=i-1
        temp=l[i]
        while j>=0 and l[j]>temp:
            l[j+1]=l[j]
            j-=1
        l[j+1]=temp
    return l

l=[]
for i in range(20):
    l.append(random.randint(0,100))
print(l)
print(insertion_sort(l))
print(insertion_sort(l)==sorted(l))