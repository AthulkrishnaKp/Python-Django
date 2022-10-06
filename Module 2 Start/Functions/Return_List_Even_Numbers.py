
#Print list of even numbers from a list.

def even():
    lst=input("Enter the numbers :").split(',')
    evenlst=[]
    for i in lst:
        if int(i)%2==0:
            evenlst.append(i)
    print(evenlst)

even()
