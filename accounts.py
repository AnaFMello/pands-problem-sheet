# week 3
# This program read a account of any length and replace the characters with Xs, except the last four digits. 

account_number = input("Enter your account number ")

# The number of the credit card will be sliced in two parts.

end_of_card = account_number[-4:]

# the number of the card from the bginer till the 5th last, will be replaced for X

new = account_number[:-4]

# the last 4 digits of the card will always be original, dosent matter the leng of the card

for n in new:
    if n.isdigit():
        new = new.replace(n, "X")


# Now the first part of the credit card is hide. 

print ("Your account number is: ", new, end_of_card)

