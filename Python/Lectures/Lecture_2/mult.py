def mult(a,b):
    ans = 0;
    i = 0;
    while i < b:
        ans = ans + a
        i = i + 1
    return ans
    
print(mult(int(input("1st Number")),int(input("2nd Number"))))