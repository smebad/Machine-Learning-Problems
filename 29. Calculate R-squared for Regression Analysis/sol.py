# Calculate R-squared for Regression Analysis
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
