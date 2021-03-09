# Andrew Riker
# CS1400 - LW2 XL
# Assignment #05

import math

# print welcome statement
print("Welcome to the Social Situation Analyzer System")

# person 1 input
print("Person One")
person1Name = input("\tEnter your name: ")
x1Pos, y1Pos = eval(input("\tEnter your position (x, y): "))
person1Radius = eval(input("\tEnter your personal space radius: "))

# person 2 input
print("\nPerson Two")
person2Name = input("\tEnter your name: ")
x2Pos, y2Pos = eval(input("\tEnter your position (x, y): "))
person2Radius = eval(input("\tEnter your personal space radius: "))

# use distance formula to calculate if person 2 is in person 1 personal space
distance = math.sqrt(math.pow(x2Pos - x1Pos, 2) + math.pow(y2Pos - y1Pos, 2))

# create msg variable
msg = "\nSocial Situation Analysis Results\n"

# use if-elif-else to determine who is in what space
if distance <= person1Radius and distance <= person2Radius:
    msg += "\tPerson Test: " + person1Name + " and " + person2Name + " are in each other's personal space\n"
elif distance <= person2Radius:
    msg += "\tPerson Test: " + person1Name + " is in " + person2Name + "\'s personal space\n"
elif distance <= person1Radius:
    msg += "\tPerson Test: " + person2Name + " is in " + person1Name + "\'s personal space\n"
else:
    msg += "\tPerson Test: Neither " + person1Name + " nor " + person2Name + " is in the other's personal space\n"

# use if-elif-else to determine if circles overlap or are in each other
if distance < person1Radius - person2Radius:
    msg += "\tSpace Test: " + person2Name + " personal space is entirely inside " + person1Name + "'s personal space"
elif distance < person2Radius - person1Radius:
    msg += "\tSpace Test: " + person1Name + " personal space is entirely inside " + person2Name + "'s personal space"
elif distance > person1Radius + person2Radius:
    msg += "\tSpace Test: " + person1Name + " and " + person2Name + "'s personal spaces do not overlap"
else:
    msg += "\tSpace Test: " + person1Name + " and " + person2Name + "'s personal spaces overlap"

# print msg
print(msg)
