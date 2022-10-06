#My Work

# n=int(input("Enter the limit: "))
# for i in range(n):
#     if i==0:
#         a=i
#         print(i,end=" ")
#     elif i==1:
#         b=i
#         print(i,end=" ")
#     else:
#         c=a+b                 #c=0+1=1   c=1+1=2
#         print(c,end=" ")      #1         2
#         a=b                   #a=1       a=1
#         b=c                   #b=1       b=2


# n=int(input("Enter the limit :"))
# a=0
# b=1
# print(a,end=" ")
# print(b,end=" ")
# for i in range(2,n):
#     s=a+b
#     a=b
#     b=s
#     print(s,end=' ')


#Class Work

n=int(input("enter the limit : "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")