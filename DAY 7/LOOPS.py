#Loops - for,while

# for iterating variable in range(start,stop,step):
#     Body of the loop

# for i in range(1,5):      #i=1  i=2  i=3  i=4    steps=1
#     print('Hai')          #Hai  Hai  Hai  Hai
#
# for i in range(1,5,2):    #i=1  i=3(i=i+2)       steps=2
#     print('Hai')          #Hai  Hai
#
# for i in range(5):        # i=0  i=1  i=2  i=3  i=4
#     print('Hai')          # Hai  Hai  Hai  Hai  hai

# for i in range(5):
#     print(i)
#
# for i in range(5):          # end=" " - print in same line with space
#     print(i,end=" ")

#even numbers

# for i in range(2,10,2):
#     print(i)

#sum of even number till 10

sum = 0
for i in range(2,10,2):  #i=2         i=4        i=6         i=8
    print(i)             #2           4          6           8
    sum=sum+i            #sum=0+2=2   sum=2+4=5  sum=6+6=12  sum=12+8=20
print("Sum is",sum)


# n=int(input("Enter a number : "))
# sum=0
# for i in range(2,n,2):  #i=2         i=4        i=6         i=8
#     print(i)              #2           4          6           8
#     sum=sum+i             #sum=0+2=2   sum=2+4=5  sum=6+6=12  sum=12+8=20
# print("Sum is",sum)