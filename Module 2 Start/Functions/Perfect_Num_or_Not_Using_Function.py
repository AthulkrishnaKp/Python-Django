#Check a given number is a perfect number or not
#6=1+2+3=6 -  perfect.    (Sum of factors equals the number)
#8=1+2+4=7 -  not perfect.

def perfect(n):
    num=n
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==num:
        print(n,"is a Perfect number")
    else:
        print(n,"is not a Perfect number")

perfect(128)
perfect(496)
perfect(28)
perfect(6)
perfect(8)