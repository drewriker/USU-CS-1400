# Andrew Riker
# CS1400 - LW2 XL
# Assignment #06

from random import randint

# declare variables
continueSim = True

# while continueSim the simulation will run again
while continueSim:
    oneEl, twoEl = 0, 0
    # for loop iterates 100,000 times for simulation
    for i in range(1, 100001):
        el1, el2, zookeeper = 0, 0, 0
        el1 = randint(1, 6)
        el2 = randint(1, 6)
        zookeeper = randint(1, 6)

        # check if zookeeper saw elephants in pen
        if zookeeper == (el1 and el2):
            oneEl += 1
            twoEl += 1
        elif zookeeper == (el1 or el2):
            oneEl += 1
    # get percentages of zookeeper seeing one elephant
    oneInPen = (oneEl / 100000)
    # percent of two elephants in checked pen
    twoInPen = ((twoEl / 100000) / oneInPen)
    oneInPen *= 100
    twoInPen *= 100

    # output the percentages
    print("\nThere was a " + str(round(oneInPen, 2)) + "% chance that at least one elephant"
                                                       " was in the pen the zookeeper checked")
    print("There was a " + str(round(twoInPen, 2)) + "% chance that two elephants"
                                                     " were in the pen the zookeeper checked")
    # check if zookeeper was correct
    if (oneInPen >= ((1 / 3) - 0.02)) and oneInPen <= ((1 / 3) + 0.02):
        print("The zookeeper was correct")
    else:
        print("The custodian was correct")

    # check if user wants to run again
    runAgain = input("\nRun the simulation again? (yes or no)")
    runAgain = runAgain.upper()
    # make continueSim true or false based on user input
    if runAgain == "YES":
        print("Running simulation again")
        continueSim = True
    else:
        print("Thank you for using my simulation!")
        continueSim = False
