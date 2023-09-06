import numpy as np
import matplotlib.pyplot as plt

x_matrix = np.array([2, 3, 5, 7, 9])
y_matrix = np.array([4, 5, 7, 10, 15])

# Takes two matrices and calculates the sum of x, y, xy, x^2
def data_values(x_matrix, y_matrix):
    sum_x = sum(x_matrix)
    sum_y = sum(y_matrix)
    sum_xy = sum(x_matrix * y_matrix)
    sum_x2 = sum(x_matrix ** 2)
    return (sum_x, sum_y, sum_xy, sum_x2)


# Calculates the slope and intercept
def linear_regression(x_matrix, y_matrix):
    sum_x, sum_y, sum_xy, sum_x2 = data_values(x_matrix, y_matrix)
    slope = (sum_xy - sum_x * sum_y) / (sum_x2 - (sum_x) ** 2)
    intercept = (sum_y - slope * sum_x) / len(x_matrix)
    return slope, intercept


slope, intercept = linear_regression(x_matrix, y_matrix)

predicted_y = slope * x_matrix + intercept

# Calculate the mean squared error
mse = np.mean((y_matrix - predicted_y) ** 2)

print("Mean Squared Error:", mse)

# Plot the data as a scatter plot
plt.scatter(x_matrix, y_matrix)

# Add the linear regression line to the plot
x = np.linspace(min(x_matrix), max(x_matrix), 100)
y = slope * x + intercept
plt.plot(x, y, "-r")

# Add axis labels and a title to the plot
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Least Squares Regression")

# Display the plot
plt.show()
