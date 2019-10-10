def totalsum(N):
    s = 0
    for a in range (0, N + 1, 1):
        s += a
    return s

def diffsum(N):
    s = 0
    for a in range (0, N + 1, 1):
        print(a)
        print(a % 2)
        if a % 2 == 0:
            s -= a
        else:
            s += a
    return s
    
def LeibnizPi(n):
    pi = 0
    i = 0
    while abs(3.14159265 - pi) > n:
        
        if i % 2 == 0:
            pi += (4)/(2*i+1)
        else:
            pi -= (4)/(2*i+1)
        i += 1
    return pi

def Palindromize(word):
    x = word
    n = len(x)
    i = 1
    while x != x[::-1]:
        x += x[n - 1 - i]
        i += 1
    return x