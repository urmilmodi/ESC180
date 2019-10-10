def exp(a,b):
    ans = 1;
    i = 0;
    while i < b:
        ans = ans * a
        i = i + 1
    return ans
    
print(exp(int(input("Base")),int(input("Exponent"))))