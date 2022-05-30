def pascal(n):
    if n==1:
        return [[1]]
    last_ret=pascal(n-1)
    last_row=last_ret[-1]
    res=[1]
    n=len(last_row)
    for i in range(n-1):
        temp=last_row[i]+last_row[i+1]
        res.append(temp)
    res.append(1)
    last_ret.append(res)
    return last_ret


def main():
    print(pascal(4))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

if __name__ == '__main__':
    main()
    