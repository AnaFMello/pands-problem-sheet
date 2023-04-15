def newton_method(number, number_iters = 100):
    a = float(number) 
    for i in range(number_iters): 
        number = 0.5 * (number + a / number) 
    return number

a=int(input("Enter a number to find the square root:"))
print("The square root is:",newton_method(a))
 