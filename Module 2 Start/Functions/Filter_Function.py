# Filter function :  filter(fun,sequence)  - SYNDAX

# To filter the given list and make required list .
# like to filter even numbers from given list and make a even list.

# Even list
# lst=input("Enter the elements :").split()

# lst=[1,2,3,4,5,6]
# even=filter(lambda x:x%2==0,lst)
# print(list(even))

# Odd list.

# lst=input("Enter the elements :").split()
# odd=filter(lambda x:int(x)%2!=0,lst)
# print(list(odd))

#or

# lst=input("Enter the elements :").split()
# lst1=map(int,lst)
# odd=filter(lambda x:x%2!=0,lst1)
# print(list(odd))

# create a list from existing list which have only multiples of 5.

# lst=input("Enter the numbers :").split()
# lst1=map(int,lst)
# mult5=filter(lambda x:x%5==0,lst1)
# print(list(mult5))

# create a list from existing list where values greater than 5.

lst=input("Enter the numbers :").split()
lst1=map(int,lst)
num=filter(lambda x:x>5,lst1)
print(list(num))

lst=[1,2,3,4,5,6,7,8,9,10]
lst1=[i**2 if i%2!=0 else i for i in lst]
print(lst1)