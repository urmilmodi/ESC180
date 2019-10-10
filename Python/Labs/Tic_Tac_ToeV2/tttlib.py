import random

def genBoard():
    return [0,0,0,0,0,0,0,0,0]

def error(T):
    if len(T) == 9 and T[0] in range(0, 3) and T[1] in range(0, 3) and T[2] in range(0, 3) and T[3] in range(0, 3) and T[4] in range(0, 3) and T[5] in range(0, 3) and T[6] in range(0, 3) and T[7] in range(0, 3) and T[8] in range(0, 3):
        return True
    
    else:
        return False
    
def printBoard(T):
    if error(T):
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
    if error(T):
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
    
def analyzeBoardV2(T):
    if error(T):
        X = 0
        O = 0
        
        for i in T:
            if i == 1:
                X += 1
                
            elif i == 2:
                O += 1
        
        if True or X == O + 1 or X == O:
            
            Win = False
            WinMoves = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        
            for i in range (0, len(WinMoves)):
          
                if T[WinMoves[i][0]] == T[WinMoves[i][1]] and T[WinMoves[i][1]] == T[WinMoves[i][2]] and not T[WinMoves[i][2]] == 0:
                    Win = True
                    return T[WinMoves[i][0]]
            
            if not Win:
                
                if T[0] == 0 or T[1] == 0 or T[2] == 0 or T[3] == 0 or T[4] == 0 or T[5] == 0 or T[6] == 0 or T[7] == 0 or T[8] == 0:    
                    
                    return 0
                
                else:
                    return 3
    else:
        return -1

def errorAuto(T, Player):
    if error(T) and (T[0] == 0 or T[1] == 0 or T[2] == 0 or T[3] == 0 or T[4] == 0 or T[5] == 0 or T[6] == 0 or T[7] == 0 or T[8] == 0) and Player in range(1,3):
        return True
    
    else:
        return False

def Move(T, Player):
    if errorAuto(T, Player):
        
        if genWinningMove(T, Player) in range(0, 9):
            return genWinningMove(T, Player)
        
        elif genNonLoser(T, Player) in range(0, 9):
            return genNonLoser(T, Player)
        
        else:
            return genOpenMove(T, Player)
                
    else:
        return -1

def genNonLoser(T, Player):
    if errorAuto(T, Player):
        
        Opponent = 1
        if Player == 1:
            Opponent = 2
        
        T2 = list(T)
        for i in range (0, len(T2)):
            if T2[i] == 0:
                T2[i] = Opponent
                    
                if analyzeBoard(T2) == Opponent:
                    return i
                
                T2[i] = 0
    else:
        return -1

def genWinningMove(T, Player):
    if errorAuto(T, Player):
        
        T2 = list(T)
        for i in range (0, len(T2)):
            if T2[i] == 0:
                T2[i] = Player
                    
                if analyzeBoard(T2) == Player:
                    return i
                
                T2[i] = 0
    else:
        return -1

def genRandomMove(T, Player):
    if errorAuto(T, Player):
        return random.randint(0, 8)
    
    else:
        return -1
    
def genOpenMove(T, Player):
    if errorAuto(T, Player):
        
        RandomMove = random.randint(0, 8)
        while not T[RandomMove] == 0:
            RandomMove = random.randint(0, 8)
            
        return RandomMove
    else:
        return -1