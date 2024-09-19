# Romain Tranchant
# CIS 103: Fundamentals of Programming
# Lab 3: Python Loops and Object Types
# Due Date: 09/21/2024 @ 11:59pm
# Instructor: MD Ali
# Objective:
# The purpose of this lab is to practice and reinforce Python
# programming concepts related to loops (while, for, nested loops),
# string operations, lists, tuples, and dictionaries.
# Part 2: Strings and List Operations
# 1: String reversal
# 2: List operations

# 1: String Reversal: Write a Python function that takes a string and returns
# the string reversed. Test it with the string "Lab3Python". Hint: Use slicing

# Define the string that we want to reverse.
original_string = "Lab3Python"

# Define the function to reverse the string by returning a reversed version of
# the original string. The slicing operation [::-1] creates a reversed copy.
# The [::] means that we are taking the entire string and the "-1" index means
# we are moving backwards in the sequence
def reverse_string():
    return original_string[::-1]

# Call the reverse_string function and print the output
print(reverse_string())



# 2: List Operations: Write a Python program to:
# ◦ Create a list of 5 integers of your choice.
# ◦ Add a new integer to the list.
# ◦ Remove the third element from the list.
# ◦ Sort the list in descending order.
# ◦ Print the final list

# Creating a my_list variable with 5 integers
my_list = [8, 12, 16, 19, 24]

# Add the number 17 to the list
my_list.append(17)

# Remove the third number from my_list, at the index 2
my_list.pop(2)

# Sort the list in descending order
my_list.sort(reverse=True)

# print the list
print(my_list)
