# Andrew Riker
# CS1400 - LW2 XL
# Assignment #08

# Add Import Statement(s) as needed ####
import pattern
# End Add Import Statement(s) ####


def main():
    # Setup pattern
    pattern.setup()

    # Play again loop
    playAgain = True

    while playAgain:
        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))

        # If they choose 'Rectangle Patterns'
        if mode == 1:
            # Add Input Statement(s) as needed ####
            centerX, centerY = eval(input("Enter the center point of pattern (x, y): "))
            offset = eval(input("Enter the offset desired for the pattern: "))
            width = eval(input("Enter the width of rectangle: "))
            height = eval(input("Enter the height of rectangle: "))
            count = eval(input("Enter the number of rectangles you would like in the pattern: "))
            rotation = eval(input("Enter the rotation of the rectangles in the pattern: "))

            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            # Add Input Statement(s) as needed ####
            centerX, centerY = eval(input("Enter the center point (x, y): "))
            offset = eval(input("Enter the offset desired: "))
            radius = eval(input("Enter the radius for the circles: "))
            count = eval(input("Enter the number of circles in the pattern: "))

            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            # Add Input Statement(s) as needed ####
            num = input("Enter number of patterns you would like: ")

            if num == "":
                pattern.drawSuperPattern()
            else:
                pattern.drawSuperPattern(eval(num))

        # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))

        # Add Statement(s) to clear drawings and play again ####
        if response == 2:
            pattern.reset()
        elif response == 3:
            playAgain = False

    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()
