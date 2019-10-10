import random

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
        self.data = x
        
    def getDisp(self):
        value = ""
        for i in self.data:
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
        if value in range (0, 2, 1) and row in range (0, len(self.data), 1) and column in range (0, len(self.data[0]), 1):
            
            self.data[row][column] = value
            return True
        else:
            return False
        
    def getNeighbours(self, row, column):
        if row in range (0, len(self.data), 1) and column in range (0, len(self.data[0]), 1):
            x = []
            if row == len(self.data) - 1:
                if column == len(self.data[row]) - 1:
                    x += [self.data[row - 1][column - 1]]
                    x += [self.data[row - 1][column]]
                    x += [self.data[row - 1][0]]
                    x += [self.data[row][column - 1]]
                    x += [self.data[row][0]]
                    x += [self.data[0][column - 1]]
                    x += [self.data[0][column]]
                    x += [self.data[0][0]]
                
                elif column == 0:
                    x += [self.data[row - 1][len(self.data[row]) - 1]]
                    x += [self.data[row - 1][column]]
                    x += [self.data[row - 1][column + 1]]
                    x += [self.data[row][len(self.data[row]) - 1]]
                    x += [self.data[row][column + 1]]
                    x += [self.data[0][len(self.data[row]) - 1]]
                    x += [self.data[0][column]]
                    x += [self.data[0][column + 1]]
                
                else:
                    x += [self.data[row - 1][column - 1]]
                    x += [self.data[row - 1][column]]
                    x += [self.data[row - 1][column + 1]]
                    x += [self.data[row][column - 1]]
                    x += [self.data[row][column + 1]]
                    x += [self.data[0][column - 1]]
                    x += [self.data[0][column]]
                    x += [self.data[0][column + 1]]
                    
            elif row == 0:
                if column == len(self.data[row]) - 1:
                    x += [self.data[len(self.data) - 1][column - 1]]
                    x += [self.data[len(self.data) - 1][column]]
                    x += [self.data[len(self.data) - 1][0]]
                    x += [self.data[row][column - 1]]
                    x += [self.data[row][0]]
                    x += [self.data[row + 1][column - 1]]
                    x += [self.data[row + 1][column]]
                    x += [self.data[row + 1][0]]
                
                elif column == 0:
                    x += [self.data[len(self.data) - 1][len(self.data[row]) - 1]]
                    x += [self.data[len(self.data) - 1][column]]
                    x += [self.data[len(self.data) - 1][column + 1]]
                    x += [self.data[row][len(self.data[row]) - 1]]
                    x += [self.data[row][column + 1]]
                    x += [self.data[row + 1][len(self.data[row]) - 1]]
                    x += [self.data[row + 1][column]]
                    x += [self.data[row + 1][column + 1]]
                
                else:
                    x += [self.data[len(self.data) - 1][column - 1]]
                    x += [self.data[len(self.data) - 1][column]]
                    x += [self.data[len(self.data) - 1][column + 1]]
                    x += [self.data[row][column - 1]]
                    x += [self.data[row][column + 1]]
                    x += [self.data[row + 1][column - 1]]
                    x += [self.data[row + 1][column]]
                    x += [self.data[row + 1][column + 1]]
                    
            elif column == len(self.data[row]) - 1:
                x += [self.data[row + 1][column - 1]]
                x += [self.data[row + 1][column]]
                x += [self.data[row + 1][0]]
                x += [self.data[row][column - 1]]
                x += [self.data[row][0]]
                x += [self.data[row - 1][column - 1]]
                x += [self.data[row - 1][column]]
                x += [self.data[row - 1][0]]
                
            elif column == 0:
                x += [self.data[row + 1][len(self.data[row]) - 1]]
                x += [self.data[row + 1][column]]
                x += [self.data[row + 1][column + 1]]
                x += [self.data[row][len(self.data[row]) - 1]]
                x += [self.data[row][column + 1]]
                x += [self.data[row - 1][len(self.data[row]) - 1]]
                x += [self.data[row - 1][column]]
                x += [self.data[row - 1][column + 1]]
                
            else:
                x += [self.data[row + 1][column - 1]]
                x += [self.data[row + 1][column]]
                x += [self.data[row + 1][column + 1]]
                x += [self.data[row][column - 1]]
                x += [self.data[row][column + 1]]
                x += [self.data[row - 1][column - 1]]
                x += [self.data[row - 1][column]]
                x += [self.data[row - 1][column + 1]]
                
            return x
        else:
            return False