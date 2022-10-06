#Home work
# Menu
# 1. Addition
# 2. subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# enter your choice
# enter num1
# enter num2
# result
# enter your coice if 5
# exit
# while true choice 5 break
print("   MENU")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
i=1
while i>0:
    n=int(input("Enter your choice: "))
    if n==1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a,"+",b,"= ",a+b)
    elif n==2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a,"-",b,"= ",a-b)
    elif n==3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a,"*",b,"= ",a*b)
    elif n==4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a,"/",b,"= ",round(a/b,2))
    while n==5:
        break






