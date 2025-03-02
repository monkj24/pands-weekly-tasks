# Write a program that outputs whether or not today is a weekday.
# First I checked what function today show me : day name, date or number
# then I use it as a number
#Author: Joanna Mnich

from datetime import datetime

today = datetime.today().weekday()

print(today)

if today > 4:
    print ('It is the weekend, yay!')
else:
    print ('Yes, unfortunately today is a weekday')

