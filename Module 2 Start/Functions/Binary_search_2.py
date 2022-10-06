def Binarysearch(lst,key):
    lst.sort()
    mid=0
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if lst[mid]<key:
            low=mid+1
        elif lst[mid]>key:
            high=mid-1
        else:
            return mid
    return -1
lst=input("Enter the elements :").split()
key=input("Enter the key :")
f=Binarysearch(lst,key)
if f==-1:
    print("Key not found")
else:
    print("Key found")