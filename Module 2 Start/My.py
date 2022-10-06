str=input("Enter the string : ")
a=int(input("Enter the index to be removed : "))
c=str[a]
print(str[0:str.index(c)]+str[str.index(c)+1:])