---
# Task 4 - The Zookeeper Statistician
---
Save your program in a file called task4.py and your software development plan in a file called plan4.txt. Here is a quick story about two elephants who live in the Potowatomi Zoo. Every evening the elephants each randomly select one of six sleeping pens to spend the night in. After deciding on which pen, they simultaneously enter the pen from opposite sides. Being slightly vision impaired, they cannot see if the other elephant entered the same pen until it is too late to turn around and go to another pen to spend the night. Thus sometimes they must each spend an uncomfortable night sharing a small sleeping area with another elephant.


After the elephants are asleep the zookeeper randomly picks one of the pens to check. During a break, the zookeeper and the nighttime custodian were talking. The zookeeper told the custodian that 1/3rd of the time when he checks a pen, there's at least one elephant in there, and of the times that there's at least one elephant in the pen, 1/6th of the time the other elephant is in there as well. The custodian said that those percentages cannot be correct, but the zookeeper insisted they are.

---
#### Requirements
---
Your job is to write a program to simulate this nightly activity 100,000 times to determine if the zookeeper or the custodian is correct. As a simulation, you will program all steps of this process. You are not writing a statistical analysis program to calculate probabilities.

You will report the following statistics.

1. What percentage of the time there is at least one elephant in the pen the zookeeper checks?
1. When there is an elephant in the pen the zookeeper checks, what percentage of time are both elephants in the pen?
1. Based on the results of your simulation, is the zookeeper or the custodian correct? (Use 2% points as the margin of error)

Your results should be displayed as percentages with two decimal places.

After your results are displayed, you will prompt the user to choose to end the program or run the simulation again. That way, whomever the results indicate is wrong, can easily try another simulation to see if the results were a fluke. You can use a simple message such as:

    Run the simulation again? (yes or no): 

Read the rubric for all requirements.

---
#### TIPS
---
1. Your software design is very important. Make sure you've planned for every requirement and thought of a way to code each requirement individually and step-by-step. Then you can increase your confidence that your simulation is correct.
1. Double check the description for what you're looking for when both elephants are in the same pen.
