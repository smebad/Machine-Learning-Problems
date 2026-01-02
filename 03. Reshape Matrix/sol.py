# Reshape Matrix
# Solution:
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int|float]) -> list[list[int|float]]:
    if len(a)*len(a[0]) != new_shape[0]*new_shape[1]:
        return []
    return np.array(a).reshape(new_shape).tolist()


# Test Cases:
# Test Case 1
a = [[1,2,3,4],[5,6,7,8]]
new_shape = (4, 2)
print(reshape_matrix(a, new_shape))  # Output: [[1, 2], [3, 4], [5, 6], [7, 8]]

# Test Case 2
a = [[1,2,3],[4,5,6]]
new_shape = (3, 2)
print(reshape_matrix(a, new_shape))  # Output: [[1, 2], [3, 4], [5, 6]]

# Test Case 3
a = [[1,2],[3,4]]
new_shape = (4, 2)
print(reshape_matrix(a, new_shape))  # Output: []
