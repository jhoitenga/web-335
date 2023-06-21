#################################################
# Title: Exercise 5.3 - Python Conditions, Lists and Loops
# Author: Professor Krasso
# Date: June 21, 2023
# Modified By: Jennifer Hoitenga
# Description: Experimenting with Python conditionals and iterators.
# Sources Used: 
# Learn Python in One Hour by Programming with Mosh YouTube
# W3Schools Python Loop Lists: https://www.w3schools.com/python/python_lists_loop.asp
# W3Schools Python If Else: https://www.w3schools.com/python/python_conditions.asp
#################################################

# Creating a list of 5 hobbies.
hobbies = ["gardening", "antiquing", "gaming", "collecting", "watching movies"]
print("My hobbies include: ")

# Using a for loop to iterate over the list of hobbies and print them.
for x in hobbies:
    print(x)

# Adding a blank line between Hobbies and Days for readability.
print()

# Creating a list of Days (Sunday through Saturday).
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Using a for loop to iterate over the list & an if else statement to display the day & message.
for day in days:
    if day == "Sunday":
       print ("Today is Sunday. I am off work and enjoying my hobbies.")
    elif day == "Monday":
       print ("Today is Monday. It is a work day.")
    elif day == "Tuesday":
       print ("Today is Tuesday. It is a work day.")
    elif day == "Wednesday":
       print ("Today is Wednesday. It is a work day.")
    elif day == "Thursday":
       print ("Today is Thursday. It is a work day.")
    elif day == "Friday":
        print ("Today is Friday. It is a work day.")
    elif day == "Saturday":
        print ("Today is Saturday. I am off work and enjoying my hobbies.")



