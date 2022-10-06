n=int(input("enter the number : "))
i=0
count=0
sum=0
num1=num=n
while n>0:
    count=count+1
    n=n//10
print(count)
while num>0:
    d=num%10
    sum=sum+d**count
    num=num//10
if num1==sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")

