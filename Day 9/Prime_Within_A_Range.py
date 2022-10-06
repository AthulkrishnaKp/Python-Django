a=int(input("Enter lower limit: "))
b=int(input("Enter upper limit: "))
for i in range(a,b):        #50        #51 #52 #53
    for j in range(2,i-1):  #2.....49          #2.....52
        if i%j==0:          #50%2==0           #53%2==0 (not satisfy)
            break           #break             #go to else
    else:                                      #print(53)
        print(i,end=" ")

#Home work
# Menu
# 1. Addition
# 2. subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# enter your choice
# enter num1
# enter num2
# result
# enter your coice if 5
# exit
# while true choice 5 break