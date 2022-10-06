
# To get a single value as result from doing some functions in list.
#  Available in functools by importing
# functools.reduce(function,sequence)  -  SYNDAX



# import functools
# lst=[1,2,3,4,5]
# result=functools.reduce(lambda x,y:x-y,lst)
# print(result)



# x=1
# y=2    1+2=3      1-2=-1
#
# x=3
# y=3    3+3=6     -1-3=-4
#
# x=6
# y=4    6+4=10    -4-4=-8
#
# x=10
# y=5    10+5=15   -8-5=-13


import functools
lst=[1,2,3,4,5,10,1,2,3]
result=functools.reduce(lambda x,y:x if x>y else y,lst)
print(result)