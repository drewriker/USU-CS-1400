# Andrew Riker
# CS1400 - LW2 XL
# Assignment #04
import math

# user enters length of sides
length = eval(input("Enter length of the polygon sides: "))
# user enters number of sides
numOfSides = eval(input("Enter the number of sides the polygon has: "))

# calculate the area of the polygon
area = (numOfSides * math.pow(length, 2)) / (4 * (math.tan(math.pi / numOfSides)))

# print the area of polygon
print("The area of the polygon is:", str(round(area, 5)))
