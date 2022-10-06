#Sum of squares of first n natural numbers


n=int(input("Enter the limit :"))
sum=0
for i in range(1,n+1):
    print(i*i)
    sum=sum+(i*i)
print("Sum of squares of first",n,"natural numbers is:",sum)