#Sets
set1={1,2,3,34,1,2,3}
print(set1)                 #Output = {1,2,3,34}
set2={2,3,4,7,10}
print(set1.union(set2))          #all members of set1 and set2.
print(set1.intersection(set2))   #both set1 and set2 have.
print(set1.difference(set2))     #set1 have and set2 dont have.
print(len(set1))                 #Repeated elements dont count in set.
print(len(set2))