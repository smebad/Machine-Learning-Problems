# Implement Gini Impurity Calculation for a Set of Classes
# Solution:
import numpy as np

def gini_impurity(y: list[int]) -> float:

    classes = set(y)
    n = len(y)

    gini_impurity = 0

    for cls in classes:
        gini_impurity += (y.count(cls)/n)**2

    return round(1-gini_impurity,3)

# Test Case:
y = [0, 1, 1, 1, 0]
print(gini_impurity(y))  # Output: 0.48
