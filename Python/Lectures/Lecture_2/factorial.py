def fact(n):
    ans = 1;
    i = 1;
    while i <= n:
        ans = ans * i
        i = i + 1
    return ans
    
print(fact(int(input("Number"))))