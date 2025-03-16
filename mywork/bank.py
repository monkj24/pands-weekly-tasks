# bank.py
# Prompt the user and read in two money amounts

# This is the first task, so I use ChatGPT to help me with print
# I found out that to define cents is necessary to use a function with % as a reminder
# author Joanna Mnich

amount1= int(input("Enter amount1 (in cent):"))
amount2 = int(input("Enter amount2 (in cent):"))

number = amount1 + amount2
euros = number // 100
cents = number % 100

print(f"The sum of these is €{euros}.{cents:02d}")

  
   

