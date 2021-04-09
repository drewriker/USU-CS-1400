from modules.blobber import Blobber


def main():
    name = input("Enter your Blobber's name: ")
    color = input("Enter your Blobber's color: ")
    radius = eval(input("Enter your Blobber's radius: "))
    height = eval(input("Enter your Blobber's height: "))

    myBlobber = Blobber(name, color, radius, height)

    done = False

    while not done:
        print()
        print("Main Menu")
        print("\t(1) Display Name")
        print("\t(2) Change Name")
        print("\t(3) Display Color")
        print("\t(4) Change Color")
        print("\t(5) Feed Blobber")
        print("\t(6) Blobber Speak")
        print("\t(7) Exit")

        # Display current vitals and check to see if it has turned to dust
        # This will catch cases where the Blobber was fed too much as well
        vitals, blobberOK = myBlobber.vitalsOK()
        print("Your Blobber is at " + format(vitals, ".2%") + " happiness")
        if not blobberOK:
            print("Your Blobber turned to dust")
            break

        choice = eval(input("Make a selection: "))
        print()

        # Check to see if the Blobber turned to dust while waiting for the user to make a selection
        vitals, blobberOK = myBlobber.vitalsOK()
        if not blobberOK:
            print("Your Blobber is at " + format(vitals, ".2%") + " happiness")
            print("Your Blobber turned to dust")
            break

        if choice == 1:
            displayName(myBlobber)
        elif choice == 2:
            changeName(myBlobber)
        elif choice == 3:
            displayColor(myBlobber)
        elif choice == 4:
            changeColor(myBlobber)
        elif choice == 5:
            feedBlobber(myBlobber)
        elif choice == 6:
            blobberSpeak(myBlobber)
        elif choice == 7:
            done = True

    print("Thanks for taking care of a Blobber")


def displayName(blobber):
    print("Your Blobber's name is " + blobber.getName())


def changeName(blobber):
    name = input("Enter Blobber's new name: ")
    blobber.setName(name)
    displayName(blobber)


def displayColor(blobber):
    print("Your Blobber's color is " + blobber.getColor())


def changeColor(blobber):
    color = input("Enter Blobber's new color: ")
    blobber.setColor(color)
    displayColor(blobber)


def feedBlobber(blobber):
    food = eval(input("Enter amount to you feed your Blobber: "))
    blobber.feedBlobber(food)


def blobberSpeak(blobber):
    print(blobber.blobberSpeak())


main()
