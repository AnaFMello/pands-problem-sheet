def newton_method(guess, number_iters = 1000):
    a = float(guess) 
    for i in range(number_iters): 
        guess = 0.5 * (guess + a / guess) 
    return guess

a=int(input("Enter a number to find the square root:"))
print("The square root is:",newton_method(a))
 