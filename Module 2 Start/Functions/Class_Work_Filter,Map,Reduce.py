lst=input("Enter the numbers :").split()
lst1=list(map(int,lst))
oddlst=list(filter(lambda x:x%2!=0,lst1))
evenlst=list(filter(lambda x:x%2==0,lst1))
from functools import reduce
sumeven=reduce(lambda x,y:x+y,evenlst)
sumodd=reduce(lambda x,y:x+y,oddlst)
print(sumeven)
print(sumodd)