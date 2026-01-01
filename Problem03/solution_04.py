# create a function that return both the area and circumfrence of a circle given its radius

import math

# def area(r):
#    return math.pi*r*r

# def circumfrence(r):
#    return 2*math.pi*r

# radius = circumfrence(3)
# radius2 = area(2)

# print(radius," " ,radius2)

def calc(r):
    Area = math.pi*r*r
    Circumfrence = 2*math.pi*r
    return Area,Circumfrence

a,c = calc(3)
print("Area is ",round(a,2)," and Circumfrence is ",round(c,2))