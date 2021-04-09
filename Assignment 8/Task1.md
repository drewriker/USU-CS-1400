# Task 1
---
Starter: [task1-starter.zip](https://github.com/drewriker/USU-CS-1400/files/6283187/task1-starter.zip)

---
### Requirements
---
You will be submitting three files: task1.py (rename the starter code file), pattern.py, and plan1.txt. Use the assn4-task3-starter.py file to get started. Ignore the name of the starter code, it's correct, but named for the 7 week version of the class. You should add to this file in the areas indicated, but not modify any existing code. This should give insight to the function definitions you need to write. You need to watch the video demo get understand the full instructions.

You are going to create a program that draws cool patterns. The user will have three modes to choose from:

1. Rectangle Pattern - A circular pattern created by drawing multiple rectangles
1. Circle Pattern - A circular pattern created by drawing multiple circles
1. Super Pattern - A random selection of some number of Rectangle and Circle Patterns

---
### Coding Notes
---

1. task1.py - Use the starter file given and only fill in the appropriate areas. Do not modify any code that is there already, only add to it. This file will help you with defining the functions in pattern.py.
1. pattern.py - You must define the following functions
    * reset() - Erase all of the patterns and start over
    * setup()
        * Configure turtle to draw quickly
        * Configure turtle to have a window of 1000 x 800
    * drawRectanglePattern()
        * Use appropriate parameters
        * See additional information below
        * It should call drawRectangle()
    * drawRectangle()
        * Use appropriate parameters
        * Should draw a SINGLE rectangle
    * drawCirclePattern()
        * Use appropriate parameters
        * See additional information below
    * drawSuperPattern()
        * Use appropriate parameters
        * Randomly draw Rectangle and Circle patterns. Each pattern should based on random values.
        * Use reasonable random values (some can be negative) so patterns are drawn on the screen
    * setRandomColor()
        * Do not use any parameters
        * Set turtle to draw in a random color
        * Use at least 4 colors
    * done()
        * Called when user quits
        * Keeps the turtle window open

Make sure to read the rubric to see the additional requirements.

---
### Drawing Rectangle Pattern
---

The Rectangle Pattern has 6 parts to it

1. Center position - This is the x, y center point of the circular pattern that is drawn
1. Offset - This is the distance from the center position to the starting corner of each rectangle. It can be a positive or negative number
1. Height - The height of a rectangle
1. Width - The width of a rectangle
1. Count - The number of rectangles to draw within the 360 degree pattern.
1. Rotation - The number of degrees each rectangle is rotated in relation to the line from the Center Position to the starting corner of the rectangle

Each individual rectangle should be a new random color. You should use at least 4 different colors.

---
### Drawing Circle Pattern
---

The Circle Pattern has 4 parts to it

1. Center position - This is the x, y center point of the circular pattern that is drawn
1. Offset - This is the distance from the center position to starting drawing point of each circle.  It can be a positive or negative number. Note that the center point of each circle should be 'radius + offset' distance from the Center Position of the pattern.
1. Radius - The radius of the circle
1. Count - The number of circles to draw within the 360 degree pattern.

Each individual circle should be a new random color. You should use at least 4 different colors.

---
### Common Errors
---

* The rotation for the rectangle pattern is a common error. The rotation happens at the corner where drawing starts for the rectangle. Make sure to watch the video for a detailed explanation.
* The offset for the circle is frequently missed. Make sure you review what that means.
