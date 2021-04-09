# Task 2 - Chessmate
---
Starter: [task2-starter.zip download](https://github.com/drewriker/USU-CS-1400/files/6283120/task2-starter.zip)


---
### Requirements
---
You will be submitting three files: task2.py (rename the starter code file), chessboard.py, and plan2.txt. You will draw a chessboard based on user inputs. You will ask for the starting location (x, y) and a height and width of the board. You will use this information to draw the chessboard (just a single chessboard). Keep in mind that it may not be a square. The location is the bottom left corner of the chessboard.

The user must enter the location, but if they do not enter a value for height or width you will use a default value of 250. Note, that input() returns an empty string(“”) if the user just hits enter without giving input. Here is some code that you must use in your program. It should be placed in a main() function.

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))

---
### Coding Notes
---
* The Software Development Plan will change slightly now that we are using functions. You will write an individual design for each function. Then in your main design (where the program starts) you will note where those functions are called.
* Use the assn4-task2-starter.py file to get started. You should add to this file in the areas indicated, but not modify any existing code. This should give insight to the drawChessboard() function definition you need to write.
* Note how the user's input is validated in the starter code. Make sure you're getting input properly so it matches how the existing code will use what is input from the user.
* DO NOT modify the starter code in assn4-task2-starter.py, only add code where indicated.
* Create a module in a file called chessboard.py. This contains all functions associated with drawing the chessboard.
    * Do not use global variables in this file
    * Define drawChessboard() with appropriate parameters
        * This function should draw the outline of the board, then call drawAllRectangles()
    * Define drawAllRectangles() with appropriate parameters
        * This should handle drawing all of the black rectangles by calling drawRectangle()
        * Note: It may be easiest to call this function twice, but not required
    * Define drawRectangle() with appropriate parameters
        * This should draw a single black rectangle
        * This function will be called many times with a loop!

Make sure to read the rubric to see all requirements.

---
### Common Errors
---
* The first of the two most common errors is one that really shouldn't be a problem. DO NOT modify the starter code except where indicated. It's actually pretty surprising at how many students modify the code because they think there's an error.
* The code in the shaded box above is very important to understand. You must write code that will work with that code. Review default parameters if you're having problems.
