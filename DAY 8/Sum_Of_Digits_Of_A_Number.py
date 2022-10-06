#Find the sum of digits of a number
#123%10 d=3    sum=sum+d
#123//10 = 12
#12%10 d=2     sum=sum+d
#12//10=1
#1%10 d=1      sum=sum+d
#1//10=0  end

# n=int(input("Enter the number: "))  #123
# sum=0                               #Sum=0
# while n>0:                          #123>0   12>0    1>0     0>0
#     d=n%10                          #d=3     d=2     d=1     exit from loop
#     sum+=d                          #sum=3   sum=5   sum=6
#     n=n//10                         #n=12    n=1     n=0
# print(sum)


#Find the sum square of digits of a number

n=int(input("Enter the number: "))
sum=0
while n>0:
    d=(n%10)**2
    sum+=d
    n=n//10
print(sum)
