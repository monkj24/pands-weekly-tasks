# program must ask user to input any positive integer 
# outputs the succesive values of the calculation, 
# continue until the sequence reaches 1


# Was difficult to me to create that program. I required help and I use another sites to resolve the errors
# I had error with output. I didn`t use "try and except" commands and program dasn`t show ame ny outputs


# Author : Joanna Mnich

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