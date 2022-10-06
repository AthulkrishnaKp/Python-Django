# def sum(a,b):          #a=5,b=10
#     c=a+b              #c=15
#     return c           #Return statement
# s=sum(5,10)            #s=15
# avg=s/2                #avg=s/2
# print("Average",avg)


def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
m,n,o,p=calc(5,10)
print("Sum is ",m)
print("difference is ",n)
print("product is ",o)
print("Quotient is ",p)