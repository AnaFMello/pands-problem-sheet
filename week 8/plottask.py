## This program display:

## a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
## and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.

import matplotlib.pyplot as plt
import numpy as np

# Histogram of a normal distribution with mean=5 and standard deviation=2
mean = 5
std_dev = 2
values = np.random.normal(mean, std_dev, 1000)
plt.hist(values, color='pink')
x_values = np.linspace(0, 10, 100)
y_values = x_values ** 3
plt.plot(x_values, y_values, color='blue')
plt.title('Week 8 - Plottask.py')
plt.xlabel('Number Cube')
plt.ylabel('Number')
plt.show()


