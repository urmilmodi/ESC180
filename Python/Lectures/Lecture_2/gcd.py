def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(gcd(int(input("1st Number")), int(input("2nd Number"))))