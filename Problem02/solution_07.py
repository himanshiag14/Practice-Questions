#Validate the input



while True:
    n = int(input("Enter the number"))
    if n>0 and n<11:
        print("Thanks")
        break
    else:
        print("Try Again")