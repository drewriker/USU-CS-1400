from modules.wordinator import Wordinator


def main():
    print("Welcome to the Wordinator")
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    wordinator1 = Wordinator(word1)
    wordinator2 = Wordinator(word2)

    done = False

    while not done:
        print()
        print("Menu")
        print("\t1) First Word")
        print("\t2) Big Word")
        print("\t3) Words Factor")
        print("\t4) Mix Words")
        print("\t5) Middle Words")
        print("\t6) Switched Case Words")
        print("\t7) Back Words Sliced")
        print("\t8) Back Words Manual")
        print("\t9) Quit")
        mode = int(input("Enter Selection: "))
        print()

        if mode == 1:
            firstWord(wordinator1, wordinator2)
        elif mode == 2:
            bigWord(wordinator1, wordinator2)
        elif mode == 3:
            wordFactor(wordinator1, wordinator2)
        elif mode == 4:
            mixWords(wordinator1, wordinator2)
        elif mode == 5:
            midWords(wordinator1, wordinator2)
        elif mode == 6:
            switchCaseWords(wordinator1, wordinator2)
        elif mode == 7:
            backWordsSlice(wordinator1, wordinator2)
        elif mode == 8:
            backWordsManual(wordinator1, wordinator2)
        elif mode == 9:
            done = True


def firstWord(wordinator1, wordinator2):
    print("The first word is " + str(min(wordinator1, wordinator2)))


def bigWord(wordinator1, wordinator2):
    print("The Big Word is " + (wordinator1 + wordinator2))


def wordFactor(wordinator1, wordinator2):
    factor = int(input("Enter an integer factor: "))
    word1 = wordinator1 * factor
    word2 = wordinator2 * factor
    print("Word factor one is " + word1)
    print("Word factor two is " + word2)


def mixWords(wordinator1, wordinator2):
    print("The mixed word is " + (wordinator1 / wordinator2))


def midWords(wordinator1, wordinator2):
    word1, word2 = wordinator1 % wordinator2
    print("Midword One is " + word1)
    print("Midword Two is " + word2)


def switchCaseWords(wordinator1, wordinator2):
    word1, word2 = wordinator1 - wordinator2
    print("Switch case one is " + word1)
    print("Switch case two is " + word2)


def backWordsSlice(wordinator1, wordinator2):
    word1 = wordinator1.backWordSlice()
    word2 = wordinator2.backWordSlice()
    printBackWords(word1, word2)


def backWordsManual(wordinator1, wordinator2):
    word1 = wordinator1.backWordManual()
    word2 = wordinator2.backWordManual()
    printBackWords(word1, word2)


def printBackWords(word1, word2):
    print("Backwords one is " + word1)
    print("Backwords two is " + word2)


main()
