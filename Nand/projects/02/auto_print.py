    # FullAdder(a=a[1], b=b[1], c=c1, sum=out[1], carry=c2);

    # Or(a=x[2], b=temp1, out=temp2);
for i in range(2,16):
    print(f"    Or(a=x[{i}], b=temp{i-1}, out=temp{i});")
    
    