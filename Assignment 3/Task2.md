Save your program in a file called task2.py. Write a program that draws a target, such as one that would be used in archery. Ask the user for input for the location of the center of the target, as well as the diameter of the bullseye (center yellow) circle. Your target should have four circles, each one a different color. Make each larger circle have a radius that is larger than the next smallest circle by the amount of the radius of the bullseye. You can assume that the user will only enter valid non-negative numbers.

Use augmented operators in your program to modify variables xPos, yPos, and radius. To move the turtle to a new position you may only use the following line of code:

    turtle.goto(xPos, yPos)

To draw a circle you may only use the following line of code:

    turtle.circle(radius)
