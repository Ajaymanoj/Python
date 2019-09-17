class inheritance:
    def __init__(self,name,age,roll,dept):
        self.name = name
        self.age = age
        self.roll = roll
        self.dept = dept

    def getname(self):
        print("The name of the mutant is: ", self.name)

    def getage(self):
        print("Age of the mutant is: ", self.age)

    def getall(self):
        print(self.name , "is from", self.dept, "and the age of the pupil is",self.age)

student = inheritance("Ajay","28","402187","Systems")

