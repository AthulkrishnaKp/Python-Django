lst=[1,2,3,4,5,6]
lst1=[]
lst1.insert(0,lst[-1])
print(lst1)
for i in range(1,len(lst)):
    lst1.insert(i,lst[i])
lst1.insert(-1,lst[0])
lst1.pop(lst1[-1])
print(lst1)

# lst=[1,2,3,4,5,6]
# lst[0],lst[-1]=lst[-1],lst[0]
# print(lst)

