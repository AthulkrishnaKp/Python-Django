#OPERATORS
#3+2  OPERATORS=+   OPERANTS=2,3

#arithmetic operators
    #Addition   +
    #Substraction  -
    #Multiplication  *
    #Division  /
    #Modulus  %
    #Floor division  //
    #Exponent  **

a=3
b=2
sum=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b           #3/2 reminder = modulus = 1
floordiv=a//b     #only integer part will be the output 3/2 , output=1(no decimal part)
exp=a**b          #2**2=4(2*2) 2**3=8(2*2*2) 2**4=16(2*2*2*2)
                  #3**2=9(3*3) 3**3=27(3*3*3)

print("Sum is:",sum)
print("Difference is:",sub)
print("Multiplication is:",mul)
print("Quotient is:",div)
print("Modulus is",mod)
print("Floor division is:",floordiv)
print("Exponent is:",exp)