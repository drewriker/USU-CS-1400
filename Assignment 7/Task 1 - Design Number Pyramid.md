---
# Task 1 - Design Number Pyramid
---
For this task you will be creating a design for a single function only. You will not write a program. Save your design in a file called task1.txt. Your design will be based on the following requirements specification. This requirements specification is pretty detailed to help you catch all of the details you'll need to account for in your design.

---
#### Requirements Specification
---
The user will enter the number of rows to have in a pyramid of numbers. Based on the user's input the program will display a pyramid where each row contains the number x, which is printed x times, where x is the row number. There is a space between each number on the rows. The top row's value is always 1, and the bottom row's value is the number given from the user. Each row is centered in a space equal to the length of the bottom row.

---
#### Notes
---
1. On the bottom row there shouldn't be any space before the first number or after the last
1. If the number of rows goes past 10 there is a ledge in the pyramid. You don't need to space the single digit numbers to span the width. Just one space between each number.
1. Use the len() function to determine the number of digits in a number. This will come in handy in calculating something you need.
1. You are designing a function, not the whole program (even though the function is the bulk of the program). Your function takes a single parameter which is the number of rows. It returns a string which can then be printed by the caller of the function.
1. The first step in your design should be: create formal parameter to get the number of rows from caller of the function
1. The last step in your design should be: return the pyramid string to the caller of the function
1. This is a similar concept to the fancy multiplication table demo in Unit 3. Check the demo code for a review
1. I wrote the code for this function in 11 lines without any blank lines. This means you should have approximately 11 steps in your design. It doesn't need to be exactly 11, but should be close.

---
#### Sample Code
---
This is code that would use the function, called makeNumberPyramid, you are designing.

    num = eval(input("Enter the number of rows: "))

    output = makeNumberPyramid(num)

    print(output)
Make sure to review the rubric.

---
#### Common Errors
---
* Many students submit code for this task. Do not do this. Only submit a design.
