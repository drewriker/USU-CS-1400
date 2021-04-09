# Task 1 - Wordinator
---
Starter: [week10_task1_starter.zip](https://github.com/drewriker/USU-CS-1400/files/6283504/week10_task1_starter.zip)


You will create a program that will generate specific output based on two words. You will design, implement, and use a Wordinator object that will perform the specific operations. Make sure to watch the video and read the description below carefully. Many parts of this are simple. There is one part that will take some thinking to get implemented properly. Note the sections where you must do things a specific way. In other words, you will not be able to use specific operators or functions, and must program the solution in another way (manually).

Use the starter code file unit5_task3_starter.py. Modify the name so it is called task1.py. Your plan should be created in plan1.txt. It must include the UML and design for the Wordinator class. You do not need to design the code that will be in task1.py. Create another file called wordinator.py to create your Wordinator class. Meet the following requirements. 

As always, please see rubric for grading details.

---
### Requirements
---
* task1.py
    1. The code in the file should not change from what is given in unit5_task3_starter.py.
    1. You should become familiar with how the menu system works. It will help you on a future assignment.
* wordinator.py
    1. Use appropriate private data and method members. Items not created as private that should be will lose points.
    1. Create a constructor that takes a single word as a parameter
    1. Write appropriate methods to meet all requirements as indicated in the user menu. Details of each are below
* Menu Item Output(use as a guide to determining method requirements)
    1. First Word
        1. Prints the word that comes first ***alphabetically***. 
        1. Note that alphabetically is bolded.
    1. Big Word
        1. Prints the two words into one big concatenated word.
        1. The first letter should be capitalized with all others lowercase.
        1. NOTE: There is an inconsistency in the video. Match the requirements here for your submission.
    3. Words Factor
        1. Ask the user for an integer factor value
        1. Print each words repeated the integer factor number of times.
        1. All letters should be uppercase
        1. NOTE: There is an inconsistency in the video. Match the requirements here for your submission.
    4. Mix Words
        1. Print a new word where each sequential letter is from the other word.
        1. Example:
            1. Word1: Apple
            1. Word2: Banana
            1. MixedWord: Abpapnlaena
        1. If one word is longer, then it's letters do not alternate after the other word's letters are used up
        1. The first letter should be capitalized with all others lowercase.
    5. Middle Words
        1. This one will take some thought
        1. Print the middle portion of each of the two words
        1. The middle portion is approximately half of the length of the entire word
        1. The number of characters that come before and after the middle portion should be equal
        1. The length of the middle word must meet the following requirements:
            1. Difference between the number of middle characters and outside characters cannot be greater than two
            1. The number of characters in the middle cannot be more than one greater than the number of outside characters
        1. Hint: If you can meet the previous requirements for words of length 7, 8, 9, and 10, you will be set.
        1. You may not have duplicate code to calculate this for each word. This should make you think of code reuse.
    6. Switch Case
        1. You may not use the switchcase() method, or any other method that swaps case automatically.
        1. Print each of the words with the case of each letter swapped from the original
        1. You may not have duplicate code to calculate this for each word.
    7. Back Words Slice
        1. Print each word backwards
        1. You must use the slice operator to reverse the ordering
        1. Each letter should maintain its original capitalization.
    8. Back Words Manual
        1. Print each word backwards
        1. You MAY NOT use the slice operator or any other method that reverses a string automatically. A loop might help.
        1. Each letter should maintain its original capitalization.

---
### Common Errors
---

Pay attention to the starter code, and how it uses the Wordinator objects for each menu item. This gives you insight in to how to design each associated method. One common error is to not realize that this task is an exercise in operator overloading for many of the menu items.
