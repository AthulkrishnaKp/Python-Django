#Simple calculator
#Enter two numbers
# 1.addition
# 2.substract
# 3.multiplication
# 4.division
#enter your choice
#Print result

a=int(input("Enter first number 'A'' :"))
b=int(input("Enter second number 'B' :"))
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
ch=int(input("Enter your choice :"))
if ch==1:
      print("A+B =",a+b)
elif ch==2:
      print("A-B = ",a-b)
elif ch==3:
      print("A*B =",a*b)
elif ch==4:
      print("A/B =",a/b)
else:
      print("WRONG CHOICE")
