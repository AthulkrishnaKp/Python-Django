#List comprehension :
# reducing number of codes.
# newflowers=[i for i in flowers if 'o' in i]     -   SYNDAX
     # here first i is the expression

#newlst=[expression for i in sequence]            -   SYNDAX

# flower=['lilly','Lotus','rose','sunflower']
# newlst=[]
# for i in flower:
#     for j in i:
#         if j=='o':
#             newlst.append(i)
# print(newlst)

#flowers=['lilly','Lotus','rose','sunflower']
# newflowers=[]
# for i in flowers:
#     if 'o' in i:
#         newflowers.append(i)
# print(newflowers)

# flowers=['lilly','Lotus','rose','sunflower']
# newflowers=[i for i in flowers]
# print(newflowers)
# newflowers=[i for i in flowers if 'o' in i]
# print(newflowers)
#
# num=[2,3,4,5,6]
# newnum=[i**3 for i in num]
# print(newnum)

# Create new list.
newlst=[i for i in range(1,6)]
print(newlst)

#
# Even numbers in a list.
# num=[2,3,4,5,6,7,8,9,10]
# newnum=[i for i in num if i%2==0]
# print(newnum)
#
# Square of even numbers.
# num=[2,3,4,5,6,7,8,9,10]
# newnum=[i**2 for i in num if i%2==0]
# print(newnum)
#
# odd numbers.
# num=[1,2,3,4,5,6,7,8,9,10]
# newnum=[i for i in num if i%2!=0]
# print(newnum)
#
# Square odd numbers.
# num=[1,2,3,4,5,6,7,8,9,10]
# newnum=[i**2 for i in num if i%2!=0]
# print(newnum)
# #
# flowers=['lilly','Lotus','rose','sunflower']
# newflowers=[i for i in flowers if 'o' in i]
# print(newflowers)

# flowers=['lilly','Lotus','rose','sunflower']
# newflowers=[i.upper() for i in flowers if 'o' in i]
# print(newflowers)

# flowers=['lilly','Lotus','rose','sunflower']
# newflowers=['hibiscus' for i in flowers if i!='lilly']
# print(newflowers)
#
# flowers=['lilly','Lotus','rose','sunflower']
# newflowers=['hibiscus' if i!='lilly' else 'lilly' for i in flowers]
# print(newflowers)


# SYNDAX

# newlst=[expression for i in sequence]              -   SYNDAX
# lst=[1,2,3,4,5]
# newlst=[i for i in lst]
#
#
# True
# newlst=[expression for i in sequ if(condition)]
# newlst=[i for i in list if(x%2==0)]
#
# True & False
# newlst=[true exp if(condition) else false exp for i in sequemce]


# flowers=['lilly','Lotus','rose','sunflower']
# newflowers=[i if i!='sunflower' else 'hibiscus' for i in flowers ]
# print(newflowers)

# num=[1,2,3,4,5,6]
# newlst=['odd' if i%2!=0 else 'Even' for i in num]
# print(newlst)