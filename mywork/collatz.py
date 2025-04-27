# COLLATZ
# Program must ask a user to input any positive integer 
# Outputs the successive values of the calculation, 
# Continue until the sequence reaches 1

# Author : Joanna Mnich
# I had an error with the output because I used only while, I didn`t use "try and except" commands 
# and the program doesn`t show me any outputs


# https://www.w3schools.com/python/python_while_loops.asp
# https://docs.python.org/3/tutorial/errors.html#handling-exceptions

def sequence(number):
    sequence = []  # Create the empty list to store the sequence of numbers

    while number != 1:
        sequence.append(number) # append, keep tracking the number, add an item to the end of the list

        if number % 2 == 0:  # if the number is even, divide it by 2
            number = number // 2
        else:
            number = number * 3 + 1  # if the number is odd, multiply by 3 and add 1

    sequence.append(1)
    return sequence
try:
    number = int(input("Please enter a positive integer: "))  # convert input into an integer

    if number <= 0:
        print ("Please enter a positive integer.")

    else:
        result = sequence(number)
        print("Sequence:", result)
except ValueError:   # if the input isn`t valid integer, it go to except block
    print("Invalid input. Please enter a positive integer.")
