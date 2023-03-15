# This program outputs whether or not today is a weekday. 

# first I have to import the date

from datetime import date
week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# now, using if, else, it prints todays date

print ("weekday!" 
       if (week[date.today().weekday()]) in (0, 1, 2, 3, 4, 5) 
       else "weekend!")

print(f'Celebrate, it is {week[date.today().weekday()]} :) !')
