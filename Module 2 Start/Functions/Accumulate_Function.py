# Accumulate -  SYNDAX  =  accumulate(sequence,function)

import itertools
lst=[1,2,3,4]
res=itertools.accumulate(lst)
print(list(res))

import itertools
lst=[1,2,3,4]
res=itertools.accumulate(lst,lambda x,y:x*y)
print(list(res))