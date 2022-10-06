# Rectangle
# length
# bredth

# class Rectangle:                                            # class
#     def getdata(self,l,b):                                     #Member function
#         self.length = l        # int(input("Enter the length : "))      #data members
#         self.bredth = b        # int(input("Enter the bredth : "))      #data members
#     def displaydata(self):                                  #Member function
#         print("Length is : ",self.length)
#         print("Bredth is : ",self.bredth)
#     def area(self):
#         a=self.length*self.bredth
#         print("Area of rectangle is : ",a)
#
# r1=Rectangle()                                              #r1 - object 1
# r1.getdata(10,5)
# r1.displaydata()
# r1.area()
#
# r2=Rectangle()                                              #r2 - object 2
# r2.getdata(5,2)
# r2.displaydata()
# r2.area()
#
# r3=Rectangle()                                              #r3 - object 3
# r3.getdata(2,8)
# r3.displaydata()
# r3.area()


class Rectangle:
    def getdata(self,l,b):
        self.length = l
        self.bredth = b
    def displaydata(self):
        print("Length is : ",self.length)
        print("Bredth is : ",self.bredth)
    def area(self):
        a=self.length*self.bredth
        print("Area of rectangle is : ",a)

r1=Rectangle()                                              #r3 - object 3
r1.getdata(10,5)
r1.displaydata()
r1.area()
print(r1.length)     # length - Public data member can be accessed anywhere outside class.
print(r1.bredth)   # __bredth - Private data member cant be accessed outside class.