def bubbleSort(x):
    if len(x) == 0:
        return [True, x]
    
    for i in x:
        if not type(x[0]) == type(i):
            return [False, x]
        
    swap = True
    while swap:
        swap = False
        for i in range (1, len(x), 1):
            if x[i - 1] > x[i]:
                temp = x[i]
                x[i] = x[i + 1]
                x[i + 1] = temp
                swap = True
                break
    return [True, x]