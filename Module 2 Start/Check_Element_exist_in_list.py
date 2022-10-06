a=input("Enter the element :")
lst=[1,2,3,5,6,'ram','ramu','appu']
for i in (lst):
    if a==str(i):
        print("Element exist in Given List")
        break
else:
    print("Element not Found")