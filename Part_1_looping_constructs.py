# Romain Tranchant
# CIS 103: Fundamentals of Programming
# Lab 3: Python Loops and Object Types
# Due Date: 09/21/2024 @ 11:59pm
# Instructor: MD Ali
# Objective:
# The purpose of this lab is to practice and reinforce Python
# programming concepts related to loops (while, for, nested loops),
# string operations, lists, tuples, and dictionaries.
#
# Part 1: Looping_constructs
# 1: While loop
# 2: For loop
# 3: Break and continue
# 4: Nested loops


# 1: While Loop: Write a Python program that prints the numbers from 1 to 10
# using a while loop, but exits the loop when the number reaches 7.

# Giving the value 1 to the variable number
number = 1

# Start a while loop that will run while the variable number
# is smaller or equal to 10 and the print value of number
while number <= 10:
    print(number)

# Increase the value of number by 1
    number += 1

# Check if the value is equal to 7 , the break statement terminates
# the "while" loop, 7 and the rest of the numbers after 8 are not printed
    if number == 8:
        break




# 2: For Loop: Write a Python program that iterates over the string "CIS103Lab3"
# and prints each character, one by one, followed by its index in the string.

# Assigning "CIS103Lab" as a string to the variable string
string = "CIS103Lab3"

# Start a for loop that will iterate every character from the variable string,
# and enumerate each character and index number
for index,char in enumerate(string):

# The print function will return every character of "CIS103Lab" and its
# index . The variable {char} will be replaced by its character
# and the variable index by its index number
    print(f"Character:{char} Index:{index}")





# 3: Break and Continue: Modify the program from Exercise 1. This time, use the
# continue statement to skip the number 5, but the program should still print
# numbers from 1 to 10, breaking at 7

# Giving the value 1 to the variable number
number = 1

# Start a while loop that will run while the variable number
# is smaller or equal to 10
while number <= 10:

# Skip the number 5 by skipping the iteration of 5, and the continue statement
# allows to loop to go past the number 5 and increase the value of number by 1
    if number == 5:
        number += 1
        continue

# Print the current number
    print(number)

# Check if the value is equal to 7; the break statement terminates
# the "while" loop, 7 and the rest of the numbers after 7 are not printed
    if number == 7:
        break

# Increase the value of number by 1
    number += 1



# 4: Nested Loop: Write a Python program that uses nested loops to generate the
# following pattern:
# *
# **
# ***
# ****
# *****

# Starting a for loop with i in range of the number 1 to 5
for i in range(1,6):

# Starting another loop where j will iterate i from the value 0 to 5
    for j in range(i):

# Print the  "*" character, the "end=" argument prevent the print function
# the stars to be printed after each others, but to be printed on different lines
        print('*', end='')

# All the starts from the previous row were printed , this print function stars
# a new row
    print()
