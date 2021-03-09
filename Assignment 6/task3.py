# Andrew Riker
# CS1400 - LW2 XL
# Assignment #06
from random import seed
from random import randint
import time

# create start time
startTime = time.time()
# create counter for inner loop
isSeven = False
flukyNum = 0
count = 0

# outside loop for The Number (fluky number)
for i in range(1, 10001):
    randomSum = 0
    for j in range(1, i):
        count += 1

        if i % j == 0:
            seed(j)
            randomSum += randint(1, i)
        if randomSum < i:
            continue
        elif randomSum > i:
            break
    if randomSum == i:
        print("Fluky Number: " + str(randomSum))
        flukyNum += 1
    if flukyNum == 7:
        break


endTime = time.time()
totalTime = endTime - startTime


# print total time and iterations
print("Total Time: " + str(round(totalTime, 2)) + " seconds")
print("Total Loops: " + str(count))
