# Romain Tranchant
# CIS 103: Fundamentals of Programming
# Lab 3: Python Loops and Object Types
# Due Date: 09/21/2024 @ 11:59pm
# Instructor: MD Ali
# Objective:
# The purpose of this lab is to practice and reinforce Python
# programming concepts related to loops (while, for, nested loops),
# string operations, lists, tuples, and dictionaries.
# Part 3: Tuples and Dictionaries
# 1: Tuple operations
# 2: Dictionary operations


# 1: Tuple operations
# ◦ Create a tuple with the elements (4, 5, 6, 7, 8).
# ◦ Print the first and last elements of the tuple.
# ◦ Attempt to change the second element of the tuple and note what happens

# Create my_tuple with 5 integers
my_tuple = (4,5,6,7,8)

# Print the first element , index 0
print("First element:", my_tuple[0])

# Try to reassign a different value the to index 1 , element 5 , with
# a new value of 123. This return an error message because tuples can not
# be changed , they are immutables
try:
    my_tuple[1] = 123
except TypeError as t:
    print("Error,", t)


# Part 2: Dictionary operations
# Dictionary operations: Write a Python program that:
# ◦ Creates a dictionary with the following key-value pairs:
# • ‘name’: ‘Alice’, ‘age’: 22, ‘major’: ‘Computer Science’
# • Adds a new key-value pair for the student’s GPA
# • Modifies the student’s age to 23
# • Removes the ‘major’ key from the dictionary
# • Prints all the keys and values from the dictionary

my_dictionary = {'name': 'Alice', 'age': 22, 'major' : 'Computer Science'}
my_dictionary["GPA"] = 4
del my_dictionary["major"]
print(my_dictionary)

