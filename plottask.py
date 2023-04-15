import matplotlib.pyplot as plt
import numpy as np

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


