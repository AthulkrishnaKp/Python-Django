# Conditional statement

#1. Simple if
#2. if--else
#3. if..elif..else
#4. Nested if

# Simple if
# if condition:
#     statements...

#Q1.Check the given number is positive

# num=int(input("Enter the number :"))
# if num>0:
#     print("The number is positive")

# if--else
# if condition:     if condition true
#     statements    print
# else:             if 'ifcondition' wrong
#     statement     output

# num=int(input("Enter the number :"))
# if num>0:
#     print("The number is positive")
# else:
#     print("Negative or zero")


# if...elif...else

# if(condition 1):
#     stmts  #will execute if condition 1 correct.
# elif(condition 2):
#     stmts  #will execute if condition 2 correct.
# else:
#     stmts  #will execute if both condition wrong.

# num=int(input("Enter the number :"))
# if num>0:
#     print("The number is positive")
# elif num<0:
#     print("The number is negative")
# else:
#     print("The number is zero")


#Nested if
#if statement contains another if statement is called nested if

# 1  ************************

# if(condition):
#     if(condition):
#         stmnts
# else:
#     stmnts

# 2  *************************

# if(condition):
#     stmnts
# else:
#     if(condition):
#         stmnts
#     else:
#         stmnts

# 3  *************************

# if(condition):
#     if (condition):
#         stmnts
#     else:
#         stmnts
# else:
#     if(condition):
#         stmnts
#     else:
#         stmnts

# num=int(input("Enter the number :"))
# if num>0:
#      print("POSITIVE")
# else:
#     if num<0:
#          print("NEGATIVE")
#     else:
#          print("ZERO")

a=int(input("Enter first number 'A' :"))
b=int(input("Enter second number 'B' :"))
c=int(input("Enter third number 'C' :"))
if a>b:
    if a>c:
        print(a,"is largest")
    else:
        print(c,"is largest")
else:
    if b>c:
        print(b,"is largest")
    else:
        print(c,"is largest")
