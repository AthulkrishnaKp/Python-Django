# Linear Search

def linearsearch(lst,key):
    for i in lst:
        if i==key:
            print("Key found at position",lst.index(i)+1)
            break
    else:
        print("Key not found")

lst=[1,10,34,56,4,67,74]
key=74
linearsearch(lst,key)