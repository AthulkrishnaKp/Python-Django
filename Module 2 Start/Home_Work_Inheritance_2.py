class Person:
    def __init__(self):
        self.name=input("Enter the name : ")
        self.code=int(input("Enter the code : "))
    def displaydata(self):
        print("Name is : ",self.name)
        print("Code is : ",self.code)
class Member_pay(Person):
    def __init__(self):
        self.pay=int(input("Enter the ammount paid to the person : "))
    def displaypay(self):
        print("Ammount paid : ",self.pay)
class Experience(Person):
    def __init__(self):
        self.exp=input("Enter the Experience : ")
    def displayexp(self):
        print("Experience of the person : ",self.exp)
class Employee(Member_pay,Experience):
    def __init__(self):
        Person.__init__(self)
        Member_pay.__init__(self)
        Experience.__init__(self)

    def display(self):
        Person.displaydata(self)
        Member_pay.displaypay(self)
        Experience.displayexp(self)

emp1=Employee()
emp1.display()
