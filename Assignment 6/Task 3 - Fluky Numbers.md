---
# Task 3 - Fluky Numbers
---
Save your program in a file called task3.py and your software development plan in a file called plan3.txt. You will write a program that will find Fluky Numbers. A Fluky Number is a number that is equal to the sum of a set of random numbers, where the random numbers are the first random numbers generated after seeding a random number generator with each factor of the number, not including itself. That's quite a mouthful, so here it is again in simpler terms. All of the following requirements must be met for a number to be a Fluky Number.

1. A Fluky Number is a number, called The Number,  that is equal to the sum of a set of randomly generated numbers.
1. Random numbers are generated with a random number function. We will use randint() from the random module.
1. The randomly generated numbers are in the range of 1 to the The Number, inclusive. (Ex. If The Number is 10, the random number can be 1 through 10, including 1 and 10)
1. Random numbers are the first number generated after setting a specific seed value (Use the random.seed() function).
1. The seed values are all of the factors of The Number, not including itself. (Ex. The factors of the number 10 that will be used for the seed are 1, 2, and 5)

---
#### Example
---
The number 8 is a Fluky Number. It's factors, not including itself, are 1, 2, and 4. The first random numbers generated between 1 and 8 after using the factors as a seed are 3, 1, and 4, respectively. The sum of those numbers is equal to 8. Thus, 8 meets the definition of a Fluky number.

---
#### Requirements
---
You must write a program to find all Fluky Numbers from 1 to 10000 (You cannot skip checking any number prior to 8). As a tip to help make sure you're on the right track, the first 3 Fluky Numbers are: 8, 22, and 25. Your program must discover these numbers, you may NOT use code such as the following:

    if testNum == 8:
        print("Found a Fluky Number!")
        
Your program may know that there are 7 Fluky numbers between 1 and 10000.

Your program must print the total running time in seconds to two decimal places. It must print the total number of inner loops executed. Here is an example output, without actual numbers showing: (Note: An 'X' does not indicate the number of digits or any other meaning. It's just a filler)

    Fluky Number: 8
    Fluky Number: 22
    Fluky Number: 25
    Fluky Number: XX
    Fluky Number: XX
    Fluky Number: XX
    Fluky Number: XX
    Total Time:  XX.XX seconds
    Total Loops:  XXXXXXXXXXX

See Rubric for all requirements. Make sure to catch the points for reducing the number of required loops.

---
#### NOTES
---
1. Your code must discover all seven Fluky Numbers using a nested loop structure.
1. You cannot use any information about properties of Fluky Numbers other than what is described. Your program may know that there will be exactly seven Fluky Numbers numbers with values of 10,000 or less.
1. You cannot start checking at 8, just because the instructions mentioned that 8 is the first Fluky Number. Your program must start checking at number 1.
1. You may use basic math/logic principles to help you reduce the number of iterations. If you're reading through wikipedia or doing google searches then you are over-thinking it. Think through in your planning how you can reduce the number of iterations without affecting the results...and think simply.
1. Big Hint: One approach to minimizing the number of iterations is to stop when you have found 7 Fluky Numbers. The other approaches are similar to this level of analysis.
