#read mark of 3 subjects out of 100
#(total mark/300)*100
#percentage calculate
#>=80% print grade A
#60<>=79 grade b
#50-59% grade c
#40-495 grade d
#below 40 failed
sub1=int(input("Enter mark in sub 1 is :"))
sub2=int(input("Enter mark in sub 2 is :"))
sub3=int(input("Enter mark in sub 3 is :"))
if sub1<=100 and sub2<=100 and sub3<=100:
    per=((sub1+sub2+sub3)/300)*100
    print("Persentage of mark is :",per)
    if per>=80:
        print("RESULT = GRADE A")
    elif per>=60 and per<80:
        print("RESULT = GRADE B")
    elif per>=50 and per<60:
        print("RESULT = GRADE C")
    elif per>=40 and per<50:
        print("RESULT = GRADE D")
    else:
        print("RESULT = FAILED")
else:
    print("WRONG MARK")