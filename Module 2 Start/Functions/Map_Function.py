# Map function :  map(function,sequence)
# To run a function along a given list and print the results in list or tuple.

# def mul(n):
#     return n*n

mul=lambda n:n*n
num=(1,2,3,4)
result=map(mul,num)      #map(function,sequence)    -  SYNDAX
print(list(result))

# num1=[1,2,3,4]
# num2=[5,6,7,8]
# result=map(lambda x,y:x+y,num1,num2)
# print(list(result))

num1=[1,2,3,4]
num2=[5,6,7,8]
result=map(lambda x,y:x+y,num1,num2)
print(list(result))

# Print length of each string in list.

fruits=['apple','orange','mango','banana','jackfruit']
result=map(len,fruits)
print(list(result))

# Print each letters as a list.

fruits=['apple','orange','mango','banana','jackfruit']
result=map(list,fruits)
print(list(result))


#  :::::::        Important        ::::::::


# Map
# Filter

# lst=[1,2,3,4,5]
# newlst=map(lambda x:x*x,lst)
# print(list(newlst))
#
# newlst1=filter(lambda x:x>2,lst)
# print(list(newlst1))