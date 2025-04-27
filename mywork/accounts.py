# ACCOUNTS
# Reads in a 10-character account number and outputs the account number with the last 4 numbers showing
# the first 6 characters replaced with Xs

# Author : Joanna Mnich
# First, I thought that if function [0:4] print the first 4 digits so, I can use a function with [6:0] 
# and it prints me the last 4, but I received no answer because the first index must be lower than the second in Python.
# Function masked made me error, because when coding, first must be defined account number (accountno =.....)
# I used a function masked with not-defined 10-digit numbers
# I used the len function to validate the input, to check how many characters were entered.
# Must be six digits entered because of the quantity masked requirement


#https://realpython.com/python-built-in-functions/#len
#https://docs.python.org/3/library/functions.html#len
#https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

accountno = input("Please enter a 10 digit account number:  ")

def mask_account(accountno):  
    if len(accountno) < 6:     
        return "Invalid account number"
    return "X" * 6 + accountno[6:] 
masked = mask_account(accountno)

name = input("Account number is:  " )
print(name + masked)
