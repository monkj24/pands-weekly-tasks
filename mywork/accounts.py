# Reads in a 10 characters account number and outputs the account number with last 4 numbers showing
# the first 6 characters replaced with Xs

# First I thought that if function [0:4] print first 4 digits, so I can use function with [6:0] and print me last 4
# I received no answer because in python , first index must be lower.
# Using function masked made me error because when coding I dont know account number to define accountno =.....
# I use function masked with not defined 10 digit numbers


# Author : joanna Mnich

accountno = input("Please enter a 10 digit account number:  ")

def mask_account(accountno):
    if len(accountno) < 6:
        return "Invalid account number"
    return "X" * 6 + accountno[6:]
masked = mask_account(accountno)

name = input("Account number is:  " )
print(name + masked)