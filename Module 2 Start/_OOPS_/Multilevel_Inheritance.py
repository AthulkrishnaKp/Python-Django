# class Student:
#     def __init__(self,n,r):
#         self.name=n
#         self.rno=r
#     def printdata(self):
#         print("Name is : ",self.name)
#         print("Roll no is : ",self.rno)
# class Mark(Student):
#     def __init__(self,n,r,m):
#         super().__init__(n,r)
#         self.mark=m
#     def printmark(self):
#         print("Mark is : ",self.mark)
# class Grade(Mark):
#     def __init__(self,n,r,m):
#         super().__init__(n,r,m)
#     def calculategrade(self):
#         p = (self.mark / 500) * 100
#         if p>=80:
#             print("Grade A")
#         elif p>=70:
#             print("Grade B")
#         elif p>=60:
#             print("Grade C")
#         elif p>=50:
#             print("Grade D")
#         else:
#             print("Failed")
#
# stu1 = Grade("Athul",12,250)
# stu1.printdata()
# stu1.printmark()
# stu1.calculategrade()


class Student:
    def __init__(self,n,r):
        self.name=n
        self.rno=r
    def printdata(self):
        print("Name is : ",self.name)
        print("Roll no is : ",self.rno)
class Mark(Student):
    def __init__(self,n,r,m):
        Student.__init__(self,n,r)
        self.mark=m
    def printmark(self):
        Student.printdata(self)
        print("Mark is : ",self.mark)
class Grade(Mark):
    def __init__(self,n,r,m):
        Mark.__init__(self,n,r,m)
    def calculategrade(self):
        Mark.printmark(self)
        p = (self.mark / 500) * 100
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

stu1 = Grade("Athul",12,400)
stu1.calculategrade()
stu2=Grade("Arun",13,300)
stu2.calculategrade()