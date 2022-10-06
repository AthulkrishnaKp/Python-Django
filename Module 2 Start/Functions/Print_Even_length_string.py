# a=input("Enter the string :").split()
# for i in a:
#     if len(i)%2==0:
#         print(i)


a=input("Enter the string :").split()
b=int(input("Enter string limit :"))
for i in a:
    if len(i)==b:
        print(i)