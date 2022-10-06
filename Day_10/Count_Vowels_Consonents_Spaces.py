#Input a string
#Count vowels,space,consonents

str=input("Enter the String :")
str1=str.lower()
v=s=c=d=0
for i in str:
    if i in "aeiou":
        v+=1
    elif i in"0123456789":
        d+=1
    elif i==" ":
        s+=1
    else:
        c+=1
print("Count of vowels =",v)
print("Count of Digits =",d)
print("Count of spaces =",s)
print("Count of consonants =",c)
