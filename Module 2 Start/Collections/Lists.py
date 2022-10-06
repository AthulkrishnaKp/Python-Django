#Collections

#Lists
#tuple
#set
#dictonary

#1. List (Mutable) (values can be changed)

#NESTED LIST

# lst=[1,2,3,[4,5],6]
# print(lst)
# print(len(lst))         #Length will be 5
# lst[0]=1
# lst[1]=2
# lst[2]=3
# lst[3]=[4,5]
      # lst[3][0]=4
      # lst[3][1]=5
# lst[4]=6

# Access element '8' in list.

# lst=[1,2,3,[4,5,[7,8]],6]
# print(lst)
# print(lst[3][2][1])

# lst=[1,2,'adam',4,6]

# #indexing (Forward & Backward) & Slicing

# print(lst[::-1])
# print(lst[1:4])
# print(lst[1:])
# print(lst[2])
# lst[0]=9                #elements can be Changed ie: " List is Mutable "
# lst[2]='Ram'
# print(lst)              #List is mutable
#
# lst.append(5)
# lst.append(100)
# lst.append(45)
# lst.extend([3,5,6,7])   #to add many new values to list
# lst.insert(3,5)         #insert(index,value) in 3rd place 5 will be replaced in place of 4.
# print(lst)
#
# lst.pop()               #Removes the last element(pop)
# lst.pop(2)              #Element in index 2 is removed ie: "ram is removed"
# print(lst)
# lst.remove(2)           #The value 2 is removed ie: difference between pop and remove.
# print(lst)
#
#
# lst=[1,2,34,12,89,8]
# lst.sort()              #Sort values in assending order.
# lst.sort(reverse=True)  #Sort values in desending order.
# lst.reverse()           #Reverse the given list.
# print(max(lst))         #Print maximum of list element.
# print(min(lst))         #Minimum of list


#Find the second largest element in the list :

# lst=[1,2,3,4,5,6]
# lst.sort()
# lst.pop(-1)
# print("Largest element in list is : ",lst[-1])

#Find sum of elements in list :

# sum=0
# lst=input("Enter list elements :").split(',')  #elements should be entered with seperated by commas. eg:1,2,3,4,6
# print(lst)
# for i in lst:
#     sum=sum+int(i)
# print("Sum of elements in list is :",sum)

#Print sum of even numbers in list

# sum=0
# lst=input("Enter list elements :").split(',')
# print(lst)
# for i in lst:
#     if int(i)%2==0:
#         sum=sum+int(i)
# print("Sum of elements in list is :",sum)

#Print all even numbers in list.

# sum=0
# lst=input("Enter list elements :").split(',')
# print(lst)
# for i in lst:
#     if int(i)%2==0:
#         print("even numbers in list : ",i)

#even numbers list and odd number list from a given list.

# sum=0
# lst=input("Enter list elements :").split(',')
# evenlist=[]          #This is how we Create a list .
# oddlist=[]
# for i in lst:
#     if int(i)%2==0:
#         evenlist.append(i)
#     else:
#         oddlist.append(i)
# print("List of Even numbers :",evenlist)
# print("List of Odd numbers  :",oddlist)
