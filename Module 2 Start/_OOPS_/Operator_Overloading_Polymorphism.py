
# Polymorphism.
# Function overloading   -> not supporting in python .

# Operator overloading   -> Python supports this .  ' IMPORTANT '

class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):   #  P1 invoke fun() __add__ Value of P1 goes to self and values of P2 goes to other.
        newa=self.a+other.a
        newb=self.b+other.b
        return Point(newa,newb)
    def __str__(self):          # __str__ invokes when we try to print an object . Provides the format .
        return "({0},{1})".format(self.a,self.b)

# P1=Point(2,3)
# P2=Point(1,2)
# print(P1)
# print(P2)
# print(P1+P2)

# Format -  build in function
# a=3
# b=4
# c=a+b
# print("sum of {0} and {1} is {2}".format(a,b,c))


# Homework .

# Complex class
# c=complex()
# d=complex()
# e=

class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __sub__(self, other):
        newr=self.r-other.r
        newi=self.i-other.i
        return Complex(newr,newi)
    def __str__(self):
        return "({0}+i{1})".format(self.r,self.i)

c1=Complex(10,5)
c2=Complex(2,3)
print(c1-c2)
print(c1)
print(c2)