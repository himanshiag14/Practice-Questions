# Movie Ticket pricing

age = int(input("Enter your age"))
day = input("Enter the day")

if age<18:
    print("$8")
else:
    print("$12")

# price = 12 if age>18 else 8

if day == "Wednesday" :
    price = price - 2

print(price)