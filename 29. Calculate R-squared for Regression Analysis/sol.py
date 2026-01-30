# Calculate R-squared for Regression Analysis

# Task: Compute the R-squared Value in Regression Analysis
# R-squared, also known as the coefficient of determination, is a measure that indicates how well the independent variables explain the variability of the dependent variable in a regression model.

# Your Task: To implement the function r_squared(y_true, y_pred) that calculates the R-squared value, given arrays of true values y_true and predicted values y_pred.

# Example:
# Input:
# import numpy as np

# y_true = np.array([1, 2, 3, 4, 5])
# y_pred = np.array([1.1, 2.1, 2.9, 4.2, 4.8])
# print(r_squared(y_true, y_pred))
# Output:
# 0.989
# Reasoning:
# The R-squared value is calculated to be 0.989, indicating that the regression model explains 98.9% of the variance in the dependent variable.


# Solution:

import numpy as np
def r_squared(y_true, y_pred):
    if np.array_equal(y_true, y_pred):
        return 1.0

    y_mean = np.mean(y_true)
    ssr = np.sum((y_true - y_pred) ** 2)
    sst = np.sum((y_true - y_mean) ** 2)

    try:
        r2 = 1 - (ssr / sst)
        if np.isinf(r2):
            return 0.0
        return round(r2, 3)
    except ZeroDivisionError:
        return 0.0

# Test Case:
y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1.1, 2.1, 2.9, 4.2, 4.8])
print(r_squared(y_true, y_pred))  # Output: 0.989