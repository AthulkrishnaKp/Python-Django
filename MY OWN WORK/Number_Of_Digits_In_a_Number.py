# Count the number of digits in a number

n=int(input("Enter the Number : "))
i=1
d=0
while i<=n:
    n=n//10
    d=d+i
print("Number of Digits =",d)





