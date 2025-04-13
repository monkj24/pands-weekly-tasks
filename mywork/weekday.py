# WEEKDAY
# Write a program that outputs whether or not today is a weekday.

# Author: Joanna Mnich
# First I checked what function today show me : day name, date ,or number
# Then I use it as a number, and add days name



#https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/
#https://docs.python.org/3/library/datetime.html
#https://docs.python.org/3/tutorial/controlflow.html#if-statements
#https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday

from datetime import datetime  # datetime module used to determine the current day of the week

today = datetime.today().weekday() # returns current day and time

days = {                # days from 0 not 1 , define each day integer with coresponding name day
    0: "Monday",
    1: "Tuesday",  
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",  
    6: "Sunday"
}

print(f"Today is {days[today]}")  # f string function to concentrate of current day week

if today in [5, 6]:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")