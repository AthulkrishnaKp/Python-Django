# def Binarysearch(lst,key):
#     lst.sort()
#     mid=0
#     low=0
#     high=len(lst)-1
#     while low<=high:
#         mid=(high+low)//2
#         if lst[mid]==key:
#             print("Key is found")
#             break
#         elif lst[mid]>key:
#             high=mid-1
#             lst=lst[:high]
#             return Binarysearch(lst,key)
#         elif lst[mid]<key:
#             low=mid+1
#             lst=lst[low:]
#             return Binarysearch(lst,key)
#     else:
#         print("Key is not found")
#
# lst=input("Enter the elements :").split()
# key=input("Enter the key :")
# Binarysearch(lst,key)


def Binarysearch(lst,key):
    lst.sort()
    mid=0
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==key:
            print("Key is found")
            break
        elif lst[mid]<key:
            low=mid+1
            lst=lst[low:]
            return Binarysearch(lst,key)
        else:
            high=mid-1
            lst=lst[:high]
            return Binarysearch(lst,key)
    else:
        print("Key not found")

lst=input("Enter the numbers :").split()
key=input("Enter the key :")
Binarysearch(lst,key)