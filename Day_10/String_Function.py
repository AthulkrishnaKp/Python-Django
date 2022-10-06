# STRING FUNCTION

str1='i like python'
print(str1.capitalize())  #First letter of string capitalize.
print(str1.title())       #Capitalize first character in each word.
print(str1.upper())       #Full letters capitalizes.
str2='HELLO WORLD'
print(str2.lower())       #Upper case to lower call fully.
b='Hai Students'
print(b.swapcase())       #Capital letters become lower case and lower case become capital letters.
print(len(str1))
print(len(str2))
print(len(b))
print(str2.isupper())     #True all letters are upper case.
print(str1.isupper())
print(b.islower())        #False all letters are not lower case.
print(str1.islower())     #True all letters is lower case.
c='@@hai@@@'
print(c.rstrip('@'))      #RIGHT STRIP = right side strips.
print(c.lstrip('@'))      #LEFT STRIP = left side strips.
print(c.strip('@'))

print(c.count('@'))   #Count the letters and give result.
print(str2.count('L',0,5))  #('character',start,end)  from start to end counts how many given characters are there.

