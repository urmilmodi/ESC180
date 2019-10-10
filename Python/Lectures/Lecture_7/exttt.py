import random

class ttt:
    def __init__(self):

        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.g = 0
        self.h = 0
        self.i = 0
     
    def print(self):
        data = []
        for i in [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i]:
            if i == 0:
                data += " "
                
            elif i == 1:
                data += "X"
            
            else:
                data += "O"
        
        print(" " + data[0] + " | " + data[1] + " | " + data[2])
        print("---|---|---")
        print(" " + data[3] + " | " + data[4] + " | " + data[5])
        print("---|---|---")
        print(" " + data[6] + " | " + data[7] + " | " + data[8])
        return True
    
        def analyzeBoard(self):
            if self.a == self.b and self.b == self.c and not self.c == 0:
                    return self.a
                    
            elif self.d == self.e and self.e == self.f and not self.f == 0:
                    return self.d
            
            elif self.g == self.h and self.h == self.i and not self.i == 0:
                return self.g
            
            elif self.a == self.d and self.d == self.g and not self.g == 0:
                return self.a
            
            elif self.b == self.e and self.e == self.h and not self.h == 0:
                return self.b
            
            elif self.c == self.f and self.f == self.h and not self.h == 0:
                return self.c
            
            elif self.a == self.e and self.e == self.i and not self.i == 0:
                return self.a
            
            elif self.c == self.e and self.e == self.g and not self.g == 0:
                return self.c
            
            else:
                if self.a == 0 or self.b == 0 or self.c == 0 or self.d == 0 or self.e == 0 or self.f == 0 or self.g == 0 or self.h == 0 or self.i == 0:    
                    return 0
                
                else:
                    return 3
     
    def genNonLoser(self, Player):
        if self.analyzeBoard() == 0:
            
            Opponent = 1
            if Player == 1:
                Opponent = 2
            
            T2 = ttt(self)
            for i in range [T2.a, T2.b, T2.c, T2.d, T2.e, T2.f, T2.g, T2.h, T2.i]:
                if i == 0:
                    i = Opponent
                        
                    if T2.analyzeBoard() == Opponent:
                        return i
                    
                    i = 0
        else:
            return -1
    
    def genWinningMove(self, Player):
        if self.analyzeBoard() == 0:
            
            T2 = ttt(self)
            for i in range [T2.a, T2.b, T2.c, T2.d, T2.e, T2.f, T2.g, T2.h, T2.i]:
                if i == 0:
                    i = Player
                        
                    if T2.analyzeBoard() == Player:
                        return i
                    
                    i = 0
        else:
            return -1
    
    def genRandomMove(self):
        if self.analyzeBoard() == 0:
            return random.randint(0, 8)
        
        else:
            return -1
        
    def genOpenMove(self):
        if self.analyzeBoard() == 0:
            
            RandomMove = random.randint(0, 8)
            
            while not [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i][RandomMove] == 0:
                RandomMove = random.randint(0, 8)
                
            return RandomMove
        else:
            return -1
        
    def Move(self, Player):
        if self.analyzeBoard() == 0:
            
            if self.genWinningMove(Player) in range(0, 9):
                return self.genWinningMove(Player)
            
            elif self.genNonLoser(Player) in range(0, 9):
                return self.genNonLoser(Player)
            
            else:
                return self.genOpenMove(Player)
                    
        else:
            return -1

        
def main():
    while True:
        T = ttt()
        W = [T.a, T.b, T.c, T.d, T.e, T.f, T.g, T.h, T.i]
        User = input("User, X or O?")
        System = 1
        if User.capitalize() == "X":
            User = 1
            System = 2
        else:
            User = 2
                
        while True:
            
            if System == 1:
                
                W = [T.a, T.b, T.c, T.d, T.e, T.f, T.g, T.h, T.i]
                W[int(T.Move(User))] = System
                
                # Check for winner/draw (Each User is checked for after it plays)
                T.a = W[0]
                T.b = W[1]
                T.c = W[2]
                T.d = W[3]
                T.e = W[4]
                T.f = W[5]
                T.g = W[6]
                T.h = W[7]
                T.i = W[8]
                state = T.analyzeBoard()
                if state == System:
                    T.print
                    print("Computer Won!")
                    break
                elif state == 3:
                    T.print
                    print("Draw!")
                    break
        
            T.print
            while True: # While loop to filter invalid/unavailable inputs
                while True: # While loop to filter invalid non-int inputs
                    W = [T.a, T.b, T.c, T.d, T.e, T.f, T.g, T.h, T.i]
                    try:
                        if User == 1:
                            movep = int(input("X User Move?"))
                        
                        elif User == 2:
                            movep = int(input("O User Move?"))
                        break
                    except ValueError:
                        print("Invalid Move!")
                if movep < 9 and movep > -1 and W[movep] == 0: # Check for valid input
                    
                    W[int(movep)] = User # Set Position
                    break
                else:
                    print("Invalid Move!")
            
            # Check for winner/draw (Each User is checked for after it plays)
            T.a = W[0]
            T.b = W[1]
            T.c = W[2]
            T.d = W[3]
            T.e = W[4]
            T.f = W[5]
            T.g = W[6]
            T.h = W[7]
            T.i = W[8]
            state = T.analyzeBoard()
            if state == User:
                T.print
                print("User Won!")
                break
            elif state == 3:
                T.print
                print("Draw!")
                break
            
            if System == 2:
                
                W = [T.a, T.b, T.c, T.d, T.e, T.f, T.g, T.h, T.i]
                W[int(T.Move(User))] = System
                
                # Check for winner/draw (Each User is checked for after it plays)
                T.a = W[0]
                T.b = W[1]
                T.c = W[2]
                T.d = W[3]
                T.e = W[4]
                T.f = W[5]
                T.g = W[6]
                T.h = W[7]
                T.i = W[8]
                state = T.analyzeBoard()
                if state == System:
                    T.print
                    print("Computer Won!")
                    break
                elif state == 3:
                    T.print
                    print("Draw!")
                    break
main()