# Program must ask user to input any positive integer 
# Outputs the succesive values of the calculation, 
# Continue until the sequence reaches 1

# 
# I had error with output because I use only while, I didn`t use "try and except" commands 
# and program doesn`t show me any outputs

# Author : Joanna Mnich

#https://www.w3schools.com/python/python_while_loops.asp
#https://docs.python.org/3/tutorial/errors.html#handling-exceptions

def sequence(number):
    sequence = []

    while number != 1:
        sequence.append(number)

        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1

    sequence.append(1)
    return sequence
try:
    number = int(input("Please enter a positive integer: "))

    if number <= 0:
        print ("Please enter a positive integer.")

    else:
        result = sequence(number)
        print("Sequence:", result)
except ValueError:
    print("Invalid input. Please enter a positive integer.")