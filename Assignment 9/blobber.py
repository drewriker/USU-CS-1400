# Andrew Riker
# CS1400 - LW2 XL
# Assignment #09
import time
from math import pi


class Blobber:
    def __init__(self, name, color, radius, height):
        self.__name = name.capitalize()
        self.__color = color.lower()
        self.__RADIUS = radius
        self.__radius = radius
        self.__height = height
        self.__startVolume = pi * (radius ** 2) * height
        self.__time = time.time()

    def vitalsOK(self):
        self.__changeRadius()
        happyLevel = self.__happyPercent()
        print(happyLevel)
        if 0.9 <= happyLevel <= 1.1:
            blobberOK = True
        else:
            blobberOK = False
        return happyLevel, blobberOK

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name.capitalize()

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color.lower()

    def feedBlobber(self, food):
        self.__radius += food

    def blobberSpeak(self):
        happyLevel = self.__happyPercent()

        speak = "Hello Master! I am " + self.__name + ", and I am " + self.__color + "."
        speak += "\nMy current happiness level is " + str(format(happyLevel, ".2%"))

        return speak

    def __happyPercent(self):
        newVolume = (pi * (self.__radius ** 2) * self.__height) / self.__startVolume
        return newVolume

    def __changeRadius(self):
        endTime = time.time()
        timeDif = endTime - self.__time
        newRadius = self.__radius
        takeOff = self.__radius * 0.002

        for i in range(int(timeDif)):
            newRadius -= takeOff

        self.__radius = newRadius
        self.__time = time.time()
