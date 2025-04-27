# BANK
# Prompt the user and read in two money amounts ( in cents)


# Author Joanna Mnich
# I found out that to define cents is necessary to use a function with % as a reminder
# Using f-string in print at the end helps clean evaluate expression inside brackets {}


#https://docs.python.org/3/library/functions.html#input
#https://www.w3schools.com/python/python_operators.asp
#https://realpython.com/python-f-strings/



amount1= int(input("Enter amount1 (in cent):"))  # convert input into an integer
amount2 = int(input("Enter amount2 (in cent):"))

number = amount1 + amount2
euros = number // 100
cents = number % 100

print(f"The sum of these is €{euros}.{cents:02d}") # Format (:02d) to show decimal number

  
   

