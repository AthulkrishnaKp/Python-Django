#Count the number of vovels in a string.

str=input("Enter the String :")
str1=str.lower()
print("Count of a :",str1.count('a'))
print("Count of e :",str1.count('e'))
print("Count of i :",str1.count('i'))
print("Count of o :",str1.count('o'))
print("Count of u :",str1.count('u'))
count=0
for i in str:
    if i in "aeiouAEIOU":
        count+=1
print("Count of vowels =",count)
