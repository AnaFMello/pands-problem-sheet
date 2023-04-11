number1 = input("Enter the first amoun: ")
number2 = input("Enter the second amount: ")

# this first part will grab the info from the user

number1 = float(number1)
number2 = float(number2)

# this second part will fix the information offered as a decimal number

number1 = number1 / 100
number2 = number2 / 100

# the third part will divide the number by 100, making is as cents

added = float(number1 + number2)

# the fourth part will add the cents, creating euro

print("Your amount total is €",added)
