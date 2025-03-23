# A histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# A plot of the function  h(x)=x3 in the range 0 to 10, 
# the one set of axes.


# Author: Joanna Mnich

import numpy as np
import matplotlib.pyplot as plt    #https://www.w3schools.com/python/numpy/numpy_random_normal.asp

# Parameters for the normal distribution
mean = 5
std_dev = 2
num_samples = 1000

np.random.seed(1)
normData = np.random.normal(mean, std_dev, num_samples)

# the figure and primary axis
fig, ax1 = plt.subplots()


# Plot the histogram of the normal distribution

ax1.hist(normData, bins=30, density=True, alpha=0.5, color='blue', label='Normal Distribution (µ=5, σ=2)')
ax1.set_ylabel('Density', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Plot the function h(x) = x^3 in the range [0, 10]
# A secondary axis for h(x) to show histogram and plot on the one set of axes
ax2 = ax1.twinx()
x = np.linspace(0, 10, 100)
h_x = x**3
ax2.plot(x, h_x, color='red', linestyle='--', linewidth=2, label='h(x) = x³')
ax2.set_ylabel('h(x)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Set title and labels
fig.suptitle('Normal Distribution and h(x) = x³', fontsize=14)
ax1.set_xlabel('x-axis')

# Labels and legend
ax1.set_xlabel('x-axis')
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95))

plt.show()



