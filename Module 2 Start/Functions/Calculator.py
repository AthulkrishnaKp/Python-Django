def sum(a,b):
    c=a+b
    print(a,"+",b,'=',c)
def subs(a,b):
    c=a-b
    print(a,"-",b,'=',c)
def mult(a,b):
    c=a*b
    print(a,"*",b,'=',c)
def div(a,b):
    c=a/b
    print(a,"/",b,'=',c)
while(1):
    print("   MENU   ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    c=int(input("Enter your choice : "))
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    if c==1:
        sum(a,b)
    elif c==2:
        subs(a,b)
    elif c==3:
        mult(a,b)
    elif c==4:
        div(a,b)
    else:
        print("Wrong Choice")
        break

