# Exception - abnormal errors occurs during execution of programs.

# a=int(input("Enter the number : "))
# b=int(input("Enter the number : "))
# div=a/b   # if b=0 it shows error its exception error." Zero division error "
# print(div)

# a=int(input("Enter the number : "))
# b=int(input("Enter the number : "))
# try:          #Suspected code.
#     div=a/b
#     print(div)
# except:       #Code for handling exception errors.
#     print("Not give 0 as second number")


# a=int(input("Enter the number : "))
# b=int(input("Enter the number : "))
# try:
#     c=a/b
#     print(c)
# except:
#     b=b+1
#     c=a/b
#     print(c)

# a=int(input("Enter the number : "))
# b=int(input("Enter the number : "))
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Not give 0 as second number ")
# except ValueError:
#     print("You must enter a number ")
# except:
#     print("all other errors handle errors ")
# else:
#     print(c)
#     print("Execute if there is no errors")

# a=int(input("Enter the number : "))
# b=int(input("Enter the number : "))
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Not give 0 as second number ")
# except ValueError:
#     print("You must enter a number ")
# except:
#     print("all other errors handle errors ")
# finally:
#     print("Always execute")

try:
    a=int(input("Enter the number : "))
    b=int(input("Enter the number : "))
    c=a/b
    print(c)
except (ZeroDivisionError,ValueError):
    print("Handle both value error & Zero division error")
except:
    print("all other errors handle errors ")
finally:
    print("Always execute")