# a=int(input("Enter first number 'A' :"))
# b=int(input("Enter second number 'B' :"))
# c=int(input("Enter third number 'C' :"))
# if a>b and a>c:
#     print(a,"is largest")
# elif b>a and b>c:
#     print(b,"is largest")
# elif c>a and c>b:
#     print(c,"is largest")
# else:
#     print("Two or all are same")


a = int(input("Enter first number 'A' :"))
b = int(input("Enter second number 'B' :"))
c = int(input("Enter third number 'C' :"))
if a > b:
    if a > c:
        print(a, "is largest")
    else:
        print(c, "is largest")
else:
    if b > c:
        print(b, "is largest")
    else:
        print(c, "is largest")
