import random
from rule import *

class conway:
    def __init__(self, numoflists, numofelements, elementchosen):
        x = []
        value = 0
        for i in range (0, numoflists, 1):
            y = []
            for j in range (0, numofelements, 1):
                if elementchosen == 'zeros':
                    value = 0
                
                elif elementchosen == 'random':
                    value = random.randint(0, 1)
                    
                y += [value]
            x += [y]
        self.store = x
        
    def getDisp(self):
        value = ""
        for i in self.store:
            for j in i:
                if j == 0:
                    value += " "
                
                elif j == 1:
                    value += "*"
            value += "\n"
        
        return value[0:len(value) - 1]
    
    def printDisp(self):
        try:
            print(self.getDisp())
        except:
            return False
        
        return True
    
    def setPos(self, row, column, value):
        if value in range (0, 2, 1) and row in range (0, len(self.store), 1) and column in range (0, len(self.store[0]), 1):
            
            self.store[row][column] = value
            return True
        else:
            return False
        
    def getNeighbours(self, row, column):
        if row in range (0, len(self.store), 1) and column in range (0, len(self.store[0]), 1):
            x = []
            if row == len(self.store) - 1:
                if column == len(self.store[row]) - 1:
                    x += [self.store[row - 1][column - 1]]
                    x += [self.store[row - 1][column]]
                    x += [self.store[row - 1][0]]
                    x += [self.store[row][column - 1]]
                    x += [self.store[row][0]]
                    x += [self.store[0][column - 1]]
                    x += [self.store[0][column]]
                    x += [self.store[0][0]]
                
                elif column == 0:
                    x += [self.store[row - 1][len(self.store[row]) - 1]]
                    x += [self.store[row - 1][column]]
                    x += [self.store[row - 1][column + 1]]
                    x += [self.store[row][len(self.store[row]) - 1]]
                    x += [self.store[row][column + 1]]
                    x += [self.store[0][len(self.store[row]) - 1]]
                    x += [self.store[0][column]]
                    x += [self.store[0][column + 1]]
                
                else:
                    x += [self.store[row - 1][column - 1]]
                    x += [self.store[row - 1][column]]
                    x += [self.store[row - 1][column + 1]]
                    x += [self.store[row][column - 1]]
                    x += [self.store[row][column + 1]]
                    x += [self.store[0][column - 1]]
                    x += [self.store[0][column]]
                    x += [self.store[0][column + 1]]
                    
            elif row == 0:
                if column == len(self.store[row]) - 1:
                    x += [self.store[len(self.store) - 1][column - 1]]
                    x += [self.store[len(self.store) - 1][column]]
                    x += [self.store[len(self.store) - 1][0]]
                    x += [self.store[row][column - 1]]
                    x += [self.store[row][0]]
                    x += [self.store[row + 1][column - 1]]
                    x += [self.store[row + 1][column]]
                    x += [self.store[row + 1][0]]
                
                elif column == 0:
                    x += [self.store[len(self.store) - 1][len(self.store[row]) - 1]]
                    x += [self.store[len(self.store) - 1][column]]
                    x += [self.store[len(self.store) - 1][column + 1]]
                    x += [self.store[row][len(self.store[row]) - 1]]
                    x += [self.store[row][column + 1]]
                    x += [self.store[row + 1][len(self.store[row]) - 1]]
                    x += [self.store[row + 1][column]]
                    x += [self.store[row + 1][column + 1]]
                
                else:
                    x += [self.store[len(self.store) - 1][column - 1]]
                    x += [self.store[len(self.store) - 1][column]]
                    x += [self.store[len(self.store) - 1][column + 1]]
                    x += [self.store[row][column - 1]]
                    x += [self.store[row][column + 1]]
                    x += [self.store[row + 1][column - 1]]
                    x += [self.store[row + 1][column]]
                    x += [self.store[row + 1][column + 1]]
                    
            elif column == len(self.store[row]) - 1:
                x += [self.store[row + 1][column - 1]]
                x += [self.store[row + 1][column]]
                x += [self.store[row + 1][0]]
                x += [self.store[row][column - 1]]
                x += [self.store[row][0]]
                x += [self.store[row - 1][column - 1]]
                x += [self.store[row - 1][column]]
                x += [self.store[row - 1][0]]
                
            elif column == 0:
                x += [self.store[row + 1][len(self.store[row]) - 1]]
                x += [self.store[row + 1][column]]
                x += [self.store[row + 1][column + 1]]
                x += [self.store[row][len(self.store[row]) - 1]]
                x += [self.store[row][column + 1]]
                x += [self.store[row - 1][len(self.store[row]) - 1]]
                x += [self.store[row - 1][column]]
                x += [self.store[row - 1][column + 1]]
                
            else:
                x += [self.store[row + 1][column - 1]]
                x += [self.store[row + 1][column]]
                x += [self.store[row + 1][column + 1]]
                x += [self.store[row][column - 1]]
                x += [self.store[row][column + 1]]
                x += [self.store[row - 1][column - 1]]
                x += [self.store[row - 1][column]]
                x += [self.store[row - 1][column + 1]]
                
            return x
        else:
            return False
    
    def evolve(self, function):
        x = []
        for i in range (0, len(self.store), 1):
            y = []
            for j in range (0, len(self.store[i]), 1):
                y += [0]
            x += [y]
        
        for i in range(0, len(x), 1):
            for j in range(0, len(x[i]), 1):
                x[i][j] = function(self.store[i][j], self.getNeighbours(i,j))

        for i in range(0, len(x), 1):
            for j in range(0, len(x[i]), 1):
                self.store[i][j] = x[i][j]
        return True