
# Multiple inheritance
# a -> c <- b
# c inherits from both a and b

class Mark:
    def __init__(self,m):
        self.m=m
    def printmark(self):
        print("Mark is : ",self.m)
class Gracemark:
    def __init__(self,gm):
        self.gm=gm
    def printgmark(self):
        print("Grace Mark is : ",self.gm)
class Grade(Mark,Gracemark):
    def __init__(self,m,gm):
        Mark.__init__(self,m)
        Gracemark.__init__(self,gm)
    def calculate(self):
        Mark.printmark(self)
        Gracemark.printgmark(self)
        Total=self.m+self.gm
        p=(Total/500)*100
        if p>=80:
            print("Grade A")
        elif p>=70:
            print("Grade B")
        elif p>=60:
            print("Grade C")
        elif p>=50:
            print("Grade D")
        else:
            print("Failed")

stu1=Grade(350,50)
stu1.calculate()