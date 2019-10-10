def genBoard():
    return [0,0,0,0,0,0,0,0,0]

def printBoard(T):
    if len(T) == 9 and T[0] in range(0, 3) and T[1] in range(0, 3) and T[2] in range(0, 3) and T[3] in range(0, 3) and T[4] in range(0, 3) and T[5] in range(0, 3) and T[6] in range(0, 3) and T[7] in range(0, 3) and T[8] in range(0, 3):
        x = ""
        for i in range (0, len(T), 1):
            if T[i] == 0:
                x += " " + str(i)
            elif T[i] == 1:
                x += " X"
            elif T[i] == 2:
                x += " O"
            if i == 2 or i == 5 or i == 8:
                x += " "
                print(x)
                x = ""
                if i == 2 or i == 5:
                    print("---|---|---")
            else:
                x += " |"
        return True    
    else:
        return False
    
def analyzeBoard(T):
    wincounter = 0
    if len(T) == 9 and T[0] in range(0, 3) and T[1] in range(0, 3) and T[2] in range(0, 3) and T[3] in range(0, 3) and T[4] in range(0, 3) and T[5] in range(0, 3) and T[6] in range(0, 3) and T[7] in range(0, 3) and T[8] in range(0, 3):
        
        if T[0] == T[1] and T[1] == T[2] and not T[2] == 0:
            wincounter += 1

            if T[2] == T[3] and T[3] == T[6]:
                wincounter -= 1
                
            elif T[2] == T[5] and T[5] == T[8]:
                wincounter -= 1
                            
        elif T[3] == T[4] and T[4] == T[5] and not T[5] == 0:
            wincounter += 1
        
        elif T[6] == T[7] and T[7] == T[8] and not T[8] == 0:
            wincounter += 1
        
        elif T[0] == T[3] and T[3] == T[6] and not T[6] == 0:
            wincounter += 1
            
            if T[6] == T[7] and T[7] == T[8]:
                wincounter -= 1
        
        elif T[1] == T[4] and T[4] == T[7] and not T[7] == 0:
            wincounter += 1
        
        elif T[2] == T[5] and T[5] == T[8] and not T[8] == 0:
            wincounter += 1
            
            if T[8] == T[6] and T[6] == T[7]:
                wincounter -= 1
        
        elif T[0] == T[4] and T[4] == T[8] and not T[8] == 0:
            wincounter += 1
        
        elif T[2] == T[4] and T[4] == T[6] and not T[6] == 0:
            wincounter += 1
        
        if wincounter == 0 or wincounter == 1:
            
            if T[0] == T[1] and T[1] == T[2] and not T[2] == 0:
                return T[0]
                
            elif T[3] == T[4] and T[4] == T[5] and not T[5] == 0:
                return T[3]
            
            elif T[6] == T[7] and T[7] == T[8] and not T[8] == 0:
                return T[6]
            
            elif T[0] == T[3] and T[3] == T[6] and not T[6] == 0:
                return T[0]
            
            elif T[1] == T[4] and T[4] == T[7] and not T[7] == 0:
                return T[1]
            
            elif T[2] == T[5] and T[5] == T[8] and not T[8] == 0:
                return T[2]
            
            elif T[0] == T[4] and T[4] == T[8] and not T[8] == 0:
                return T[0]
            
            elif T[2] == T[4] and T[4] == T[6] and not T[6] == 0:
                return T[2]
            
            else:
                if T[0] == 0 or T[1] == 0 or T[2] == 0 or T[3] == 0 or T[4] == 0 or T[5] == 0 or T[6] == 0 or T[7] == 0 or T[8] == 0:    
                    
                    return 0
                
                else:
                    return 3
        else:
            return -1
    else:
        return -1