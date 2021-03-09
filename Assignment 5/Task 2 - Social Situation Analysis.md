---
# Task 2 - Social Situation Analysis
---
Save your program as task2.py and your software development plan as plan2.txt. You will write a program that will perform an analysis on a social situation. A user will input their name, location, and radius of their personal space. A second user will do the same. You will analyze this information and determine the results of two tests.

Person Test: This test determines if an individual has someone in their own personal space. One of the following outputs is possible:

* Person One is in Person Two's personal space
* Person Two is in Person One's personal space
* Person One and Person Two are in each other's personal space
* Neither Person One nor Person Two is in the other's personal space

Space Test: This test determines the relation of the personal spaces of each person. One the following outputs is possible:

* Person One and Person Two's personal spaces overlap
* Person One and Person Two's personal spaces do not overlap
* Person One's personal space is entirely inside Person Two's personal space
* Person Two's personal space is entirely inside Person One's personal space

NOTE: The messages you print out should look very similar to these. That means the user's name should actually be printed where Person One or Person Two is shown above.

---
#### Example
---
    Welcome to the Social Situation Analyzer System
    Person One
        Enter your name: Alice
        Enter your position (x, y): 50, -70
        Enter your personal space radius: 30

    Person Two
        Enter your name: Bob
        Enter your position (x, y): 30, -50
        Enter your personal space radius: 20

    Social Situation Analysis Results
        Person Test: Bob is in Alice's personal space
        Space Test: Alice and Bob's personal spaces overlap

---
#### Code Requirements
---
* You may have only one print statement after the second user enters their info. It must look exactly as the following:
    print(msg)
* You may assume the user will give proper input
* You may assume that the people cannot stand in the exact same location (distance between them cannot be zero)
* You must use a logical operator to determine if the users are both in each other's space
* Read the Rubric for all grading details
