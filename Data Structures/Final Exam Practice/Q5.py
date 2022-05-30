#Problem5
def is_min_heap(array):
    return helper(array, 0)

def helper(array, idx):
    left=idx*2+1
    right=idx*2+2
    if left>=len(array) and right>=len(array):
        return True
    left_flag=right_flag=True
    if left<len(array):
        if array[idx]>array[left]:
            left_flag=False
    if right<len(array):
        if array[idx]>array[right]:
            right_flag=False
    if not (left_flag and right_flag):
        return False
    return helper(array, left) and helper(array, right)
            

if __name__ == '__main__':
    #test case
    print(is_min_heap([9, 15, 11, 25, 17, 20])) #True
    print(is_min_heap([2, 4, 3, 6])) #True
    print(is_min_heap([2, 1, 3, 6])) #False
