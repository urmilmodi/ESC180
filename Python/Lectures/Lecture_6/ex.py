def exp(a, b):
    if a == 0:
        return "Error"
    
    elif b == 0:
        return 1
    
    elif b > 0:
        ans = 1
        for i in range (0, b, 1):
            ans = ans*a
        return ans
    
    elif b < 0:
        return 1/exp(a, -b)
    
def fibo(n):
    if n == 0 or n == 1:
        return 1
    
    elif n > 0:
        N = [1, 1]
        for i in range (0, n - 1, 1):
            N += [N[i] + N[i + 1]]
        return N[len(N) - 1]
    
def pascaltriline(n):
    if n >= 0:
        Line = [[1]]
        for i in range (0, n, 1):
            Line += [[1]]
            for j in range (0, len(Line[i - 1]) - 1, 1):
                Line[i] += [Line[i - 1][j] + Line[i - 1][j + 1]]
            Line[i] += [1]
        return Line[n - 1]
        
    else:
        return "Error, input must be greater than or equal to 0"

def pascaltri(n):
    if n >= 0:
        Line = [[1]]
        for i in range (0, n, 1):
            Line += [[1]]
            for j in range (0, len(Line[i - 1]) - 1, 1):
                Line[i] += [Line[i - 1][j] + Line[i - 1][j + 1]]
            Line[i] += [1]
        return Line[n - 1]
    
def trinomialtriline(n):
    if n >= 0:
        Line = [[1], [1, 1, 1]]
        if n > 1:
            for i in range(2, n + 1, 1):
                Line += [[1]]
                Line[i] += [2]
                for j in range (0, len(Line[i - 1]) - 2, 1):
                    Line[i] += [Line[i - 1][j] + Line[i - 1][j + 1] + Line[i - 1][j + 2]]
                Line[i] += [i]
                Line[i] += [1]
            return Line[n]
        else: 
            return Line[n]
    else:
        return "Error, input must be greater than or equal to 0"    

def bernoullitriline(n):
    if n >= 0:
        Line = [[1]]
        for i in range (0, n, 1):
            Line += [[1]]
            for j in range (0, len(Line[i - 1]) - 1, 1):
                Line[i] += [Line[i - 1][j] + Line[i - 1][j + 1]]
            Line[i] += [2*Line[i - 1][len(Line[i - 1]) - 1]]
        return Line[n - 1]
        
    else:
        return "Error, input must be greater than or equal to 0"