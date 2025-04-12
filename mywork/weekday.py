# Write a program that outputs whether or not today is a weekday.
# First I checked what function today show me : day name, date ,or number
# then I use it as a number
# and add days name

#Author: Joanna Mnich

#https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/

from datetime import datetime  

today = datetime.today().weekday()

days = {
    0: "Monday",
    1: "Tuesday",  
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",  
    6: "Sunday"
}

print(f"Today is {days[today]}")

if today in [5, 6]:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")