#1.
str=input("Enter the string :")
str1=0
count=1
for i in range(len(str)):
    if str[i]==" ":
        count+=1
print("Number of Words : ",count)

#2.
str=input("Enter the string :")
str1=str.lower()
space=str1.count(" ")
print("Number of Words",space+1)