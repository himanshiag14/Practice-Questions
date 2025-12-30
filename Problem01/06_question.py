#Distance

Distance = int(input("Enter the Km"))

if Distance < 3:
    mode = "walk"
elif Distance < 15:
    mode = "Bike"
else:
    mode = "Car"

print(mode)