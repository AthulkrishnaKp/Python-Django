#Nested loop

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()





# 0 0 0
# 1 1 1
# 2 2 2

# for i in range(3):
#     for j in range(3):
#         print(i,end=" ")
#     print()





# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
#
# for i in range(5):
#     for j in range(5):
#         print(i+1,end=" ")
#     print()



# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4

# for i in range(5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# 1
# 2 2
# 3 3 3
# 4 4 4 4

# for i in range(4):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()

# *
# * *
# * * *
# * * * *

# for i in range(4):
#     for j in range(i+1):
#         print("*",end=" ")
#     i=i+1
#     print()

#    *
#   * *
#  * * *
# * * * *

#n=4
n=int(input("Enter the limit: "))

for i in range(n):
    for k in range(n-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=" ")

    # i=i+1
    print()

 #    1
 #   2 3
 #  4 5 6
 # 7 8 9 10

# n=int(input("Enter the limit: "))
# a=1
# for i in range(n):
#     for k in range(n-i-1):
#         print(end=" ")
#     for j in range(i+1):
#         print(a,end=" ")
#         a=a+1
#     i=i+1
#     print()