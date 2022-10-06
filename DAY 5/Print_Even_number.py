#Check a given number is even
# 0 1 2 3 4 5
# 0 1 0 1 0 1 (reminders when the numbers are divided by 2) (modulus operator)
#if n%2==0 -> even number
#if n%2==1 -> odd number    ( == -> comparison operator )

n=int(input('Enter the number : '))
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")