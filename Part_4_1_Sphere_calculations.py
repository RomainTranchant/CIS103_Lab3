# Romain Tranchant
# CIS 103: Fundamentals of Programming
# Lab 3: Python Loops and Object Types
# Due Date: 09/21/2024 @ 11:59pm
# Instructor: MD Ali
#  Write a program that takes the radius of a sphere (a floating-point number)
#  as input and outputs the sphere’s diameter, circumference, surface area,
#  and volume


# Define the variable pi
pi = 3.14159

# Define the diameter function using the radius as float input and return the formula
# to calculate the diameter
def diameter(radius):
    return radius * 2

# Define the circumference function using the radius as float input and return the
# formula to calculate the circumference
def circumference(radius):
    return radius * 2 * pi

# Define the surface function using the radius as float input and return the formula to
# calculate the surface
def surface(radius):
    return 4 * pi * radius **2

# Define the volume function using the radius as float input and return the formula to
# calculate the volume
def volume(radius):
    return 4/3 * pi * radius **3

# Define the main function
def main():

# Start a while loop to get the user input
    while True:

# Using the try block to handle errors and incorrect inputs
        try:

# Asking the user to input a number and convert it into a float number
            radius = float(input("Enter the radius:"))

# If the radius is negative or equal to 0, print an error message and the
# sphere function skips the rest of the loop through the continue statement
            if radius <= 0:
                print("Error, the radius must be a positive number")
                continue

# If the radius is not a number, print an error message and the sphere function
# skips the rest of the loop through the continue statement
        except ValueError:
            print("Error, please enter a number")
            continue

# call all the previously defined functions and print the results using formatted strings
        print(f"Diameter: {diameter(radius)}")
        print(f"Circumference: {circumference(radius)}")
        print(f"Surface: {surface(radius)}")
        print(f"Volume: {volume(radius)}")

# Continue the loop for another user input
        continue
# Call the sphere function to execute the program
main()

# Make sure that the function can only run in this program and ca not be imported
if __name__ == "__main__":
    main()
