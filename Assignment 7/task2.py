# Andrew Riker
# CS1400 - LW2 XL
# Assignment #7

# Add Import Statement(s) as needed
from chessboard import drawChessboard


def main():
    # Add Code to get input from user
    startX, startY = eval(input("Enter the starting coordinates (x, y): "))
    width = input("Enter the desired width of the chessboard: ")
    height = input("Enter the desired height of the chessboard: ")

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()
