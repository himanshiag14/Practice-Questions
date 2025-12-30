#Age Group Categorization

age  = int(input("Enter your age: "))

if age < 13:
    print("you are child")
elif age >= 13 and age < 20:
    print("You are teenager")
elif age >=20 and age < 60:
    print("You are adult")
else:
    print("You are senior citizen")