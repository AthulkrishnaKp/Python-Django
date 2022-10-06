# Constructor
# used to initialize data members .
# To give values to data members.
# in python default constructor is __init__ .
# Constructor is a member fun()
# automatically invoke if we create an object.


class Rectangle:
    def __init__(self, l, b):  # Here init is contractor .
        self.length = l
        self.bredth = b

    def displaydata(self):
        print("Length is : ", self.length)
        print("Bredth is : ", self.bredth)

    def area(self):
        a = self.length * self.bredth
        print("Area of rectangle is : ", a)


r1 = Rectangle(10, 5)
r1.displaydata()
r1.area()

r2 = Rectangle(14, 12)
r2.displaydata()
r2.area()
