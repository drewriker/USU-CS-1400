# Andrew Riker
# CS1400 - LW2 XL
# Assignment #11

from math import pi
# from random import shuffle  # Hint hint
from random import randint
import time


class Orbian:
    # DO NOT MODIFY THE CONSTRUCTOR
    def __init__(self, name, headRadius, bodyRadius, bodyHeight):
        # NOTE: These are constants
        self.__HEAD_RADIUS = headRadius
        self.__BODY_RADIUS = bodyRadius
        self.__BODY_HEIGHT = bodyHeight
        self.__NAME = name
        self.__BIRTH_TIME = time.time()

        # This is the only variable
        self.__adult = False

    def __getHeadVolume(self):
        return 4 / 3 * pi * self.__getHeadRadius() ** 3

    def __getBodyVolume(self):
        return pi * self.__getBodyRadius() ** 2 * self.__getBodyHeight()

    def __ageCheck(self):
        # Become an adult at 2
        if self.getAge() >= 2:
            self.__adult = True

    # private module to get the correct body radius
    def __getBodyRadius(self):
        # call the age check module to update the Objects age
        self.__ageCheck()
        # check if Object is an 'adult'
        if not self.__adult:
            # not 'adult' get constant
            return self.__BODY_RADIUS
        else:
            # if 'adult' get new body radius
            return self.__BODY_RADIUS * 2

    # private module to get the correct body height
    def __getBodyHeight(self):
        # do age check
        self.__ageCheck()
        # if not 'adult'
        if not self.__adult:
            # return constant body height
            return self.__BODY_HEIGHT
        # if 'adult'
        else:
            # return new body height
            return self.__BODY_HEIGHT * 4

    # private module to get correct head radius
    def __getHeadRadius(self):
        # age check
        self.__ageCheck()
        # if Object is not 'adult'
        if not self.__adult:
            # return constant head radius
            return self.__HEAD_RADIUS
        # if Object is 'adult'
        else:
            # return new head radius
            return self.__HEAD_RADIUS * 2

    # public module to get the age of Object
    def getAge(self):
        ageTime = time.time() - self.__BIRTH_TIME
        # return time divided by 5 because each 'year' is 5 seconds
        return int(ageTime // 5)

    # public module to get total volume of Object
    def getVolume(self):
        # return head volume plus body volume
        return round(self.__getHeadVolume() + self.__getBodyVolume())

    # public module to get name of Object
    def getName(self):
        # return constant name
        return self.__NAME

    # Operator overloading string
    def __str__(self):
        # returns the name of the Object
        return self.__NAME

    # operator overloading >
    def __gt__(self, other):
        # checks which object total volume is greater
        if self.getVolume() > other.getVolume():
            # if first object is greater, return True
            return True
        else:
            # if the objects are equal or other is greater, return False
            return False

    # operator overloading =
    def __eq__(self, other):
        # checks if objects volumes are equal
        if self.getVolume() == other.getVolume():
            # if they are equal, return True
            return True
        else:
            # if not, return False
            return False

    # operator overloading +
    def __add__(self, other):
        # get combination of both Object names
        combName = self.__NAME + other.getName()
        # get the baby name length by averaging the two name lengths
        nameLength = len(combName) // 2
        # starter variable for the loop
        babyName = ""
        # for loop iterating the number of times the baby's name will be
        for i in range(nameLength):
            # get a random number between 0 and combination of both names
            num = randint(0, len(combName) - 1)
            # use the random number to get new name
            babyName += combName[num]
        # get baby dimensions from both 'parents'
        headRadius = round((self.__getHeadRadius() + other.__getHeadRadius()) * 0.25)  # 25% of sum
        bodyRadius = round((self.__getBodyRadius() + other.__getBodyRadius()) * 0.25)  # 25% of sum
        bodyHeight = round((len(self) + len(other)) * 0.125)  # 12.5% of sum
        # return new Object
        return Orbian(babyName.capitalize(), headRadius, bodyRadius, bodyHeight)

    # operator overloading len()
    def __len__(self):
        # return the total height of the Object
        return self.__getBodyHeight() + (self.__getHeadRadius() * 2)
