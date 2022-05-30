def unique(S):
    """
    :param S: List[Any] -- list of values.
    :return: True if all values within s are unique.
             False otherwise.
    """
    return helper(0,1,S)

def helper(ele_pointer, position, s):
    if position==len(s):
        return helper(ele_pointer+1, ele_pointer+2, s)
    if ele_pointer==len(s):
        return True
    if s[ele_pointer]==s[position]:
        return False
    return helper(ele_pointer, position+1, s)


def main():
    print(unique([1,7,6,5,4,3,1]))   # False
    print(unique([9,4,3,2,1,8]))     # True
    print(unique(['9',[],4,3,2,1,8]))     # True
    print(unique([1, 3, 2, 1]))    # False
    print(unique([3, 1, 2, 5]))    # True


if __name__ == '__main__':
    main()