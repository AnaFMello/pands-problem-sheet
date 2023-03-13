def newton_method(number, number_iters = 100):

    a = float(number) 

    for i in range(number_iters): 

        number = 0.5 * (number + a / number) 

    return number

# defining the function using the newton method, to find the square foot

a=int(input("Enter a number:"))


print("Square root of {a}:",newton_method(a))


## search source https://www.angela1c.com/projects/problem_set_links/problem7/  
## https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method?utm_content=cmp-true