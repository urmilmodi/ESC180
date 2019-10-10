from tttlib import *

T = genBoard()
while True:
    printBoard(T)
    while True: # While loop to filter invalid/unavailable inputs
        while True: # While loop to filter invalid non-int inputs
            try:
                moveX = int(input("X move?"))
                break
            except ValueError:
                print("Invalid Move!")
        if moveX < 9 and moveX > -1 and T[moveX] == 0: # Check for valid input
            T[int(moveX)] = 1 # Set Position
            break
        else:
            print("Invalid Move!")

    # Check for winner/draw (Each Player is checked for after it plays)
    state = analyzeBoard(T)
    if state == 1:
        printBoard(T)
        print("X Won!")
        break
    elif state == 3:
        printBoard(T)
        print("Draw!")
        break

    printBoard(T)
    while True: # While loop to filter invalid/unavailable inputs
        while True: # While loop to filter invalid non-int inputs
            try:
                moveO = int(input("O move?"))
                break
            except ValueError:
                print("Invalid Move!")
        if moveO < 9 and moveO > -1 and T[moveO] == 0: # Check for valid input
            T[int(moveO)] = 2 # Set Position
            break
        else:
            print("Invalid Move!")

    # Check for winner/draw (Each Player is checked for after it plays)
    state = analyzeBoard(T)
    if state == 2:
        printBoard(T)
        print("O Won!")
        break
    elif state == 3:
        printBoard(T)
        print("Draw!")
        break
