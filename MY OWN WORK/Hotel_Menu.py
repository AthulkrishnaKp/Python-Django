Menu={1:'Tea',2:'Coffee',3:'Dosa',4:'Vada',5:'Idli'}
print(Menu)
ch=int(input("Enter your choice: "))
if ch<=0 or ch>5:
    print("Invalid choice")
else:
    print("Your have ordered :",Menu[ch])

# list=[1,2,3,4,5]
# list.append(10)
# print(list)