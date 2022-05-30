def power(x,n):
    if n==0:
        return 1
    if n>0:
        return x*power(x,n-1)
    elif n<0:
        return 1/x*power(x,n+1)
    


def main():
    print(power(-2, 4))     # 16
    print(power(4, 3))      # 64
    print(power(-2, -3))    # -0.125

if __name__ == '__main__':
    main()