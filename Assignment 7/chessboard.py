# Andrew Riker
# CS1400 - LW2 XL
# Assignment #7
import turtle


# function drawRectangle to draw a single black rectangle
def drawRectangle(length, height):
    # draw the rectangle
    turtle.color("black")
    turtle.pd()
    turtle.setheading(0)
    # for loop for each side
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.pu()


# function drawAllRectangles to draw the entire colored squares on board
def drawAllRectangles(xPos, yPos, width, height):
    # calculate length and height of each black rectangle with (width / 8)
    length = width / 8
    newHeight = height / 8

    X_POS = xPos
    Y_POS = yPos

    # incrementation of black rectangles
    lenInc = length * 2
    heightInc = newHeight * 2

    turtle.pu()
    turtle.goto(xPos, yPos)
    # start loop for rectangles
    for i in range(1, 5):
        for j in range(1, 5):
            drawRectangle(length, newHeight)
            xPos = X_POS + (lenInc * j)
            turtle.goto(xPos, yPos)
        yPos += heightInc
        turtle.goto(X_POS, yPos)

    # set new xPos and yPos for off center rows
    X_2_Pos = X_POS + length
    Y_2_POS = Y_POS + newHeight
    yPos = Y_2_POS
    # off center rectangle rows
    turtle.goto(X_2_Pos, Y_2_POS)
    for x in range(1, 5):
        for a in range(1, 5):
            drawRectangle(length, newHeight)
            xPos = X_2_Pos + (lenInc * a)
            turtle.goto(xPos, yPos)
        yPos += heightInc
        turtle.goto(X_2_Pos, yPos)


# function called drawChessboard
def drawChessboard(xPos, yPos, width=250, height=250):
    # set speed, and go to starting spot
    turtle.speed(20)
    turtle.hideturtle()
    turtle.pu()
    turtle.goto(xPos, yPos)
    turtle.color("red")
    turtle.pd()
    # for loop for the box
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.pu()

    # use drawAllRectangles
    drawAllRectangles(xPos, yPos, width, height)
    turtle.done()

