#RECURSION

# A function call by itself is called Recursion.

# Factorial of a number using Recursion

def fact(n):                  #4
    if n==1:
        return 1
    else:
        return n*fact(n-1)    #4*fact(3)
                              #4*3*fact(2)
print(fact(4))                #4*3*2*fact(1)
                              #4*3*2*1 = 24

#Sum of n Natural numbers using Recursion

def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(4))