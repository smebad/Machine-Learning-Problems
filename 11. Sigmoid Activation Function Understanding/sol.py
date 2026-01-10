# Sigmoid Activation Function Understanding
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
