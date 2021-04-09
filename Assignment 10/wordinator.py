# Andrew Riker
# CS1400 - LW2 XL
# Assignment #10
import math


class Wordinator:
    def __init__(self, word):
        self.__word = word
        self.__length = len(word)

    # returns word
    def getWord(self):
        return self.__word

    # returns length of word
    def getLength(self):
        return self.__length

    # concatenates both words
    def __add__(self, other):
        # set variable as both words
        word = self.__word + other.getWord()
        # return new word but capitalized
        return word.capitalize()

    # returns str with other amount added
    def __mul__(self, other):
        return self.__word.upper() * other

    # returns 1 word that alternates characters from both words
    def __truediv__(self, other):
        # set variables
        len1 = self.__length
        len2 = other.getLength()
        secondWord = other.getWord()
        output = ""

        # check which word is longer
        if len1 > len2:
            # loop iterates as long as the second word
            for i in range(len2):
                # adding one character from first word and second until loop ends
                output += self.__word[i] + secondWord[i]
            # add the outstanding letters from first word to the end of new 'word'
            output += self.__word[i:]
        else:
            # loop iterates as long as first word
            for i in range(len1):
                # adds character from second word then first word until loop ends
                output += secondWord[i] + self.__word[i]
            # add outstanding letters from second word to end of new 'word' (if any)
            output += secondWord[i:]
        # returns new 'word' but capitalized
        return output.capitalize()

    # returns 2 words that is the middle portion of the original word
    def __mod__(self, other):
        # set all local variables
        startSpot1, startSpot2 = self.__length / 4, other.getLength() / 4
        midLength1, midLength2 = self.__length / 2, other.getLength() / 2
        endSpot1, endSpot2 = midLength1 + startSpot1, midLength2 + startSpot2
        word1, word2 = self.__word, other.getWord()
        str1, str2 = "", ""

        # outer loop iterates 2 times
        for i in range(1, 3):
            for x in range(round_half_up(startSpot1), round(endSpot1)):
                print(x)
                str1 += word1[x]
            # on second iteration it breaks so values stay
            if i == 2:
                break
            else:
                # swapping variable contents to store previous iteration
                str2, str1 = str1, str2
                word2, word1 = word1, word2
                startSpot2, startSpot1, endSpot2, endSpot1 = startSpot1, startSpot2, endSpot1, endSpot2
        # returns the middle 'word'
        return str2, str1

    # Returns two words in the opposite case they were entered in
    def __sub__(self, other):
        # setting variables needed
        str1, str2 = "", ""
        word1, word2 = self.__word, other.getWord()
        # checking which is longer
        if self.__length > other.getLength():
            dif = self.__length - other.getLength()
            # if first word is longer then we add the necessary spaces to make len equal
            word2 += " " * dif
        elif other.getLength() > self.__length:
            dif = other.getLength() - self.__length
            # same as last comment but for other word
            word1 += " " * dif

        # loop iterates 2 times
        for i in range(1, 3):
            for x in word1:
                if x.isupper():
                    str1 += x.lower()
                else:
                    str1 += x.upper()
            # on second loop it breaks before reassigning variables
            if i == 2:
                break
            else:
                # swapping variables
                str2, str1 = str1, str2
                word2, word1 = word1, word2
        return str2, str1

    # returns word when main() tries to print Wordinator object
    def __str__(self):
        # returns the word
        return self.__word

    # returns boolean (True if first word comes before other, false if not)
    def __lt__(self, other):
        # checks which word comes first alphabetically
        return self.__word < other.getWord()

    # returns word backward using Splice operator
    def backWordSlice(self):
        # iterated through the word backwards using slice operator
        backward = self.__word[:: -1]
        return backward

    # returns word backward without using splice operator
    def backWordManual(self):
        # set variables
        backward = ""
        # iterate through word using loop
        for i in self.__word:
            # put new letter before past letters
            backward = i + backward
        return backward


def round_half_up(num, decimal=0):
    multiply = 10 ** decimal
    return math.floor(num * multiply + 0.5) // multiply
