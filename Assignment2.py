# Andrew Riker
# CS1400 - LW2 XL
# Assignment #002
import turtle
turtle.speed(0)

# set background blue and size
turtle.screensize(400, 400, "light blue")

# head of snow man
turtle.pu()
turtle.goto(0, 60)
turtle.begin_fill()
turtle.fillcolor("white")
turtle.pd()
turtle.circle(60)
turtle.end_fill()

# middle part of snowman
turtle.pu()
turtle.goto(0, -80)
turtle.pd()
turtle.begin_fill()
turtle.fillcolor("white")
turtle.circle(80)
turtle.end_fill()

# bottom part
turtle.pu()
turtle.goto(0, -250)
turtle.begin_fill()
turtle.fillcolor("white")
turtle.pd()
turtle.circle(100)
turtle.end_fill()

# hat position
turtle.pu()
turtle.goto(-50, 170)

# start hat
turtle.begin_fill()
turtle.fillcolor("purple")
turtle.forward(100)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.end_fill()

# outline hat
turtle.pu()
turtle.pensize(3)
turtle.goto(-50, 170)
turtle.setheading(0)
turtle.pd()
turtle.color("blue")
turtle.forward(100)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)

# button 1
turtle.pu()
turtle.color("red")
turtle.goto(0, 50)
turtle.setheading(0)
turtle.pd()
turtle.begin_fill()
turtle.circle(10)
turtle.pu()
turtle.end_fill()

# button 2
turtle.goto(0, 0)
turtle.pd()
turtle.begin_fill()
turtle.circle(10)
turtle.pu()
turtle.end_fill()

# button 3
turtle.goto(0, -50)
turtle.pd()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# move to eye position
turtle.color("black")
turtle.pu()
turtle.goto(-20, 130)

# draw eye 1
turtle.pd()
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()

# move to eye 2
turtle.pu()
turtle.goto(20, 130)

# draw eye 2
turtle.pd()
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()

# move to smile
turtle.pu()
turtle.pencolor("pink")
turtle.goto(-30, 100)
turtle.setheading(315)

# draw smile
turtle.pd()
turtle.width(10)
turtle.circle(40, 90)

# move to arms
turtle.pu()
turtle.setheading(0)
turtle.goto(65, 10)

# draw arm
turtle.pd()
turtle.pencolor("brown")
turtle.forward(50)
turtle.forward(20)
turtle.backward(20)
turtle.setheading(30)
turtle.forward(20)
turtle.backward(20)
turtle.setheading(-30)
turtle.forward(20)


# move to second arm
turtle.pu()
turtle.setheading(180)
turtle.goto(-65, 10)

# draw second arm
turtle.pd()
turtle.forward(50)
turtle.forward(20)
turtle.backward(20)
turtle.setheading(210)
turtle.forward(20)
turtle.backward(20)
turtle.setheading(150)
turtle.forward(20)

# cleanup
turtle.hideturtle()
turtle.done()
