# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     i=i+1
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     i=i+1
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(5):
#     for j in range(5-i):
#         print("*",end=" ")
#     i=i+1
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10

# c = 0
# for i in range(5):
#      for j in range(1,i+1):
#          c=c+1
#          print(c,end=" ")
#      i=i+1
#      print()

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# # for i in range(1,6):
# #     for j in range(0,6-i):
# #         print(i,end=" ")
# #     i=i+1
# #     print()

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

for i in range(5):
    for j in range(1,i+2):
        print(j,end=" ")
    i=i+1
    print()

