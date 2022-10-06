# n=int(input("Enter a number: "))
# print("Number before reversing =",n)
# while n>0:
#     d=n%10
#     n=n//10
#     print(d,end="")

n=int(input("Enter a number: "))
print("Number before reversing =",n)
s=0
while n>0:
    d=n%10
    s=s*10+d
    n=n//10
print(s)