# HOME WORK
# n
# 1
# 2
# iam multiple of 3
# 4
# 5
# iam multiple of 3
# 7
# 8
# iam multiple of 3
# .
# .
# .
# .

n=int(input("Enter the limit :"))
for i in range(1,n+1):
    if i%3==0:
        print("iam multiple of 3")
    else:
        print(i)