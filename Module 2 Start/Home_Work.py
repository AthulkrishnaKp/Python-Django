# 1 question .

str=input("Enter the word :")
print(str)
n=int(input("Enter the index to be removed :"))
a=str[n]
print(str[0:str.index(a)]+str[str.index(a)+1:])

# 2 question .


# def power(a,n):
#     if n==0:
#         return 1
#     else:
#         return a*power(a,n-1)
#
# print(power(5,3))


