### Task 3 - Gronky
---
Starter Code: unit6_task3.zip

You will complete a program for a brand-new kind of card game. The game is called Gronky. It is similar to a regular deck of cards, with some slight changes. Starter code has been provided. Use the starter code and only fill in required areas. This includes the spots marked `<Fill-In>` and adding missing functions or methods as indicated. You should not be modifying existing code. Your submission should include five files: task3.py, gronkyutil.py, deck.py, card.py, plan3.txt.

#### Overview
---
* You will figure out how many cards you need in the deck to fulfill the requirements
* Each card has three components
  * Id: unique integer for each card (lowest id number is 0, largest is one less than number of cards)
  * Title: Numbers one through ten, Baker, Jester, Page, Scribe, Squire, Armorer, and Marshal
  * Gang: Jets, Pollos, Slugs, Yokels, Keiths, and Elbows
* Each card is unique, meaning there are no cards that match all three components. The Id can be used to determine its title and gang.
* Every possible combination of Title/Gang must be present in the deck of cards


#### Requirements
---
* Create a file called plan3.txt
  * Include the Software design for your search and sort functions (three total)
  * No other UML, design, or plan is required.
* Add to a class called Card in card.py
  * Used to create a single card for the deck
  * Fill in partial lines of code for getTitle() and getGang()
  * Add two dunder methods in order to meet other program requirements
* Add to a class called Deck in deck.py
  * Used to create a single deck of cards
  * Fill in three lines/sections as indicated
* Use the module called gronkyutil.py
  * This stores the map for TITLE and GANG
  * It contains a function you can use to check to see if your id to title/gang conversion is working properly. It may also come in handy somewhere else (hint hint).
  * Fill in areas as indicated
* Change the unit6_task3_starter.py file name to task3.py.
* Main menu
  * Each menu option should result in a function call, except for option 5
  * The function signature for option 1 is included and should help you with the others
  * Display
    * Display each card in the hand on a single line
    * Use the print() with the card object as the parameter
      * Ex. print(card1)
      * This means you should not call a method on the card object to determine what to print
    * Each card should be displayed as "Title of Gang"
      * Ex. Baker of Slugs
  * Sort by Title
    * Perform a sort using a selection, insertion, or bubble sort.
    * A message should indicate which sort is used
    * Use an existing function in the code to make it appear as if the program is processing
    * Do not display the list of cards. The user should choose to display it after the sort is complete
  * Sort by Gang
    * Perform a sort using a selection, insertion, or bubble sort.
    * Do not use the same sort technique as the Sort by Title
    * A message should indicate which sort is used
    * Use an existing function in the code to make it appear as if the program is processing
    * Do not display the list of cards. The user should choose to display it after the sort is complete
  * Search for Card
    * Display submenus to allow the user to select a Title and Gang for the card to search for
    * Use an existing sort algorithm to sort the hand
    * Perform a binary search to determine if the card is in the hand
    * Display a message indicating whether or not the card is in the hand
