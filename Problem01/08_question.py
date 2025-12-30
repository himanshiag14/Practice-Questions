# Password Generator

password = input("enter the no. of word ")

if len(password) < 6:
    mode = "Weak"
elif len(password) < 15:
    mode = "Medium"
else :
    mode = "Strong"

print(mode)


