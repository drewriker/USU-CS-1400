# Task 2 - Blobber
---
Call your files task2.py, blobber.py, and plan2.txt.

You are going to complete a program called Blobber. A Blobber is an imaginary being who is shaped like a cylinder. Your program will allow a user to create a Virtual Blobber they can take care of, similar to virtual pet like a Tamagotchi. Taking care of a Blobber is not an easy task. It takes constant vigilance and dedication. By the time you’re done testing your program you will never want to own an actual Blobber.

---
### Starter Code
---
[task2_starter.zip](https://github.com/drewriker/USU-CS-1400/files/6283298/task2_starter.zip)

Change the name of this file to task2.py. Only change the file where marked `<Fill-In>`. If `<Fill-In>` is only a line by itself, then you must complete the entire line. If it is part of a line, then you just add code to replace the `<Fill-In>` marker.

---
### How a Blobber works
---
A Blobber is a funny kind of being. It known by a combination of a name and color. It is shaped like a cylinder and likes to maintain a certain level of happiness. Its happiness is determined solely by how close its current volume is compared to its volume at birth. Immediately following birth, its radius begins to decrease. The Blobber caretaker can feed the Blobber regularly in order to maintain its volume. If the volume is ever too high or too low, the Blobber turns to dust.

Create a class called Blobber inside of a file called blobber.py. Your Blobber class should have the following properties:

* A private float data field called radius
* A private float data field called height
* A private string data field called color. The color should always be lowercase.
* A private string data field called name. The name should always be capitalized.
* A constructor is called with a name, color, radius, and height.
* Accessor (getter) and mutator (setter) methods for name and color
* A method called feedBlobber()
    * Takes a float value and increases the radius by the given amount
    * This method takes some thought!
* A method called blobberSpeak() that returns a string that can be printed.
    * The string should be a complete two line statement that includes the name, color, and happiness level of the Blobber.
    * Ex:
        * My name is Alice, and I am green.
        * My current happiness level is 93.25%
    * The happiness level should be shown as a percentage with two decimal places
    * Note: this method returns a string, it does not print a string
* A method called vitalsOK().
    * See the Blobber Vitality section for more details 
    * Returns two values:
        * The current happiness level
        * A Boolean value 
            * True if the Blobber is alive.
            * False if the Blobber has turned to dust.
* Any other private data or methods you need.

---
### Blobber Vitality
---
A Blobber’s happiness level is a measure of how close its current volume is compared to its original volume. It is 100% when the volumes are exactly the same. It cannot survive when the current volume is +/- 10% of its original volume. This means a Blobber can only exist if its happiness is from 90% to 110%.

A Blobber loses 0.2% of its ***original*** radius every second. If its volume is ever greater or less than 10% of its ***original*** volume, then it turns to dust.  The vitality should be checked and displayed right after the menu. It should also be checked right after a menu selection is made. In either case, if the Blobber has turned to dust, an appropriate message should be displayed and the program should end. See the starter code for details.

---
### Main Menu
---

    (1): Display Name
    (2): Change Name
    (3): Display Color
    (4): Change Color
    (5): Feed Blobber
    (6): Blobber Speak
    (7): Exit

You will need to decide on some submenus for some of the choices. Use blank lines in your output so it's easy for the user to see what is happening.

---
### Video Demo
---

Sorry, there is a bug in my demo. The calculation of the happiness level is off. I believe I had the radius and height variables backwards. Double check your formula and go with your calculation.


---
### Timer Help
---

This is not really part of the assignment, but may help you figure out how to manage the changing of the Blobber's vitality.

[FakeTimer.zip](https://github.com/drewriker/USU-CS-1400/files/6283341/FakeTimer.zip)

---
### Design Plan
---

Your Software Design is getting more and more complicated. Make your plan for blobber.py, including UML. Within the plan create a design for each function/method. As you break down the problem into individual pieces, calling a function/method you design counts as an individual piece since it will be designed as well.  This means the design of one function/method can include a function call to another function/method. Make sure to include UML for the Blobber class.

---
### Common Errors
---

This is the most difficult task to this point of this semester. It is meant to be very challenging. The most common error is not breaking the program down into small pieces. Complete one menu item at a time.
