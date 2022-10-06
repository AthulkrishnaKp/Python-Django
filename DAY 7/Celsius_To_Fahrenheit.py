#Temperature conversion
#Celcius to fahrenheit
#Farenheit to celcius

# c=int(input("Enter the temperature in Celsius : "))
# f=c*(9/5)+32
# print(f,"fahrenheit")

print("1. Celcius to Fahrenheit. ")
print("2. Fahrenheit to Celcius. ")
n=int(input("Enter your choice :"))
if n==1:
    c=float(input("Enter the Temperature in Celcius :"))
    f=c*(9/5)+32
    print(round(f,2),"Degree Fahrenheit",)
elif n==2:
    f=float(input("Enter the Temperature in Fahrenheit :"))
    c=(f-32)*(5/9)
    print(round(c,2),"Degree Celcius",)
else:
    print("Invalid input")
