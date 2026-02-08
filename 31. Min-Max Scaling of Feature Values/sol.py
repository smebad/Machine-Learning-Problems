# Min-Max Scaling of Feature Values
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
