# Andrew Riker
# CS1400 - LW2 XL
# Assignment #03
import turtle

# enter location for target
xPos = eval(input("Enter the X position: "))
yPos = eval(input("Enter the Y position: "))
# enter diameter of desired bullseye
radius = eval(input("Enter the radius of desired target: "))
RADIUS = radius
Y_POS = yPos

turtle.speed(20)

# draw first target
turtle.pu()
radius *= 3
yPos -= radius
turtle.goto(xPos, yPos)
turtle.begin_fill()
turtle.color("black")
turtle.pd()
radius = RADIUS
radius *= 4
turtle.circle(radius)
turtle.end_fill()

# draw second layer
radius = RADIUS
yPos = Y_POS
turtle.pu()
turtle.begin_fill()
turtle.color("blue")
radius *= 2
yPos -= radius
turtle.goto(xPos, yPos)
radius = RADIUS
radius *= 3
turtle.circle(radius)
turtle.end_fill()

# draw third layer
radius = RADIUS
yPos = Y_POS
turtle.pu()
turtle.begin_fill()
turtle.color("red")
yPos -= radius
turtle.goto(xPos, yPos)
radius = RADIUS
radius *= 2
turtle.circle(radius)
turtle.end_fill()

# draw fourth layer
radius = RADIUS
yPos = Y_POS
turtle.pu()
turtle.begin_fill()
turtle.color("yellow")
turtle.goto(xPos, yPos)
turtle.circle(radius)
turtle.end_fill()

# tidy up
turtle.hideturtle()
turtle.done()