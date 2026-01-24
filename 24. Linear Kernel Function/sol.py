# Linear Kernel Function
# Solution:
import numpy as np

def kernel_function(x1, x2):
    return np.inner(x1, x2)

# Test Case:
if __name__ == "__main__":
    x1 = np.array([1, 2, 3])
    x2 = np.array([4, 5, 6])
    
    result = kernel_function(x1, x2)
    print(result)  # Output: 32
