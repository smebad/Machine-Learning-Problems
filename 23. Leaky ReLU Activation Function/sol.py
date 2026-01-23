# Leaky ReLU Activation Function
# Solution:
def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
    return z if z > 0 else alpha * z

# Test cases:
print(leaky_relu(0))        # Output: 0
print(leaky_relu(1))        # Output: 1
print(leaky_relu(-1))       # Output: -0.01
print(leaky_relu(-2, 0.1))  # Output: -0.2
