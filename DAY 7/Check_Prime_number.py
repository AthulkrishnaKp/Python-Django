# n=int(input("Enter a number :"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print(n,"is not prime number")
#             break
#     else:
#         print(n, "is a prime number")
# else:
#     print(n, 'is not a prime number')
    
n=int(input("Enter the number : "))
count=0
for i in range(1,n+1):
     if n%i==0:
        count=count+1
if count==2:
    print(n,"is a Prime number")
else:
    print(n,"is not a Prime number")
    
    


