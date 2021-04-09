# Andrew Riker
# CS1400 - LW2 XL
# Assignment #08

# import statements
import turtle
from random import random
from random import randint


# function clears the screen
def reset():
    turtle.clear()


# function sets up the turtle screen and speed
def setup():
    turtle.speed(100)
    turtle.setup(1000, 800)
    turtle.hideturtle()


# function draws one rectangle
def drawRectangle(length, width):
    # calls randomColor
    setRandomColor()
    turtle.pd()

    # this for loop draws the sids of the rectangle
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    # make sure everything goes well after this function is called
    turtle.pu()


def drawRectanglePattern(x, y, offset, width, height, count, rotation=0):
    # calculate degree each rectangle is off by
    degree = 360 / count

    # for loop iterates the amount of count
    for i in range(count):
        # sets turtle up
        turtle.pu()
        turtle.goto(x, y)
        # sets heading by multiplying i and degree to increment each rectangle equally
        turtle.setheading(i * degree + rotation)
        # move from center point to starting point of rectangle
        turtle.forward(offset)

        # call drawRectangle function passing width and height
        drawRectangle(width, height)


def drawCirclePattern(x, y, offset, radius, count):
    # find distance from center on each circle
    distance = radius + offset
    # calculate degree each circle is off by
    degree = 360 / count

    # for loop iterates the amount of count
    for i in range(count):
        # set up for circle drawing
        turtle.pu()
        # go to center point
        turtle.goto(x, y)
        # set heading by incrementing by i
        turtle.setheading(i * degree)
        # move from center to starting point
        turtle.forward(distance)
        # call setRandomColor to set a random color
        setRandomColor()
        # draw circle
        turtle.pd()
        turtle.circle(radius)
        

def drawSuperPattern(numOfPatterns=5):
    # loops amount of patterns entered
    for i in range(numOfPatterns):
        # use mode to pick which pattern to choose (rectangle or circle)
        mode = random()
        # use randint to pick number for universal variables
        x = randint(-500, 500)
        y = randint(-400, 400)
        count = randint(2, 200)
        offset = randint(-100, 100)

        # if mode < .5 then rectangle pattern is chosen
        if mode < .5:
            # use randint to set other variables necessary
            height = randint(1, 100)
            width = randint(25, 200)
            rotation = randint(-50, 359)

            # call drawRectanglePattern and pass the needed variables
            drawRectanglePattern(x, y, offset, width, height, count, rotation)
        # if mode <= .5 then circle pattern is chosen
        else:
            # use randint to set radius
            radius = randint(2, 100)

            # call drawCirclePattern and pass needed variables
            drawCirclePattern(x, y, offset, radius, count)


def setRandomColor():
    mode = randint(1, 4)

    # if statements to choose color based on random number generated
    if mode == 1:
        turtle.color("green")
    elif mode == 2:
        turtle.color("blue")
    elif mode == 3:
        turtle.color("red")
    else:
        turtle.color("purple")


def done():
    # keep turtle drawing up
    turtle.done()
