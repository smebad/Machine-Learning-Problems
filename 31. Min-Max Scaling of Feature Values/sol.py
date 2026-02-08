# Min-Max Scaling of Feature Values
# Implement a function that performs Min-Max Normalization on a list of integers, scaling all values according to the formula. Min-Max normalization helps ensure that all features contribute equally to a model by scaling them to a common range.

# Example:
# Input:
# min_max([1, 2, 3, 4, 5])
# Output:
# [0.0, 0.25, 0.5, 0.75, 1.0]
# Reasoning:
# The minimum value (1) becomes 0.0, the maximum value (5) becomes 1.0, and the values in between are scaled proportionally. For instance, 3 is exactly halfway between 1 and 5, so it becomes 0.5.


# Solution:
def min_max(x: list[float]) -> list[float]:
  x_min = min(x)
  x_max = max(x)
  
  if x_max == x_min:
      return [0.0] * len(x)
  
  return [(val - x_min) / (x_max - x_min) for val in x]

# Test Cases
print(min_max([1, 2, 3, 4, 5]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(min_max([10, 20, 30]))       # Output: [0.0, 0.5, 1.0]
print(min_max([5, 5, 5]))          # Output: [0.0, 0.0, 0.0] (all values are the same, so they are all normalized to 0.0)