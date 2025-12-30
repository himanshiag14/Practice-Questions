#Grade Calculator

marks = int(input("Enter the marks: "))
    

if marks <= 100 and marks > 90:
    print("A")
elif marks < 91 and marks > 80:
    print("B")
elif marks < 81 and marks > 70:
    print("C")
elif marks < 71 and marks > 60:
    print("D")
else :
    print("F")