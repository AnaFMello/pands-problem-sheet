from datetime import date
week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

print ("Ops, it's weekday!" 
       if (week[date.today().weekday()]) in (0, 1, 2, 3, 4, 5) 
       else "Woooohoo, it's weekend!")