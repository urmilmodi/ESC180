#def main():
#    print(1)
#    print(1)
#    print(2)
#    print(3)
#    print(5)
#    print(8)
#    print(13)
#    print(21)
#    print(34)
#    print(55)
#    return True
    
#main()

def fibo(n):
    if n == 0 or n == 1:
        return 1
    
    elif n > 0:
        N = [1, 1]
        for i in range (0, n - 1, 1):
            N += [N[i] + N[i + 1]]
        return N[len(N) - 1]

def main():
    for i in range (0, 10, 1):
        print(fibo(i))

main()
