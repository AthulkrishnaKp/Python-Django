#Tuple=(1,2,3,"Ram","syam")
#Tuple is immutable ie: items cannot be changed .
tuple1=(1,2,3,9,4,2,11)

#tuple1[2]=35     * Immutable,value cannot be changed .

print(len(tuple1))
print(tuple1.count(2))
print(tuple1.index(3))
#  print(tuple1.append(1))      # cannot append values in tuple .
print(max(tuple1))              # max of tuple1 .
print(min(tuple1))              # min of tuple1 .
print(sorted(tuple1))           # to sort tuple1 assending .

#Find sum of elements .

# tuple1=(1,2,3,9,4,2,11)
# sum=0
# for i in tuple1:
#     sum+=i
# print(sum)

#Search an element .

# tuple1=input("Enter elements in tuple : ").split(',')
# print(tuple1)
# tuple1=tuple(tuple1)
# print(tuple1)
# n=input("Enter the element :")
# for i in tuple1:
#     if i==n:
#         print("Element is found in Tuple")
#         break
# else:
#     print("Element not found in Tuple")

