
class Circle:
    def read(self):
        self.radi=int(input("Enter the Radius :"))
    def display(self):
        print("Radius of circle is : ",self.radi)
        a=3.14*(self.radi**2)
        print("Area of Circle is : ",a)

c1=Circle()
c1.read()
c1.display()

c2=Circle()
c2.read()
c2.display()

c3=Circle()
c3.read()
c3.display()