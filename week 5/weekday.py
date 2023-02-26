# This program outputs whether or not today is a weekday.


from datetime import date
week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

print ("weekday!" 
       if (week[date.today().weekday()]) in (0, 1, 2, 3, 4, 5) 
       else "weekend!")

print(f'Celebrate, it is {week[date.today().weekday()]} :) !')
