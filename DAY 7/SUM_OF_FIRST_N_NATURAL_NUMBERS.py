#Sum of first "n" natural numbers .

sum=0
n=int(input("Enter the number : "))
for i in range(1,n+1):
    print(i)
    sum=sum+i
print("Sum of first",n,"natural numbers is :",sum)