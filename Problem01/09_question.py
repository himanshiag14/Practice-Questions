# Leap Year

year = int(input("ENter the Year"))

if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print("Leap year")
else:
    print("normal Year")