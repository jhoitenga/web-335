#################################################
# Title: Exercise 3.3 - Python Variables and Functions
# Author: Professor Krasso
# Date: June 7th, 2023
# Modified By: Jennifer Hoitenga
# Description: Experimenting with Python variables and functions.
# Sources Used: 
# Learn Python in One Hour by Programming with Mosh YouTube
# Python Functions by Programming with Mosh YouTube
#################################################

# Creating a function that adds two parameters.
num1 = 4
num2 = 4
def add(num1, num2):
    total = num1 + num2
    return total

result = add(num1, num2)
print("{} + {} is {}.".format(num1, num2, result))


# Creating a function that subtracts two parameters.
num3 = 10
num4 = 6

def subtract(num3, num4):
    total = num3 - num4
    return total

result = subtract(num3, num4)
print("{} - {} is {}.".format(num3, num4, result))


# Creating a function that divides two parameters.
num5 = 8
num6 = 2

def divide(num5, num6):
    total = num5 / num6
    return total

result = divide(num1, num2)
print("{} / {} is {}.".format(num5, num6, result))


# Creating a function that multiplies two parameters.
num7 = 10
num8 = 2

def multiply(num7, num8):
    total = num7 * num8
    return total

result = multiply(num7, num8)
print("{} * {} is {}.".format(num7, num8, result))


# Call each function and print the results using output variables and string concatenation.
add_result = add(num1, num2)
print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(add_result) + ".")

subtract_result = subtract(num3, num4)
print("The difference between " + str(num3) + " and " + str(num4) + " is " + str(subtract_result) + ".")

divide_result = divide(num5, num6)
print("The division of " + str(num5) + " by " + str(num6) + " is " + str(divide_result) + ".")

multiply_result = multiply(num7, num8)
print("The product of " + str(num7) + " and " + str(num8) + " is " + str(multiply_result) + ".")