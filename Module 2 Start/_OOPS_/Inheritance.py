# Inheritance.
# Parent class/Super class
# Child class/Derived class.

# Parent class - Person
#          voter id
#          name
#          getdata()
#          printdata()

# Child class  - Employee                (All features of parent
#                salary                      class is accessed by child classs)
#                getsalary(),getdata()
#                printsalary(),printdata()

# create object of child class because it can access every functions
# including parent class also.

# class Person:
#     def getdata(self):
#         self.vid=input("Enter voter id : ")
#         self.name=input("Enter the name : ")
#     def printdata(self):
#         print("Voter id is : ",self.vid)
#         print("Name is : ",self.name)
# class Employee(Person):
#     def getsalary(self):
#         self.salary=int(input("Enter the salary : "))
#     def printsalary(self):
#         print("Salary is : ",self.salary)
#
#
# emp1=Employee()
# emp1.getdata()
# emp1.getsalary()
# emp1.printdata()
# emp1.printsalary()


# Overriding - if child fun() and parent fun() same name,
# child fun will only execute over parent class
# its called overriding.

# class Person:
#     def getdata(self):
#         self.vid=input("Enter voter id : ")
#         self.name=input("Enter the name : ")
#     def printdata(self):
#         print("Voter id is : ",self.vid)
#         print("Name is : ",self.name)
# class Employee(Person):
#     def getdata(self):
#         super().getdata()    # To access getdata from parent class.
#         self.salary=int(input("Enter the salary : "))
#     def printdata(self):
#         super().printdata()
#         print("Salary is : ",self.salary)
#
# emp1=Employee()
# emp1.getdata()
# emp1.printdata()


# Using Constructor .

# class Person:
#     def __init__(self):  # Constructor no need to be called seperate automatically invoke if we create object.
#         self.vid = input("Enter voter id : ")
#         self.name = input("Enter the name : ")
#
#     def printdata(self):
#         print("Voter id is : ", self.vid)
#         print("Name is : ", self.name)
#
#
# class Employee(Person):  # inherit from parent class. (child(parent))
#     def __init__(self):
#         super().__init__()
#         self.salary = int(input("Enter the salary : "))
#
#     def printdata(self):
#         super().printdata()
#         print("Salary is : ", self.salary)
#
#
# emp1 = Employee()
# emp1.printdata()

# This is a Single Inheritance .


class person:
    def __init__(self, v, n):
        self.vid = v                       #123
        self.name = n                      #Athul
    def display(self):
        print("Voterd id :", self.vid)
        print("Name id :", self.name)
class employee(person):                    #class child(parent)
    def __init__(self, v, n, s):           #123,'Athul',12000
        super().__init__(v, n)             #123, 'Athul'
        self.salary = s                    #12000
    def display(self):
        super().display()
        print("Salary is :", self.salary)         #12000


emp1 = employee(123, 'Athul', 12000)
emp1.display()

