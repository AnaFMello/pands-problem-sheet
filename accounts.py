account_number = input("Enter your account number ")
end_of_card = account_number[-4:]
new = account_number[:-4]

for n in new:
    if n.isdigit():
        new = new.replace(n, "X")

print ("Your account number is: ", new+end_of_card)

