#Sum of Even numbers as of needed limit

n=int(input("Enter the limit : "))
sum=0
for i in range(2,n,2):    #i=2         i=4        i=6         i=8
    print(i)              #2           4          6           8
    sum=sum+i             #sum=0+2=2   sum=2+4=5  sum=6+6=12  sum=12+8=20
print("Sum is",sum)