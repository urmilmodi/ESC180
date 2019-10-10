class seqdetector:
    def __init__(self):
        self.values = []
        self.state = 0
    
    def evolve(self, word):
        Code = ["here", "are", "the", "solutions", "to", "the", "next", "exam"]
        self.values += [word]
        for i in range(0, len(self.values), 1):
            if self.values[i] == Code[i]:
                self.state = i + 1
                
            else:
                self.state = 0
                self.values = []
                break
            
        if self.state == 8:
            self.values = []
            return True
        return False
    
# Tester Code
def main():
    x=seqdetector()
    n=0
    while True:
        status=x.evolve(input()) 
        if status == True:
            print("Detected: end position is",n)
            break
        n = n+1
    return True

main()