def exp(a, b):
    power = b
    if power == 0:
        return 1
    
    elif power >= 1:
        return a*exp(a, power - 1)
    
    elif power < 0:
        return 1/(exp(a, -power))
        
def sumlist(T):
    X = list(T)
    
    if len(X) == 1:
        return X[0]
    
    else:
        return X[0] + sumlist(X[1:len(T) - 1])
    
def fib(N):
    if N >= 2:
        return fib(N - 1) + fib(N - 2)
    
    elif N in range (0, 2, 1):
        return 1
    
    else:
        return "Only 0+ Numbers"
    
def printfib(N):
    x = ""
    for i in range (0, N + 1):
        
        if i < N:
            x += str(fib(i)) + ", "
            
        else:
            x += str(fib(i))
            
    return x

def sumfib(N):
    x = 0
    if N >= 0:
        
        for i in range (0, N + 1, 1):
            if i >= 2:
                x += fib(i - 1) + fib(i - 2)
            
            elif i in range (0, 2, 1):
                x += 1
    else:
        return "Only 0+ Numbers"
        
    return x

def fact(n):
    ans = 1
    i = 1
    while i <= n:
        ans = ans * i
        
        i = i + 1
        
    return ans

def PascalTriLine(n):
    if n >= 0:
        Line = [1]
        
        if n > 0:
            LineBefore = PascalTriLine(n - 1)
            for i in range (0, n - 1, 1):
                Line += [LineBefore[i] + LineBefore[i + 1]]
            Line += [1]
            return Line
        
        else:
            return [1]
    else:
        return "Error, input must be greater than or equal to 0"