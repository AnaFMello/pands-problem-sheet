# this task asks the user to input any positive integer
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one

number = int(input("provide an integer: "))

c = number

while c > 1:
     if c % 2 == 0:
          c = (c / 2)
     else: 
          c = ((c * 3) + 1)
     print(c)
