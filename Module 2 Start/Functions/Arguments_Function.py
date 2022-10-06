# def data(r,n):
#     print('Roll No :',r)
#     print('Name :',n)
# data('Ram',4)
# data(n='ram',r=4)                 #Keyword arguments


def studentdetails(r,n,d='BCA'):    #Default argument
    print('Roll No :',r)
    print('Name :',n)
    print('Department :',d)
studentdetails(34,'Ram')
studentdetails(2,'Syam','BSC')
studentdetails(1,'Athul','Mechanical')

#Variable length argument
# def fun1(*num):
#     print(type(num))
#     for i in num:
#         print(i)
# print('Call 1')
# fun1(10,20,30,40,50)
# print('Call 2')
# fun1(34,24,14,22,56)
