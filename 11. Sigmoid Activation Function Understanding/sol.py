# Sigmoid Activation Function Understanding
# Write a Python function that computes the output of the sigmoid activation function given an input value z. The function should return the output rounded to four decimal places.

# Example:
# Input:
# z = 0
# Output:
# 0.5
# Reasoning:
# The sigmoid function is defined as σ(z) = 1 / (1 + exp(-z)). For z = 0, exp(-0) = 1, hence the output is 1 / (1 + 1) = 0.5.


# Solution:
import math
def sigmoid(z: float) -> float:
   result = 1 / (1 + math.exp(-z))
   return round(result, 4)

# Test Case
# Test Case 1:
z = 0
print(sigmoid(z))  # Output: 0.5

# Test Case 2:
z = 2
print(sigmoid(z))  # Output: 0.8807970779778823

# Test Case 3:
z = -2
print(sigmoid(z))  # Output: 0.11920292202211775