#check a prime number

n = int(input("Enter a number"))

# if n ==1 or n==2:
#     print("No Prime")

# if(n%7==0):
#     print("Number is prime")
# else:
#     print("not Prime")

is_Prime = True
if n>1:
    for i in range(2,n):
        if n%i==0 :
            is_Prime = False
            break
print(is_Prime)