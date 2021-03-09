# Andrew Riker
# CS1400 - LW2 XL
# Assignment #05
from random import randint

# create random number
compInt = randint(1, 10)
# Welcome output
print("Welcome to the Guessing Game")
print("The Computer has picked a number from 1 - 10. Try to match it.")

# enter number (1-10)
userInt = eval(input("What number do you choose (1-10): "))

# find difference between userInt and compInt
if userInt > compInt:
    diff = userInt - compInt
else:
    diff = compInt - userInt

# create msg
msg = "You picked " + str(userInt) + ", and the actual number was " + str(compInt) + ".\n"

if diff == 0:
    msg += "Honored to play with you, Master"
elif diff == 1:
    msg += "You are a worthy opponent, Knight"
elif diff == 2:
    msg += "You have much to learn, Padawan"
elif diff == 3:
    msg += "Youngling, your time will come."
else:
    msg += "Keep working hard in the Service Corps"

# print msg
print(msg)
