for i in range(16):
    # Mux(a=a[0], b=b[0], sel=sel[1], out=temp1[0]);
    
    print(f"    Mux(a=temp1[{i}], b=temp2[{i}], sel=sel[0], out=out[{i}]);")
    
    