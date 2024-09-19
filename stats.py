# Romain Tranchant
# CIS 103: Fundamentals of Programming
# Lab 3: Python Loops and Object Types
# Due Date: 09/21/2024 @ 11:59pm
# Statisticians would like to have a set of functions to compute the median and mode of a
# list of numbers. The median is the number that would appear at the midpoint of a list if it
# were sorted. The mode is the number that appears most frequently in the list. Define these
# functions in a module named stats.py. Also include a function named mean , which
# computes the average of a set of numbers. Each function expects a list of numbers as an
# argument and returns a single number.

the_list = [22, 23, 24, 24, 25, 25, 29, 30, 35]

# Define the mode function using the_list as a variable
def mode(the_list):
# Create a max_count variable as a tuple using the index and the value
# of the corresponding number
    max_count = (0, 0)
# Start a for loop going through each number of the_list
    for number in the_list:
# Count how many times the current number appears in the_list
       count_of_number = the_list.count(number)
# Check if the current number's count is greater than the maximum count recorded
       if count_of_number > max_count[0]:
# Update max_count to the new maximum count and the corresponding number
           max_count = (count_of_number, number)
# Return the number that has the highest count
# If there is a tie, will return the first number encountered with that maximum frequency
    return max_count [1]
# Call the mode function and print the result using f-string
print(f"The mode is: {mode(the_list)}")


# Define the median function using the_list as a variable
def median(the_list):
# Sort the_list in ascending order
    the_list.sort()
# Getting the length of the_list through the list_length variable
    length_list = len(the_list)
# Check if the length of the list is an odd number
    if length_list % 2 != 0:
# Assign the list_middle variable by dividing index value of length_list by 2
        list_middle = length_list // 2
# Return the list_middle as being the middle element, the median
        return the_list[list_middle]
# If the length of the list is an even number
    else:
# Calculate the index of the higher middle element
        list_middle1 = length_list // 2
# Calculate the index of the lower middle element.
        list_middle2 = list_middle1 - 1
# return the mean of the two middle elements, the median
        return (the_list[list_middle1] + the_list[list_middle2]) / 2
# Call the median function and print the result using f-string
print(f"The median is: {median(the_list)}")



# Define the mean function using the_list as a variable
def mean(the_list):
# Create a variable named total to get track of the sum of numbers on the_list
    total = 0
# Start a for loop to go through each number of the_list
    for number in the_list:
# Add the current number to the total sum
        total = total + number
# Return the sum total of the_list and divide it by the length of the_list
    return total / len(the_list)
# Call the mean function and print the result using f-string
print(f"The mean is: {mean(the_list)}")
