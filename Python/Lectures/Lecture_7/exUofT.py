class UofT:
    def __init__(self, firstname, lastname, studentnumber, coursestaken, coursegrades, tuitionamount, paidornot):
        
        self.fname = firstname
        self.lname = lastname
        self.no = studentnumber
        self.courses = coursestaken
        self.grades = coursegrades
        self.tuition = tuitionamount 
        self.paid = paidornot
    
    def setfname(self, x):
        self.fname = x
        return True
    
    def setlname(self, x):
        self.lname = x
        return True
    
    def setno(self, x):
        self.no = x
        return True
    
    def setcourses(self, x):
        self.courses = x
        return True
    
    def setgrades(self, x):
        self.grades = x
        return True
    
    def settuition(self, x):
        self.tuition = x
        return True
    
    def setpaid(self, x):
        self.paid = x
        return True
    
    def getfname(self):
        return self.fname
    
    def getlname(self):
        return self.lname
    
    def getno(self):
        return self.no
    
    def getcourses(self):
        return self.courses
    
    def getgrades(self):
        return self.grades
    
    def gettuition(self):
        return self.tuition
    
    def getpaid(self):
        return self.paid
    
    def getDesc(self):
        return "First Name: " + self.fname + "\n" + "Last Name: " + self.lname + "\n" + "Student Number: " + self.no + "\n" + "Current Courses: " + self.courses + "\n" + "Current Grades: " + self.grades + "\n" + "Tuition ($): " + self.tuition + "\n" + "Tuition Paid: " + self.paid 
    
def main():
    fname = input("First Name: ")
    lname = input("Last Name: ")
    no = input("Student Number: ")
    courses = input("Current Courses: ")
    grades = input("Current Grades in Specified Courses: ")
    tuition = input("Tuition Amount in $")
    paid = input("Tuition Fully Paid (Yes or No): ")
    Student = UofT(fname, lname, no, courses, grades, tuition, paid)
    print(Student.getDesc())
    return True

main()