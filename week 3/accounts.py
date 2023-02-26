# week 3
# This program read a account of any length and replace the characters with Xs, except the last four digits. 

account_number = input("Enter your account number ")

end_of_card = account_number[-4:]

new = account_number[:-4]

# The number of the credit card is sliced in two parts.

for n in new:
    if n.isdigit():
        new = new.replace(n, "X")


# Now the first part of the credit card is hide. 

print ("Your account number is: ", new, end_of_card)