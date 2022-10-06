# year=int(input("Enter the year :"))
# if year%4==0:
#     if year%100!=0:
#          print(year,"is a Leap year")
#     elif year%100==0 and year%400==0:
#          print(year,"is a leap year")
#     else:
#      print(year, "not a leap year")
# else:
#     print(year,"not a Leap year")

year = int(input("Enter the year :"))
if year%4==0 and year%100!=0:
    print(year, "is a Leap year")
elif year%100 == 0 and year%400==0:
    print(year, "is a leap year")
else:
    print(year, "not a Leap year")