number = int(input("provide an integer: "))
while number > 1:
     print(number, end=" ")
     if number % 2 == 0:
          number = (number / 2)
     else: 
          number = ((number * 3) + 1)
     
print(number)
