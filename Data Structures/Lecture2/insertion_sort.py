def insertion_sort(lissy):
    sorted=[lissy[0]]
    lissy.pop(0)
    while lissy:
        key=lissy.pop(0)
        sorted.append(0)
        i=len(sorted)-2
        while sorted[i]>key and i>=0:
            sorted[i+1]=sorted[i]
            i-=1
        sorted[i+1]=key
    return sorted

lissy=[8,5,3,4,2]
print(insertion_sort(lissy))
        
        