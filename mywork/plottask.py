<<<<<<< HEAD
# PLOTTASK
# A histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2, 
# A plot of the function  h(x)=x3 in the range 0 to 10, 
# the one set of axes.


# Author: Joanna Mnich

#https://www.w3schools.com/python/numpy/numpy_random_normal.asp
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
#https://pandas.pydata.org/pandas-docs/version/0.15.0/visualization.html
#https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html
#https://realpython.com/python-histograms/?utm_source=chatgpt.com



import numpy as np   # numpy used for numerical operations, here to generate random data for a normal distribution
import matplotlib.pyplot as plt    # matplotlib import librery to creating plots, 
                                   # pyplot create the figure, axes 

=======
import numpy as np
import matplotlib.pyplot as plt


>>>>>>> 66af136 (new)
# Parameters for the normal distribution
mean = 5
std_dev = 2
num_samples = 1000

<<<<<<< HEAD
np.random.seed(1) # seed added to ensure data does not change whenever the code is run
normData = np.random.normal(mean, std_dev, num_samples) # result of random stored in normData

# the figure and primary axis
fig, ax1 = plt.subplots() # creates a figure and a primary set of axes, 
                          # The subplots function returns a figure and axis object


# Histogram of the normal distribution

ax1.hist(normData, bins=30, density=True, alpha=0.5, color='blue', label='Normal Distribution (µ=5, σ=2)')
# The bins = 30 means the data will be divided into 30 bins
# Density is a probability density, which is the area under the histogram.
# alpha - 0.5 makes the bars semi-transparent
# color of bars
ax1.set_ylabel('Density', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# A second plot of he function h(x) = x^3 in the range [0, 10]
ax2 = ax1.twinx()
x = np.linspace(0, 10, 100)
h_x = x**3

# An axis for h(x) to show the histogram and plot on the one set of axes
ax2.plot(x, h_x, color='red', linestyle='--', linewidth=2, label='h(x) = x³') 
ax2.set_ylabel('h(x)', color='red')
ax2.tick_params(axis='y', labelcolor='red') # Params = parameters

# Title and labels
fig.suptitle('Normal Distribution and h(x) = x³', fontsize=14)
ax1.set_xlabel('x-axis')

# Labels and legend
ax1.set_xlabel('x-axis')
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95)) 

plt.show()



=======
# Generate random values from a normal distribution
normal_data = np.random.normal(mean, std_dev, num_samples)

# Generate x values for the cubic function
x_values = np.linspace(0, 10, 100)
h_values = x_values**3

# Create a figure and an axis
plt.figure(figsize=(10, 6))

# Plot the histogram of the normal distribution
plt.hist(normal_data, bins=30, density=True, alpha=0.5, color='blue', label='Normal Distribution (µ=5, σ=2)')

# Plot the cubic function
plt.plot(x_values, h_values, color='red', label='h(x) = x^3', linewidth=2)

# Add labels and title
plt.title('Histogram of Normal Distribution and Function h(x) = x^3')
plt.xlabel('x')
plt.ylabel('Density / h(x)')
plt.legend()
plt.grid()

# Show the plot
plt.show()
>>>>>>> 66af136 (new)
