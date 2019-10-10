from tttlib import *

while True:
    T = genBoard()
    User = input("User, X or O?")
    System = 1
    if User.capitalize() == "X":
        User = 1
        System = 2
    else:
        User = 2
      
    while True:
        
        if System == 1:
            
            T[int(Move(T, User))] = System
            
            # Check for winner/draw (Each User is checked for after it plays)
            state = analyzeBoard(T)
            if state == System:
                printBoard(T)
                print("Computer Won!")
                break
            elif state == 3:
                printBoard(T)
                print("Draw!")
                break
    
        printBoard(T)
        while True: # While loop to filter invalid/unavailable inputs
            while True: # While loop to filter invalid non-int inputs
                try:
                    if User == 1:
                        move = int(input("X User Move?"))
                    
                    elif User == 2:
                        move = int(input("O User Move?"))
                    break
                except ValueError:
                    print("Invalid Move!")
            if move < 9 and move > -1 and T[move] == 0: # Check for valid input
                T[int(move)] = User # Set Position
                break
            else:
                print("Invalid Move!")
    
        # Check for winner/draw (Each User is checked for after it plays)
        state = analyzeBoard(T)
        if state == User:
            printBoard(T)
            print("User Won!")
            break
        elif state == 3:
            printBoard(T)
            print("Draw!")
            break
        
        if System == 2:
            
            T[int(Move(T, User))] = System
        
            # Check for winner/draw (Each User is checked for after it plays)
            state = analyzeBoard(T)
            if state == System:
                printBoard(T)
                print("Computer Won!")
                break
            elif state == 3:
                printBoard(T)
                print("Draw!")
                break
