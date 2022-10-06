# To check three digit armstrong number
# 153 , 1**3+5**3+3**3=153
# 27+125+1=153

# n=int(input("Enter the number: "))
# sum=0
# num=n
# while n>0:
#     d=(n%10)**3
#     sum+=d
#     n=n//10
# if num==sum:
#     print(num,"is Armstrong number")
# else:
#     print(num,"is Not Armstrong number")

# To check armstrong number (any digit)
# 1234=1^4+2^4+3^4+4^4

# My Program

# n=int(input("Enter the number: "))
# sum=0
# num=num1=n
# d1=0
# i=1
# while i<=n:
#     n=n//10
#     d1=d1+i
# print(d1)
# while(num>0):
#     d=num%10
#     sum=sum+d**d1
#     num=num//10
# if num1==sum:
#     print(num1,"is Armstrong number")
# else:
#     print(num1,"is Not Armstrong number")




n=int(input("Enter the number: "))
sum=0
num=num1=n
count=0
while n>0:
    n=n//10
    count=count+1
print(count)
while num>0:
    d=num%10
    sum=sum+d**count
    num=num//10
if num1==sum:
    print(num1,"is Armstrong number")
else:
    print(num1,"is Not Armstrong number")
