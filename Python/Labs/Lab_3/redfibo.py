def fibo(n):
    if n == 0 or n == 1:
        return 1
    
    elif n > 0:
        N = [1, 1]
        for i in range (0, n - 1, 1):
            N += [N[i] + N[i + 1]]
        return N[len(N) - 1]
    
def fiboL(n):
    A = []
    for i in range (0, n + 1, 1):
        A += [fibo(i)]
    return A

def redfibo(n):
    A = fiboL(n)
    B = 1
    for i in A:
        B = B*i
    return B
