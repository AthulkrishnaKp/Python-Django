
#Logical operators ( and , or , not )

print(10>5 and 10>5)  #True True     True
print(10>5 and 10<5)  #True False    False
print(10<5 and 10>5)  #False True    False
print(10<5 and 10<5)  #False False   False

print(10>5 or 10>5)  #True True     True
print(10>5 or 10<5)  #True False    True
print(10<5 or 10>5)  #False True    True
print(10<5 or 10<5)  #False False   False

print(not 10>5)  #False
print(not 10<5)  #True


