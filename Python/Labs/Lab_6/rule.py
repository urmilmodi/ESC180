def rule(key, L): 
    total = 0
    for i in L:
        total += i
    if key == 1:
        if total == 2 or total == 3:
            return 1
        
        else:
            return 0
    
    else:
        if total == 3:
            return 1
        
        else:
            return 0