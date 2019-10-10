class counter:
    def __init__(self, initCnt):
        self.cnt = initCnt
   
    def evolve(self, x):
        self.cnt = self.cnt + x
        return True
      
    def getState(self):
        return self.cnt
    
mycnt = counter(1000)
x = counter(1)
print(x.getState())
print(mycnt.getState())
mycnt.evolve(100)
print(mycnt.getState())
x.evolve(mycnt.getState())
print(x.getState())
mycnt.evolve(-500)
print(mycnt.getState())
x.evolve(mycnt.getState())
print(x.getState())
